from os import environ


# Some constant globals that memcached uses.
MEMCACHE_PASSWORD = 'MEMCACHE_PASSWORD'
MEMCACHE_SERVERS = 'MEMCACHE_SERVERS'
MEMCACHE_USERNAME = 'MEMCACHE_USERNAME'


def memcacheify():
    """Return a fully configured Django ``CACHES`` setting. We do this by
    analyzing all environment variables on Heorku, scanning for an available
    memcache addon, and then building the settings dict properly.

    If no memcache servers can be found, we'll revert to building a local
    memory cache.

    Returns a fully configured caches dict.
    """
    caches = {}

    if all((
        environ.get(MEMCACHE_PASSWORD, ''),
        environ.get(MEMCACHE_SERVERS, ''),
        environ.get(MEMCACHE_USERNAME, '')
    )):
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
