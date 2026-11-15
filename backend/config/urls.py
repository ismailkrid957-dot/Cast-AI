from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import test_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/test/", test_api),
    path("api/", include("casting.urls")),
    path("api/", include("applicants.urls")),
    path("api/", include("evaluations.urls")),
    path("api-auth/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
