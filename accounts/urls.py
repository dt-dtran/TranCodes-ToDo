from django.urls import path
from accounts.views import *

urlpatterns = [
    path("login/", user_login, name="login"),
]
