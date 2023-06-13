from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from apps.users.models import User
from apps.users.serializers import SignUpSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignUpSerializer
