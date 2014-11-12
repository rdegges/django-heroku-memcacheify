from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'django-heroku-memcacheify',
    version = '0.8',
    py_modules = ('memcacheify',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['django-pylibmc==0.5.0'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'r@rdegges.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/django-heroku-memcacheify',
    keywords = 'django heroku cloud cache memcache memcached awesome epic',
    description = 'Automatic Django memcached configuration on Heroku.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
