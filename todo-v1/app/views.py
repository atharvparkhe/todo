from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TodoSerializer
from .models import *

class TodoLC(ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

class TodoRUD(RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"