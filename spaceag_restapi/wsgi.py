import os
from dotenv import read_dotenv

from django.core.wsgi import get_wsgi_application

read_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spaceag_restapi.settings')

application = get_wsgi_application()
