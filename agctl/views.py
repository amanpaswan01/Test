from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def test_server(request):

    return JsonResponse({"status":True,"message":"Augmented Transformations"})
