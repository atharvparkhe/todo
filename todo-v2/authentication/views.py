from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import *
from .threads import *
from .serializers import *


@api_view(["POST"])
def signUp(request):
    try:
        data = request.data
        serializer = signupSerializer(data=data)
        if serializer.is_valid():
            name = serializer.data["name"]
            email = serializer.data["email"]
            password = serializer.data["password"]
            if UserModel.objects.filter(email=email).first():
                return Response({"result":"Acount already exists."}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                new_customer = UserModel.objects.create(email=email, name=name)
                new_customer.set_password(password)
                new_customer.save()
                return Response({"result":"Account created"}, status=status.HTTP_201_CREATED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def logIn(request):
    try:
        data = request.data
        serializer = loginSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            password = serializer.data["password"]
            customer_obj = UserModel.objects.filter(email=email).first()
            if customer_obj is None:
                return Response({"result":"Account does not exist"}, status=status.HTTP_404_NOT_FOUND)
            user = authenticate(email=email, password=password)
            if not user:
                return Response({"result":"Incorrect password"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            jwt_token = RefreshToken.for_user(user)
            return Response({"result":"Login successfull", "token":str(jwt_token.access_token)}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def forgot(request):
    try:
        data = request.data
        serializer = emailSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            if not UserModel.objects.get(email=email):
                return Response({"result":"Account does not exists"}, status=status.HTTP_404_NOT_FOUND)
            thread_obj = send_forgot_link(email)
            thread_obj.start()
            return Response({"result":"reset mail sent"}, status=status.HTTP_200_OK)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def reset(request):
    try:
        data = request.data
        serializer = OTPSerializer(data=data)
        if serializer.is_valid():
            otp = serializer.data["otp"]
            if not UserModel.objects.filter(otp=otp).first():
                return Response({"result":"OTP expired"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            user_obj = UserModel.objects.get(otp=otp)
            npw = serializer.data["npw"]
            cpw = serializer.data["cpw"]
            if npw == cpw:
                user_obj.set_password(cpw)
                user_obj.save()
                return Response({"result":"Password changed successfull"}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def resendForgot(request):
    try:
        data = request.data
        serializer = emailSerializer(data=data)
        if serializer.is_valid():
            email = serializer.data["email"]
            thread_obj = send_forgot_link(email)
            thread_obj.start()
            return Response({"message":"OTP sent on your email"}, status=status.HTTP_200_OK)
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
