from os import environ


# Memcache addon environment variables.
# See: https://addons.heroku.com/memcache
MEMCACHE_ENV_VARS = (
    'MEMCACHE_PASSWORD',
    'MEMCACHE_SERVERS',
    'MEMCACHE_USERNAME',
)


def memcacheify():
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
            'LOCATION': 'localhost:11211',
            'TIMEOUT': 500,
            'BINARY': True,
            'OPTIONS': {
                'tcp_nodelay': True,
                'ketama': True,
            }
        }
    else:
        caches['default'] = {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }

    return caches
