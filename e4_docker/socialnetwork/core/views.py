from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Connection
from .serializers import ProfileSerializer, ConnectionSerializer
#from .mock_db import *  

@api_view(['GET', 'POST'])
def profiles_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        requestSerializer = ProfileSerializer(data=request.data)
        if requestSerializer.is_valid():
            profile = Profile()
            profile.email = requestSerializer.data['email']
            profile.isHidden = requestSerializer.data['isHidden']
            profile.save()
            responseSerializer = ProfileSerializer(profile)
            return Response(responseSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(requestSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET','PATCH'])
def profile_detail(request, id):
    if request.method == 'GET':
        if(not Profile.objects.filter(pk=id).exists()):
            return Response(status = status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProfileSerializer(Profile.objects.get(pk = id))
            return Response(serializer.data)
    elif request.method == 'PATCH':
        if(not Profile.objects.filter(pk=id).exists()):
            return Response(status = status.HTTP_404_NOT_FOUND)
        else:
            print(request.data)
            if (not 'isHidden' in request.data.keys()) or (not isinstance(request.data['isHidden'], bool)):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                profile = Profile.objects.get(pk = id)
                profile.isHidden = request.data['isHidden']
                profile.save()
                serializer = ProfileSerializer(profile)
                return Response(serializer.data)

@api_view(['GET', 'POST'])
def connections_list(request):
    if request.method == 'GET':
        connections = Connection.objects.all()
        serializer = ConnectionSerializer(connections, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        requestSerializer = ConnectionSerializer(data=request.data)
        if requestSerializer.is_valid():
            connection1 = Connection()
            connection1.id1 = requestSerializer.validated_data['id1']
            connection1.id2 = requestSerializer.validated_data['id2']
            connection1.save()
            
            connection2 = Connection()
            connection2.id1 = requestSerializer.validated_data['id2']
            connection2.id2 = requestSerializer.validated_data['id1']
            connection2.save()

            connections = Connection.objects.all()
            responseSerializer = ConnectionSerializer(connections, many=True)
            return Response(responseSerializer.data, status=status.HTTP_201_CREATED)
        return Response(requestSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def connection_recomendation(request, id):
    if(not Profile.objects.filter(pk=id).exists()):
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    recommendations = {}
    
    #for each friend of the profile
    for connection in Connection.objects.filter(id1 = id):
        #for each friend of the the friend
        for connectionOfConnection in Connection.objects.filter(id1 = connection.id2):
            #score of this profile increases, if not hidden
            profile = Profile.objects.get(pk = connectionOfConnection.id2.id)
            if (not profile.isHidden) and (profile.pk != id):
                if recommendations.get(profile.pk) == None:
                    recommendations[profile.pk] = 1
                else:
                    recommendations[profile.pk] = recommendations[profile.pk] + 1

    #remove profiles that are already connected
    for connection in Connection.objects.filter(id1 = id):
        if connection.id2.id in recommendations.keys():
            recommendations.pop(connection.id2.id)
    
    #return orderded list of recommendations 
    sortedRecomendation = dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True))

    return Response(sortedRecomendation)