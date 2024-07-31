import os
from django.core.wsgi import get_wsgi_application
 
# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'semresults.settings')

# Get the WSGI application
application = get_wsgi_application()
