from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('api/todo/', views.TodoView.as_view()),
    path('api/todo/delete/', views.TodoDeleteView),
    path('api/event/', views.EventView.as_view()),
    path('api/event/delete/', views.EventDeleteView),
    path('api/add-members/<event_id>/', views.add_members),
    path('api/invite/<event_id>/', views.invite),
]