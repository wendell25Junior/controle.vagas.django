import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import sensorproject.rotas  # ← IMPORTANTE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sensorproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            sensorproject.rotas.websocket_urlpatterns
        )
    ),
})
