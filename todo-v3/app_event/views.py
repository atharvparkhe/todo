from rest_framework.decorators import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .threads import *


class EventView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user_obj = UserModel.objects.get(email=self.request.user)
            objs = EventModel.objects.filter(user=user_obj)
            serializer = EventSerializer(objs, many=True)
            return Response({"status" : 200, "data" : serializer.data})
        except Exception as e:
            print(e)
            return Response({"status":500, "message":"something went wrong", "error":e})
    def post(self, request):
        try:
            user_obj = UserModel.objects.get(email=self.request.user)
            data = request.data
            serializer = EventSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=user_obj)
                return Response({"status" : 200, "result" : "success", "data" : serializer.data})
            else:
                return Response({"status" : 400, "error" : serializer.errors})
        except Exception as e:
            print(e)
            return Response({"status":500, "message":"something went wrong", "error":e})
    def patch(self, request):
        try:
            user_obj = UserModel.objects.get(email=self.request.user)
            data = request.data
            todo_obj = EventModel.objects.get(id=data.get("id"))
            serializer = EventSerializer(todo_obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(user=user_obj)
                return Response({"status" : 200, "data" : data, "result" : "success"})
            else:
                return Response({"status" : 400, "error" : serializer.errors})
        except Exception as e:
            print(e)
            return Response({"status":500, "message":"something went wrong", "error":e})

@api_view(['PATCH'])
def EventDeleteView(request):
    try:
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        data = request.data
        todo_obj = EventModel.objects.get(id=data.get("id"))
        serializer = EventDeleteSerializer(todo_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"status" : 200, "data" : data, "result" : "success"})
        else:
            return Response({"status" : 400, "error" : serializer.errors})
    except Exception as e:
        print(e)
        return Response({"status":500, "message":"something went wrong", "error":e})


class TodoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            objs = TodoModel.objects.filter(user=self.request.user)
            serializer = TodoSerializer(objs, many=True)
            return Response({"status" : 200, "data" : serializer.data})
        except Exception as e:
            print(e)
            return Response({"status":500, "message":"something went wrong", "error":e})
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return Response({"status" : 200, "result" : "success", "data" : serializer.data})
            else:
                return Response({"status" : 400, "error" : serializer.errors})
        except Exception as e:
            print(e)
            return Response({"status":500, "message":"something went wrong", "error":e})
    def patch(self, request):
        try:
            data = request.data
            todo_obj = TodoModel.objects.get(id=data.get("id"))
            serializer = TodoSerializer(todo_obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return Response({"status" : 200, "data" : data, "result" : "success"})
            else:
                return Response({"status" : 400, "error" : serializer.errors})
        except Exception as e:
            print(e)
            return Response({"status":500, "message":"something went wrong", "error":e})

@api_view(['PATCH'])
def TodoDeleteView(request):
    try:
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        data = request.data
        todo_obj = TodoModel.objects.get(id=data.get("id"))
        serializer = TodoDeleteSerializer(todo_obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"status" : 200, "data" : data, "result" : "success"})
        else:
            return Response({"status" : 400, "error" : serializer.errors})
    except Exception as e:
        print(e)
        return Response({"status":500, "message":"something went wrong", "error":e})



@api_view(["POST"])
def add_members(request, event_id):
    try:
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        data =request.data
        if EventModel.objects.filter(id = event_id):
            user_obj = UserModel.objects.get(email=request.user)
            event_obj = EventModel.objects.get(id = event_id)
            serializer = AddMemberSerializer(data=data)
            if serializer.is_valid():
                invite_obj, _ = UserModel.objects.get_or_create(
                    email = serializer.data["member_email"],
                    name = serializer.data["member_name"]
                )
                event_obj.members.add(invite_obj, user_obj)
                event_obj.save()
                thread_obj = send_invite_email(serializer.data["member_name"], serializer.data["member_email"], event_id)
                thread_obj.start()
    except Exception as e:
        print(e)
        return Response({"status":500, "message":"something went wrong", "error":e})


@api_view(["POST"])
def invite(request, event_id):
    try:
        authentication_classes = [JWTAuthentication]
        permission_classes = [IsAuthenticated]
        data = request.data
        if EventModel.objects.filter(id = event_id):
            user_obj = UserModel.objects.get(email=request.user)
            event_obj = EventModel.objects.get(id = event_id)
            serializer = InviteSerializer(data=data)
            if serializer.is_valid():
                choice = serializer.data["choice"]
                if choice=="yes":
                    event_obj.members.add(user_obj)
                    event_obj.save()
                    thread_obj_1 = invite_accepted(request.user)
                    thread_obj_1.start()
                    thread_obj_2 = invite_accepted(event_obj.user.email)
                    thread_obj_2.start()
                    return Response({"status" : 200, "data" : data, "result" : "invite accepted"})
                elif choice=="no":
                    thread_obj_1 = invite_rejected(request.user)
                    thread_obj_1.start()
                    thread_obj_2 = invite_rejected(event_obj.user.email)
                    thread_obj_2.start()
                    return Response({"status" : 200, "data" : data, "result" : "invite rejected"})
    except Exception as e:
        print(e)
        return Response({"status":500, "message":"something went wrong", "error":e})