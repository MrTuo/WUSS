"""
WSGI config for WUSS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WUSS.settings")

application = get_wsgi_application()

import _thread
from update_manage.views import check_all_update

_thread.start_new_thread(check_all_update,())