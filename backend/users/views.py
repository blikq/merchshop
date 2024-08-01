from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth import login as login_
from rest_framework.authtoken.models import Token
from .models import CustomUser, VerifyEmail
from django.http import JsonResponse
from django.utils.encoding import uri_to_iri

import datetime
import urllib
import random
from django.utils import timezone

from .serializers import UserSerializer, UserSerializerLogin


@api_view(['POST'])
def signup(request):
    # request.data.remove("pin")
    # user_se = {
    #     "username": request.data["username"],
    #     "email": request.data["email"],
    #     "password": request.data["password"],
    # }
    serializer = UserSerializer(data=request.data)
    print(request.data)
    print(0)
    
    if CustomUser.objects.get(username=request.data['username']):
        return Response("username taken")

    if CustomUser.objects.get(username=request.data['email']):
        return Response("email taken")

    pin = request.headers["pin"]
    if serializer.is_valid():

        serializer.save()
        print(1)
        if int(pin) == VerifyEmail.objects.get(email=request.data["email"]).pin:
            print(2)

            user = CustomUser.objects.get(username=request.data['username'], email=request.data['email'])

            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            response = Response({'token': token.key, 'user': serializer.data})

            return response
        

    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def confirm_email(request):
    # verily = VerifyEmail.objects.update_or_create(email=request.data["email"], pin=random.randint(1000, 9999))
    verily = VerifyEmail.objects.filter(email=request.data["email"]).exists()
    if verily:
        veri = VerifyEmail.objects.get(email=request.data["email"])
        time_ = veri.date_created.timestamp()
        current_time = timezone.now().timestamp()
        dtime = current_time - time_
        if dtime < 0.0:
            return Response("Time Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if dtime <= float(30.0):
            return Response({'time_left': int(30.0 - dtime)})

        veri.pin = random.randint(1000, 9999)
        veri.date_created = timezone.now()
        veri.save()

    if not verily:
        veri = VerifyEmail.objects.create(email=request.data["email"])
        veri.save()


    # verily.save()
    #TODO: Send pin to users

    return Response({"success": True})

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

# @api_view(['POST'])
# def verify_user(request):
#     id_ = uri_to_iri(request.GET.get('id'))
#     # print(id_)
#     user_v = VerifyEmail.objects.get(link = id_)
#     if user_v:
#         print(user_v.user.email)
#         user_v.verified = True
#         user_v.user.is_active = True
#         user_v.save()
#         user_v.user.save()
#         return Response("sucess")

#     return Response(status=status.HTTP_404_NOT_FOUND) 


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    user = request.user
    response = {"username": user.username}

    print(response)
    return JsonResponse(response)


#Non Api-functions

def send_verification_email():
    #TODO: implement this 
    return None