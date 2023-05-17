from rest_framework import serializers

class ProfileSerializer(serializers.Serializer):
    email = serializers.EmailField()
    isHidden = serializers.BooleanField()
