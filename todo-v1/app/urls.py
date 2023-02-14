from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('todo/', views.TodoLC.as_view(), name="TodoLC"),
    path('todo/<id>/', views.TodoRUD.as_view(), name="TodoRUD"),
]