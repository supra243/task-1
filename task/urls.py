from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
