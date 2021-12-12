from django.urls import path, include
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]

