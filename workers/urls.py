"""
URL configuration for workers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# workers/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import user_registration, user_login, ManagerViewSet, WorkerViewSet


router = DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'managers', ManagerViewSet)  # Add the ManagerViewSet to the router


urlpatterns = [
    # Other URL patterns...
    path('/api/v1/', include(router.urls)),
    path('api/v1/register/', user_registration, name='user_registration'),
    path('api/v1/login/', user_login, name='user_login'),
]