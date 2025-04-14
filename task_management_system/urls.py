"""
URL configuration for task_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tms.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # Uncomment the above line to enable the browsable API authentication
    # path('api-auth/', include('rest_framework.authtoken.urls')),
    # Uncomment the above line to enable token authentication
    # path('api-auth/', include('rest_framework_jwt.urls')),
    # Uncomment the above line to enable JWT authentication
    # path('api-auth/', include('rest_framework_simplejwt.urls')),
    # Uncomment the above line to enable Simple JWT authentication
    # path('api-auth/', include('rest_framework_social_oauth2.urls')),
    # Uncomment the above line to enable social authentication
    # path('api-auth/', include('rest_framework_social_auth.urls')),
    # Uncomment the above line to enable social authentication
    # path('api-auth/', include('rest_framework_oauth.urls')),
    # Uncomment the above line to enable OAuth authentication
]
