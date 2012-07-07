#!/usr/bin/env python
# -*- coding: utf8 -*-

"""openzoom.templatetags.openzoom
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django import template

register = template.Library()

@register.inclusion_tag('openzoom/script.html', takes_context=True)
def openzoomscript(context, directory, name, width, height):
    return {
        'directory': directory,
        'name': name,
        'width': width,
        'height': height,
        'openzoomsettings': context['openzoomsettings'],
    }

@register.inclusion_tag('openzoom/div.html', takes_context=True)
def openzoomdiv(context):
    return { 'openzoomsettings': context['openzoomsettings'] }

#references
#http://squeeville.com/2009/01/27/django-templatetag-requestcontext-and-inclusion_tag/
#https://github.com/ojii/django-classy-tags/issues/6