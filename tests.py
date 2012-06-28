from os import environ
from unittest import TestCase

from memcacheify import memcacheify


class Memcacheify(TestCase):

    def test_uses_local_memory_backend_if_no_memcache_addon_is_available(self):
        self.assertEqual(memcacheify(), {'default':
            {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
        })

    def tests_uses_local_memory_backend_if_one_of_the_memcache_env_vars_is_missing(self):
        environ['MEMCACHE_PASSWORD'] = 'GCnQ9DhfEJqNDlo1'
        environ['MEMCACHE_SERVERS'] = 'mc3.ec2.northscale.net'
        self.assertEqual(memcacheify(), {'default':
            {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
        })
        del environ['MEMCACHE_PASSWORD']
        del environ['MEMCACHE_SERVERS']

    def test_sets_proper_backend_when_memcache_addon_is_available(self):
        environ['MEMCACHE_PASSWORD'] = 'GCnQ9DhfEJqNDlo1'
        environ['MEMCACHE_SERVERS'] = 'mc3.ec2.northscale.net'
        environ['MEMCACHE_USERNAME'] = 'appxxxxx%40heroku.com'
        self.assertEqual(memcacheify()['default']['BACKEND'],
                'django_pylibmc.memcached.PyLibMCCache')
        del environ['MEMCACHE_PASSWORD']
        del environ['MEMCACHE_SERVERS']
        del environ['MEMCACHE_USERNAME']

    def test_uses_local_memory_backend_if_no_memcachier_addon_is_available(self):
        environ['MEMCACHIER_PASSWORD'] = 'xxx'
        environ['MEMCACHIER_SERVERS'] = 'mc1.ec2.memcachier.com'
        self.assertEqual(memcacheify(), {'default':
            {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
        })
        del environ['MEMCACHIER_PASSWORD']
        del environ['MEMCACHIER_SERVERS']

    def test_sets_proper_backend_when_memcachier_addon_is_available(self):
        environ['MEMCACHIER_PASSWORD'] = 'xxx'
        environ['MEMCACHIER_SERVERS'] = 'mc1.ec2.memcachier.com'
        environ['MEMCACHIER_USERNAME'] = 'xxx'

        caches = memcacheify()
        self.assertEqual(caches['default']['BACKEND'], 'django_pylibmc.memcached.PyLibMCCache')
        self.assertEqual(environ['MEMCACHE_SERVERS'], environ['MEMCACHIER_SERVERS'])
        self.assertEqual(environ['MEMCACHE_USERNAME'], environ['MEMCACHIER_USERNAME'])
        self.assertEqual(environ['MEMCACHE_PASSWORD'], environ['MEMCACHIER_PASSWORD'])

        del environ['MEMCACHIER_PASSWORD']
        del environ['MEMCACHIER_SERVERS']
        del environ['MEMCACHIER_USERNAME']
        del environ['MEMCACHE_PASSWORD']
        del environ['MEMCACHE_SERVERS']
        del environ['MEMCACHE_USERNAME']
