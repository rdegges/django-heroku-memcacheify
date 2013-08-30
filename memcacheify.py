from os import environ


# Memcache addon environment variables.
# See: https://addons.heroku.com/memcache
MEMCACHE_ENV_VARS = (
    'MEMCACHE_PASSWORD',
    'MEMCACHE_SERVERS',
    'MEMCACHE_USERNAME',
)


# MemCachier addon environment variables.
# See: https://addons.heroku.com/memcachier
MEMCACHIER_ENV_VARS = (
    'MEMCACHIER_PASSWORD',
    'MEMCACHIER_SERVERS',
    'MEMCACHIER_USERNAME',
)


def memcacheify(timeout=500):
    """Return a fully configured Django ``CACHES`` setting. We do this by
    analyzing all environment variables on Heorku, scanning for an available
    memcache addon, and then building the settings dict properly.

    If no memcache servers can be found, we'll revert to building a local
    memory cache.

    Returns a fully configured caches dict.
    """
    caches = {}

    if all((environ.get(e, '') for e in MEMCACHE_ENV_VARS)):
        caches['default'] = {
            'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
            'BINARY': True,
            'LOCATION': 'localhost:11211',
            'OPTIONS': {
                'ketama': True,
                'tcp_nodelay': True,
            },
            'TIMEOUT': timeout,
        }
    elif all((environ.get(e, '') for e in MEMCACHIER_ENV_VARS)):
        environ['MEMCACHE_SERVERS'] = environ.get('MEMCACHIER_SERVERS').replace(',', ';')
        environ['MEMCACHE_USERNAME'] = environ.get('MEMCACHIER_USERNAME')
        environ['MEMCACHE_PASSWORD'] = environ.get('MEMCACHIER_PASSWORD')
        caches['default'] = {
            'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
            'BINARY': True,
            'LOCATION': environ.get('MEMCACHIER_SERVERS').replace(',', ';'),
            'OPTIONS': {
                'ketama': True,
                'tcp_nodelay': True,
            },
            'TIMEOUT': timeout,
        }
    elif environ.get('MEMCACHEIFY_USE_LOCAL', False):
        caches['default'] = {
            'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        }
    else:
        caches['default'] = {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }

    return caches
