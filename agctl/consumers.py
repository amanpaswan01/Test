from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

from channels.db import database_sync_to_async
import string,random
from agctl.models import ConnectedAgent
from channels.exceptions import StopConsumer
import json
from agctl.models import Device
from agctl.async_query import del_live_client,update_or_create_device
from channels.layers import get_channel_layer

class AgentListener(AsyncWebsocketConsumer):

    async def connect(self):
        
        if 'agent'==self.scope['url_route']['kwargs']['type']:
            group=''.join(random.choices(string.ascii_uppercase +string.digits, k=6))
            self.group_name = group
            await self.channel_layer.group_add(self.group_name,self.channel_name)
            connected_agent=ConnectedAgent(ip_address=self.scope['client'][0],client_channel_name=self.channel_name,group=group)
            await database_sync_to_async(connected_agent.save)()
        else:
            self.group_name=self.scope['url_route']['kwargs']['type']
            await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def receive(self,text_data=None, bytes_data=None):
        
        device_id=None
        if text_data:
            try:
                data=json.loads(text_data)
            except Exception as e:
                print("ERROR",e)
            
            if 'system_info' in data:
                device_id,is_new=await update_or_create_device(self,data)
                await self.channel_layer.group_send('web_client',{
                    'type': 'group.broadcast',
                    'message':{"device_id":device_id,"is_new":is_new,"status":True}})
                
            if 'cmd' in data:
                await self.channel_layer.group_send(
                self.group_name,
                {'type':'cmd.agent',
                 'message': text_data,
                 'sender_channel_name': self.channel_name})

    async def cmd_agent(self,event):
        if self.channel_name != event['sender_channel_name']:
            await self.send(json.dumps({'message':event['message']}))
        
          
    async def disconnect(self,event):
        id=await del_live_client(self,self.channel_name)
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
        await self.channel_layer.group_send('web_client',{
            'type': 'group.broadcast',
            'message':{"device_id":id,"status":False}})
        raise StopConsumer()


class WebClient(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.group_name="web_client"
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def receive(self,text_data=None, bytes_data=None):
        pass

    async def group_broadcast(self,event):
        await self.send(json.dumps({'message':event['message']}))


    async def disconnect(self,event):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
        raise StopConsumer()