"""
URL configuration for apps project.

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
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from {{cookiecutter.project_slug}}.app.controllers import {{cookiecutter.model_name}} as {{cookiecutter.model_name}}_views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    # Custom views
    path("api/v1.0/{{cookiecutter.model_name_plural}}/", {{cookiecutter.model_name}}_views.{{cookiecutter.model_name|title}}ListCreateAPIView.as_view(), name="{{cookiecutter.model_name_plural}}"),
    path("api/v1.0/{{cookiecutter.model_name_plural}}/<int:pk>", {{cookiecutter.model_name}}_views.{{cookiecutter.model_name|title}}RetrieveUpdateDeleteAPIView.as_view(), name="{{cookiecutter.model_name}}"),
    # OpenAPI - Swagger
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
