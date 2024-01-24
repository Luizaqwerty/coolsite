from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path("women/", include('women.urls')),
]
