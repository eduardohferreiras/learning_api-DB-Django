from rest_framework import serializers
from core.models import Profile

class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(required = False)
    email = serializers.EmailField()
    isHidden = serializers.BooleanField(required=False, default=False)

class ConnectionSerializer(serializers.Serializer):
    id1 = serializers.IntegerField()
    id2 = serializers.IntegerField()
