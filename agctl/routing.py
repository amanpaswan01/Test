from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path("agctl/<str:type>/",consumers.AgentListener.as_asgi()),
    path("web_client/",consumers.WebClient.as_asgi()),
]