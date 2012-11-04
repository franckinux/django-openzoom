#!/usr/bin/env python
# -*- coding: utf8 -*-

"""openzoom.views
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.shortcuts import render

def html(request, directory):
    return render(request,
                  'openzoom/page.html',
                  { 'directory': directory,
                  })
