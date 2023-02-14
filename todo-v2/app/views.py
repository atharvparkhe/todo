from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from authentication.models import UserModel
from .models import *

class TodoLC(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TodoModel.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
    def list(self, request, *args, **kwargs):
        try:
            objs = TodoModel.objects.filter(user=UserModel.objects.get(email=request.user.email)).order_by("-created_at")
            serializer = self.serializer_class(objs, many=True)
            return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def create(self, request, *args, **kwargs):
        try:
            authentication_classes = [JWTAuthentication]
            permission_classes = [IsAuthenticated]
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(self):
                serializer.save(user=UserModel.objects.get(email=request.user.email))
                return Response({"message":"Task added", "data":serializer.data}, status=status.HTTP_202_ACCEPTED)
            return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TodoRUD(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"