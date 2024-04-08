from email.mime import base

from django.urls import path
from rest_framework.routers import SimpleRouter

from core.auth.views import ChangePasswordView
from core.auth.viewsets import (LoginViewSet, RefreshViewSet,
                                RegistrationViewSet)
from core.user.viewsets import UserViewSet
from walk_a_dog_app.viewsets import *

routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

# APP
routes.register(r'dog', DogViewSet, basename='dog')
routes.register(r'slot', SlotViewSet, basename='slot')
routes.register(r'walk', WalkViewSet, basename='walk')
routes.register(r'clientopinion', ClientOpinionViewSet, basename='clientopinion')
routes.register(r'traineropinion', TrainerOpinionViewSet, basename='traineropinion')


urlpatterns = [
    *routes.urls,
    path('auth/password', ChangePasswordView.as_view())
]