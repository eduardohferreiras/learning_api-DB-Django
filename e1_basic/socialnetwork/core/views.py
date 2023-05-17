from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from .mock_db import *  


# Create your views here.
@api_view(['GET', 'POST'])
def  profiles_list(request):
    serializer = ProfileSerializer(ProfileBase.values(), many=True)
    return Response(serializer.data)
