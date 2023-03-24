from json import JSONDecodeError
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Alerts
from .serializer import AlertSerializer
from rest_framework.decorators import api_view



# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET', 'POST'])
def alerts(request, format=None):
    if request.method == 'GET':
        alerts = Alerts.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
def alert_detail(request, id, format=None):
    # sourcery skip: remove-unnecessary-else, remove-unreachable-code, swap-if-else-branches
    
    try:
        alerts =  Alerts.objects.get(pk=id)
    except Alerts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #Sourcery skip
    if request.method == "GET":
       serializer = AlertSerializer(alerts)
       return Response(serializer.data)
    #
    if request.method == "PUT":
        serializer = AlertSerializer(alerts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        serializer = AlertSerializer(alerts) 
        alerts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

def settings(request):
    return HttpResponse('Das ist die Settings Seite')