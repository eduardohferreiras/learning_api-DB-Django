from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer, ConnectionSerializer
from .mock_db import *  


@api_view(['GET', 'POST'])
def  profiles_list(request):
    if request.method == 'GET':
        serializer = ProfileSerializer(ProfileBase.values(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        requestSerializer = ProfileSerializer(data=request.data)
        if requestSerializer.is_valid():
            print(requestSerializer.validated_data)
            responseSerializer = ProfileSerializer(create_new_profile(email = requestSerializer.validated_data['email'], isHidden = requestSerializer.validated_data['isHidden']))
            return Response(responseSerializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def  connections_list(request):
    if request.method == 'GET':
        data = []
        for profileConnectionsRowKey in ConnectionBase.keys():
            profileConnectionsRowSerializer = ConnectionSerializer(ConnectionBase[profileConnectionsRowKey], many=True)
            data.extend(profileConnectionsRowSerializer.data)
        return Response(data)
    else:
        return Response("TBD")


@api_view(['GET'])
def profile_detail(request, id):
    if(ProfileBase.get(id) == None):
        return Response(status = status.HTTP_404_NOT_FOUND)
    else:
        serializer = ProfileSerializer(ProfileBase.get(id))
        return Response(serializer.data)