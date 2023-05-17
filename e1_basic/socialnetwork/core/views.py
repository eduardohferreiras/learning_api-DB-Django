from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from .mock_db import *  


# Create your views here.
@api_view(['GET', 'POST'])
def  profiles_list(request):
    if request.method == 'GET':
        serializer = ProfileSerializer(ProfileBase.values(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        return Response(serializer.data)

@api_view(['GET'])
def profile_detail(request, id):
    if(ProfileBase.get(id) == None):
        return Response(status = status.HTTP_404_NOT_FOUND)
    else:
        serializer = ProfileSerializer(ProfileBase.get(id))
        return Response(serializer.data)