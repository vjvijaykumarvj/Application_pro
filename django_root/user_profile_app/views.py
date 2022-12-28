from django.shortcuts import render
from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from .models import User,UserProfile
from.serializer import UserSerializer,UserProfileSeralizer
from rest_framework.response import Response

class UserCreate(APIView):
    def post(self,request):
        user_serializer = UserSerializer(data=request.data)
        userprofile_serilaizer = UserProfileSeralizer(data=request.data)
        if user_serializer.is_valid():
            if userprofile_serilaizer.is_valid():
                user = User.objects.create(
                    name = request.data.get('name', ''),
                    photo = request.data.get ('photo', '')
                )
                UserProfile.objects.create(
                    user = user,
                    age = request.data.get('age', ''),
                    salary = request.data.get('salary', ''),
                    address = request.data.get('address', ''),
                    phone = request.data.get('phone', '')
                )
                return Response({'status' : 'success'},status=status.HTTP_200_OK)
            else:
                return Response(userprofile_serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)