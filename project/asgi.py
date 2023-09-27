
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import chat.routing

application = ProtocolTypeRouter(
    {
        'http' : get_asgi_application(),
        'websocket': URLRouter(
            chat.routing.websocket_urlpatterns
        )
    }
)

