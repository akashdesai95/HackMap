from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('authenticate/', auth_user, name='authenticate'),
    path('login/', login, name='login'),
]