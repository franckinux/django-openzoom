#!/usr/bin/env python
# -*- coding: utf8 -*-

"""setup
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from distutils.core import setup
from setuptools import find_packages

setup(name = "django-openzoom",
    version = "0.1",
    description = "Django application for displaying an image you can zoom in",
    author = "Franck Barbenoire",
    author_email = "fbarbenoire@yahoo.fr",
    url = "https://github.com/franckinux/django-openzoom",
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = ['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Framework :: Django',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content']
) 
