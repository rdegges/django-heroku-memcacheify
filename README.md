# django-heroku-memcacheify

Automatic Django memcached configuration on Heroku.


![Deploying memcached is easy](https://github.com/rdegges/django-heroku-memcacheify/raw/master/assets/memcacheify.jpg)


## Install

To install ``django-heroku-memcacheify``, simply run
``pip install django-heroku-memcacheify`` and you'll get the latest version
installed automatically.


## Usage

Modify your Django ``settings.py`` file, and set:

``` python
from memcacheify import memcacheify

CACHES = memcacheify()
```

That's it.

Assuming you have a memcache server available to your application on Heroku, it
will instantly be available. If you have no memcache addon provisioned for your
app, ``memcacheify`` will default to using local memory caching as a backup :)


## Heroku Setup

Now that you've got Django configured to use memcache, all you need to do is
install one of the two excellent memcache addons that Heroku provides!

- [Memcache](https://addons.heroku.com/memcache) - Been around longer, but
  pretty expensive, or
- [MemCachier](https://addons.heroku.com/memcachier) - Newer, less expensive.

Let's say I want to install the ``memcachier`` addon, I could simply run:

``` bash
$ heroku addons:add memcachier:25
$ heroku config
...
MEMCACHIER_SERVERS    => memcachier1.example.net
MEMCACHIER_USERNAME   => bobslob
MEMCACHIER_PASSWORD   => l0nGr4ndoMstr1Ngo5strang3CHaR4cteRS
...
```

The example above will provision a *free* 25m memcache server for your
application. Assuming everything worked, ``heroku config``'s output should show
that you now have 3 new environment variables set.


## Testing Your Cache

If you don't trust me, and want to make sure your caching is working as
expected, you may do the following:

``` bash
$ heroku run python manage.py shell
Running python manage.py shell attached to terminal... up, run.1
Python 2.7.2 (default, Oct 31 2011, 16:22:04)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.cache import cache
>>> cache.set('memcache', 'ify!')
True
>>> cache.get('memcache')
'ify!'
>>>
```

Assuming everything is working, you should be able to set and retrieve cache
keys.


## References

If you're confused, you should probably read:

- [Heroku's Getting Started Guide](http://devcenter.heroku.com/articles/django)
- [Heroku's memcache Addon Documentation](https://devcenter.heroku.com/articles/memcache#using_memcache_from_python)
- [Heroku's memcachier Addon Documentation](https://devcenter.heroku.com/articles/memcachier)


## Tests

[![Build Status](https://secure.travis-ci.org/rdegges/django-heroku-memcacheify.png?branch=master)](http://travis-ci.org/rdegges/django-heroku-memcacheify)

Want to run the tests? No problem:

``` bash
$ git clone git://github.com/rdegges/django-heroku-memcacheify.git
$ cd django-heroku-memcacheify
$ python setup.py develop
...
$ pip install -r requirements.txt  # Install test dependencies.
$ nosetests
.............
----------------------------------------------------------------------
Ran 13 tests in 0.166s

OK
```
