from django.urls import path

from apps.users.views import UserCreateAPIView

urlpatterns = [
    path('signup', UserCreateAPIView.as_view())

]
