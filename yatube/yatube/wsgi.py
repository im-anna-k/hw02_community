import os

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yatube.settings')

application = get_wsgi_application()
