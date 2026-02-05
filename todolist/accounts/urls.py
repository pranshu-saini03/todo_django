from django.urls import path
from .views import loginview, logoutview, registrationview
urlpatterns = [
    path("login/", loginview.as_view()),
    path("logout/", logoutview.as_view()),
    path("register/", registrationview.as_view()),
]
