from django.urls import path
from .views import *


urlpatterns = [
     path("test-server", test_server, name="test_server"),
]