from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root.settings import MEDIA_URL, MEDIA_ROOT
from root.swagger import swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.insta_clone.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.shared.urls')),


] + swagger_urls + static(MEDIA_URL, document_root=MEDIA_ROOT)
