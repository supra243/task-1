from django.contrib import admin
from rest_framework import routers
from django.urls import path, include

from api.views import ProfileView

#router = routers.SimpleRouter()

#router.register('profile', ProfileViewset, basename="profile")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("profile/<int:pk>", ProfileView.as_view()),
    #path('api/', include(router.urls)),
]
