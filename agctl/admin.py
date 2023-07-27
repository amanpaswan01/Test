from django.contrib import admin
from agctl.models import ConnectedAgent,Device
# Register your models here.



@admin.register(ConnectedAgent)
class ConnectedAgentAdmin(admin.ModelAdmin):
    list_display = ['client_channel_name','group','ip_address','created_at',]
    readonly_fields=['created_at']



@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['product_id','username','full_name']
    readonly_fields=['created_at','updated_at']