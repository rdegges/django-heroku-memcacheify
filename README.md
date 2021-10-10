# django-heroku-memcacheify

Automatic Django memcached configuration on Heroku.


![Deploying memcached is easy](https://github.com/rdegges/django-heroku-memcacheify/raw/master/assets/memcacheify.jpg)


## Install

To install ``django-heroku-memcacheify``, simply run
``pip install django-heroku-memcacheify`` and you'll get the latest version
installed automatically.

**NOTE**: If you'd like to install this locally, you'll need to have the
``libmemcached-dev`` libraries installed for this to compile properly. On
Debian and Ubuntu you can install this by running ``sudo aptitude -y install
libmemcached-dev``. If you're using a Mac, you can use
[homebrew](http://mxcl.github.com/homebrew/) and run ``brew install libmemcached``.


## Usage

Modify your Django ``settings.py`` file, and set:

``` python
from memcacheify import memcacheify

CACHES = memcacheify()
```

Next, ensure pylibmc is present in your ``requirements.txt`` file (or one
included from it), so the Heroku Python buildpack will detect the necessary
C dependencies and 'bootstrap' your application.

Assuming you have a memcache server available to your application on Heroku, it
will instantly be available. If you have no memcache addon provisioned for your
app, ``memcacheify`` will default to using local memory caching as a backup :)


## Heroku Setup

Now that you've got Django configured to use memcache, all you need to do is
install one memcache addons that Heroku provides!

I personally recommend [MemCachier](https://addons.heroku.com/memcachier) --
they're stable, cheap, great!

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


## Local Development
If you have a memcached server locally for development that doesn't support
authentication, you can still use memcache by setting an environment variable
`MEMCACHEIFY_USE_LOCAL=True`.

This will set the default cache to `django_pylibmc.memcached.PyLibMCCache`

If there are no environment variables for memcache or memcacheify, the default
cache will be local memory `django.core.cache.backends.locmem.LocMemCache`.


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
$ flake8
$ nosetests
.............
----------------------------------------------------------------------
Ran 13 tests in 0.166s

OK
```


## Changelog

v1.0.1: 10-10-2021

    - Fixing PyPI description

v1.0.0: 01-04-2016

    - Update django-pylibmc dependency to >=0.6.1.
    - Officially support Python 3.5.
    - Stop testing on Python 2.6.

v0.8: 11-12-2014

    - Adding support for memcachedcloud!

v0.7: 9-22-2014

    - Upgrading dependencies (again)!

v0.6: 9-20-2014

    - Upgrading dependencies.

v0.5: 12-31-2013

    - Making the timeout option configurable.
    - Removing Python 2.5 support.
    - Adding an option to use memcached locally without SASL.
    - Updating the README, explaining how to use memcached locally.

v0.4: 12-5-2012

    - Update which allows memcachier users to support multiple servers >:)
      Thanks @alexlod!

v0.3: 6-27-2012

    - Fixing broken memcachier support.

v0.2: 5-22-2012

    - Adding support for memcachier Heroku addon.
    - Updating documentation.
    - Refactoring implementation for clarity.
    - Adding better tests.

v0.1: 5-2-2012

    - Initial release!
