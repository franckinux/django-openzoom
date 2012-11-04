#!/usr/bin/env python
# -*- coding: utf8 -*-

"""openzoom.urls
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.conf.urls import patterns, url

urlpatterns = patterns('',

    url(r'^(?P<directory>.+)/$', 'openzoom.views.html'),
)
