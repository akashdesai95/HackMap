from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('map/', map_view, name='map'),
    path('authenticate/', auth_user, name='authenticate'),
    path('login/', login, name='login'),
]