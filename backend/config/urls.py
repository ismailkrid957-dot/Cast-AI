
from django.contrib import admin
from django.urls import path, include
from .views import test_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/test/", test_api),
    path("api/", include("casting.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
