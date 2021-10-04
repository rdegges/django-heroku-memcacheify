from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name='django-heroku-memcacheify',
    version='1.0.0',
    py_modules=('memcacheify',),

    # Packaging options:
    zip_safe=False,
    include_package_data=True,

    # Package dependencies:
    install_requires=['django-pylibmc>=0.6.1'],

    # Metadata for PyPI:
    author='Randall Degges',
    author_email='r@rdegges.com',
    license='UNLICENSE',
    url='https://github.com/rdegges/django-heroku-memcacheify',
    keywords='django heroku cloud cache memcache memcached awesome epic',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    description='Automatic Django memcached configuration on Heroku.',
    long_description=open(normpath(join(dirname(abspath(__file__)),
                                        'README.md'))).read(),
    long_description_content_type='text/markdown'

)
