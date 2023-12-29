from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate

from user.serializers import UserSerializer, AuthRequestSerializer


class AuthView(APIView):

    def post(self,request):
        if request.path == '/api/user/register/':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.path == '/api/user/login/':
            email = request.data.get('email')
            password = request.data.get('password')
            serializer = AuthRequestSerializer(data=request.data)
            if serializer.is_valid():
                user = authenticate(email=email, password=password)
                if  not user:
                    return Response({'message':'Email or password is incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
                
                user.last_login = timezone.now()
                user.save()
                token= Token.objects.get_or_create(user=user)
                return Response({'token':token[0].key}, status=status.HTTP_200_OK)
            
            
            return Response({"message":"All fields are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.path == '/api/user/logout/':
            user = int(request.data.get('user_id'))
            token = get_object_or_404(Token, user=user)
            token.delete()

            return Response({"message":" User Logout successfully"}, status=status.HTTP_200_OK)