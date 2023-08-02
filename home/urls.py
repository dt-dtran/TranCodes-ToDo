from django.urls import path, include
from home.views import home_page, about_page

urlpatterns = [
    path("home/", home_page, name="home_page"),
    path("about/", about_page, name="about_page"),
]
