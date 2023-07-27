from django.urls import path
from .views import *


urlpatterns = [
     path("", landing_page, name="landing_page"),
     path("all_info/<int:device_id>", all_info, name="all_info"),
     path("cmd/<int:device_id>", cmd, name="cmd"),
]