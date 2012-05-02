from os import environ
from unittest import TestCase

from memcacheify import memcacheify


class Memcacheify(TestCase):

    def test_uses_local_memory_backend_if_no_memcache_addon_is_available(self):
        self.assertEqual(memcacheify(), {'default':
            {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
        })

    def test_sets_proper_backend_when_memcache_addon_is_available(self):
        environ['MEMCACHE_PASSWORD'] = 'GCnQ9DhfEJqNDlo1'
        environ['MEMCACHE_SERVERS'] = 'mc3.ec2.northscale.net'
        environ['MEMCACHE_USERNAME'] = 'appxxxxx%40heroku.com'
        self.assertEqual(memcacheify()['default']['BACKEND'],
                'django_pylibmc.memcached.PyLibMCCache')
        del environ['MEMCACHE_PASSWORD']
        del environ['MEMCACHE_SERVERS']
        del environ['MEMCACHE_USERNAME']
