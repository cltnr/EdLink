from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("stats/<str:link_user>", views.link_infos, name="link_infos"),
    path("<str:link_user>+", views.link_infos, name="link_infos"),
    path("<str:link_user>", views.link_redirect, name="link_redirect")
]
