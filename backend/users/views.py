from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth import login as login_
from rest_framework.authtoken.models import Token
from .models import CustomUser
import datetime

from .serializers import UserSerializer, UserSerializerLogin

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    print(request.data)

    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=request.data['username'], email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        response = Response({'token': token.key, 'user': serializer.data})

        return response

    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    print(request.data)
    user = get_object_or_404(CustomUser, email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    login_(request, user)
    serializer = UserSerializerLogin(user)
    response = Response({'user': serializer.data})
    response.set_cookie('token', token.key, max_age=604800)
    return response

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")