from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

#Mock bases creation
ProfileBase = {}
ConnectionBase = {}

#Mock profiles creation and registration
mockProfile1 = Profile(email = "1@email.com")
ProfileBase[mockProfile1.email] = mockProfile1
ConnectionBase[mockProfile1.email] = []

mockProfile2 = Profile(email = "2@email.com")
ProfileBase[mockProfile2.email] = mockProfile2
ConnectionBase[mockProfile2.email] = []

mockProfile3 = Profile(email = "3@email.com")
ConnectionBase[mockProfile3.email] = []
ProfileBase[mockProfile3.email] = mockProfile3

#Conection creation (1<>2)
ConnectionBase[mockProfile1.email].append(mockProfile2.email)
ConnectionBase[mockProfile2.email].append(mockProfile3.email)


# Create your views here.
@api_view()
def  profiles_list(request):
    serializer = ProfileSerializer(ProfileBase.values(), many=True)
    return Response(serializer.data)
