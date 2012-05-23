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
