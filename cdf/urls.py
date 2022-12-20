from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("atas/", include("atas.urls")),
    path("admin/", admin.site.urls),
]
