from rest_framework import serializers
from .models import Profile
#from .mock_db import *  

class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(required = False)
    email = serializers.EmailField()
    isHidden = serializers.BooleanField(required=False, default=False)

class ConnectionSerializer(serializers.Serializer):
    id1 = serializers.PrimaryKeyRelatedField(
        queryset = Profile.objects.all()
    )
    id2 = serializers.PrimaryKeyRelatedField(
        queryset = Profile.objects.all()
    )

    def validate(self, data):
        if (not Profile.objects.filter(pk=self.id1).exists()) or (not Profile.objects.filter(pk=self.id2).exists()):
            raise serializers.ValidationError("Profile IDs must exist before creating a connection.")
        else:
            return data