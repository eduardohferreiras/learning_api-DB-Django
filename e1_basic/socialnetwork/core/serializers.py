from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.EmailField()
    isHidden = serializers.BooleanField()
    
