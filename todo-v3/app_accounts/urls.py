from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('api/login/', views.APILogIn.as_view(), name="api-login"),
	path('api/signup/', views.APISignUp.as_view(), name="api-signup"),
	path('api/verify/<token>/', views.APIVerify.as_view(), name="api-verify"),
	path('api/forgot/', views.APIForget.as_view(), name="api-forgot"),
	path('api/reset/<token>/', views.APIReset.as_view(), name="api-reset"),
]