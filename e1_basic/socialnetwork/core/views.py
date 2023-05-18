from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer, ConnectionSerializer, get_all_connections_serialized
from .mock_db import *  



@api_view(['GET', 'POST'])
def  profiles_list(request):
    if request.method == 'GET':
        serializer = ProfileSerializer(ProfileBase.values(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        requestSerializer = ProfileSerializer(data=request.data)
        if requestSerializer.is_valid():
            responseSerializer = ProfileSerializer(create_new_profile(email = requestSerializer.validated_data['email'], isHidden = requestSerializer.validated_data['isHidden']))
            return Response(responseSerializer.data)
        else:
            return Response(requestSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def  connections_list(request):
    if request.method == 'GET':
        data = get_all_connections_serialized()
        return Response(data)
    elif request.method == 'POST':
        requestSerializer = ConnectionSerializer(data=request.data)
        if requestSerializer.is_valid():
            create_new_connection(id1 = requestSerializer.validated_data['id1'],id2 = requestSerializer.validated_data['id2'])
            data = get_all_connections_serialized()
            return Response(data)
        return Response(requestSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile_detail(request, id):
    if(ProfileBase.get(id) == None):
        return Response(status = status.HTTP_404_NOT_FOUND)
    else:
        serializer = ProfileSerializer(ProfileBase.get(id))
        return Response(serializer.data)