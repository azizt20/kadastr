from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('user_info/<int:id>', user_info, name="user_info"),
    path('garden/<int:id>', garden, name="garden"),
    path('kadastr/<int:id>', kadastr, name="kadastr"),
]
