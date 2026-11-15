from django.urls import path, re_path
from .views import index

urlpatterns = [
    path("", index),
    re_path(r"^(?:.*)/?$", index),  # Forwards client-side React Router paths to index.html
]