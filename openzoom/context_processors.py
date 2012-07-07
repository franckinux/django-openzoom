#!/usr/bin/env python
# -*- coding: utf8 -*-

"""openzoom.context_processors
(C) Franck Barbenoire <fbarbenoire@yahoo.fr>
License : GPL v3"""

from django.conf import settings as proj_settings

def settings(request):
    return {
        'openzoomsettings': {
            'url': proj_settings.OPENZOOM_STATIC_URL,
            'secure': proj_settings.OPENZOOM_FLASH_SECURE,
        }
    }