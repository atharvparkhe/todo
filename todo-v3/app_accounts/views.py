from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import *
from .threads import *
from .serializer import *


class APILogIn(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = loginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data["email"]
                password = serializer.data["password"]
                stu_obj = UserModel.objects.filter(email=email).first()
                if stu_obj is None:
                    return Response({"status":400, "result":"Account does not exist"})
                if not stu_obj.is_verified:
                    return Response({"status":400, "result":"Email not verified. Check your mail"})
                user = authenticate(email=email, password=password)
                jwt_token = RefreshToken.for_user(user)
                return Response({"status":200, "result":"Login successfull", "token":str(jwt_token.access_token)})
            return Response({"status":400, "error":serializer.errors})
        except Exception as e:
            print(e)
        return Response({"status":500, "message":"something went wrong"})


class APISignUp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = signupSerializer(data=data)
            if serializer.is_valid():
                name = serializer.data["name"]
                email = serializer.data["email"]
                password = serializer.data["password"]
                if UserModel.objects.filter(email=email).first():
                    return Response({"status":400, "result":"Acount already exists."})
                else:
                    new_student = UserModel.objects.create(email=email, name=name)
                    new_student.set_password(password)
                    new_student.save()
                    return Response({"status":200, "result":"Account created, verification mail sent", "data":serializer.data})
            return Response({"status":400, "error":serializer.errors})
        except Exception as e:
            print(e)
        return Response({"status":500, "message":"something went wrong"})
        

class APIVerify(APIView):
    def get(self, request, token):
        try:
            data = request.data
            user_obj = UserModel.objects.filter(verification_token = token).first()
            if user_obj:
                if user_obj.is_verified:
                    return Response({"status":400, "result":"Account is already verified"})
                user_obj.is_verified = True
                user_obj.save()
                return Response({"status":200, "result":"Account verification successfull"})
        except Exception as e:
            print(e)
        return Response({"status":500, "message":"something went wrong"})

class APIForget(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = signupSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data["email"]
                if not UserModel.objects.get(email=email):
                    return Response({"status":400, "result":"Account does not exists"})
                thread_obj = send_forgot_link(email)
                thread_obj.start()
                return Response({"status":200, "result":"reset mail sent"})
            return Response({"status":400, "error":serializer.errors})
        except Exception as e:
            print(e)
        return Response({"status":500, "message":"something went wrong"})

class APIReset(APIView):
    def post(self, request, token):
        try:
            data = request.data
            if not cache.get(token):
                return Response({"status":400, "result":"Acount already exists."})
            else:
                stu_obj = UserModel.objects.get(email = cache.get(token))
                if stu_obj:
                    serializer = signupSerializer(data=data)
                    if serializer.is_valid():
                        npw = serializer.data["npw"]
                        cpw = serializer.data["cpw"]
                        if npw == cpw:
                            stu_obj.set_password(cpw)
                            stu_obj.save()
                            return Response({"status":200, "result":"Password changed successfull"})
                else:
                    return Response({"status":400, "result":"Acount does not exists."})
        except Exception as e:
            print(e)
        return Response({"status":500, "message":"something went wrong"})