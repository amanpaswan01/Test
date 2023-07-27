from channels.db import database_sync_to_async
from .models import ConnectedAgent,Device
import json

@database_sync_to_async
def del_live_client(self,client_channel_name):
  client=ConnectedAgent.objects.filter(client_channel_name=client_channel_name).first()
  device=Device.objects.filter(connection=client).first()
  id=client.id
  client.delete()
  return device.id

@database_sync_to_async
def update_or_create_device(self,data):
    # print(data['unique_id'])
    connected_agent=ConnectedAgent.objects.filter(client_channel_name=self.channel_name)[0]
    device=Device.objects.filter(product_id=data['unique_id'])
    is_new=False
    if len(device)>0:
        device=device[0]
        device.connection=connected_agent
        device.product_id=data['unique_id']
        device.username=data['current_user']['username']
        device.full_name=data['current_user']['full_name']
        device.other_info=json.dumps(data)
        device.save()
        
        
    else:
        device=Device(  connection=connected_agent,
                        product_id=data['unique_id'],
                        username=data['current_user']['username'],
                        full_name=data['current_user']['full_name'],
                        other_info=json.dumps(data) )
        device.save()
        is_new=True

    return device.id,is_new
