from rest_framework import serializers
#from .mock_db import *  

class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(required = False)
    email = serializers.EmailField()
    isHidden = serializers.BooleanField(required=False, default=False)

class ConnectionSerializer(serializers.Serializer):
    id1 = serializers.IntegerField()
    id2 = serializers.IntegerField()

    def validate(self, data):
        if (not data['id1'] in ProfileBase.keys()) or (not data['id2'] in ProfileBase.keys()):
            raise serializers.ValidationError("Profile IDs must exist before creating a connection.")
        else:
            return data

def get_all_connections_serialized():
    data = []
    for profileConnectionsRowKey in ConnectionBase.keys():
        profileConnectionsRowSerializer = ConnectionSerializer(ConnectionBase[profileConnectionsRowKey], many=True)
        data.extend(profileConnectionsRowSerializer.data)
    return data