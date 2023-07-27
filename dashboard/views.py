from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from agctl.models import Device
import json
from django.shortcuts import redirect
# Create your views here.


def landing_page(request):
    context={}
    devices=Device.objects.all()
    context['devices']=devices
    context['title']="Landing Page"
    context['dashboard']='active'
    return render(request,"dashboard/landing_page.html",context)

def all_info(request,device_id):
    context={}
    device=Device.objects.get(pk=device_id)
    context['all_info']=json.loads(device.other_info)
    context['device']=device
    return render(request,'dashboard/all_info.html',context)


def cmd(request,device_id):

    device=Device.objects.get(pk=device_id)

    context={}

    if device.connection:
        context['group']=device.connection.group

        

    else:
        messages.error(request,"Agent Is Offline")
        return redirect('landing_page')

    return render(request,"dashboard/cmd.html",context)