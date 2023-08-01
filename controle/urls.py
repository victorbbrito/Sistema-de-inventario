from django.urls import path, include
from .views import *


urlpatterns = [
    path('',homepage),
    path('contato/', contatos_page),
    path('login/', login_page),
    path('users/', homeusers),
]