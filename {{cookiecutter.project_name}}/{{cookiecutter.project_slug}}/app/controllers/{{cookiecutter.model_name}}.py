from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from {{cookiecutter.project_slug}}.app.models.{{cookiecutter.model_name}} import {{cookiecutter.model_name|title}}
from {{cookiecutter.project_slug}}.app.serializers.{{cookiecutter.model_name}} import {{cookiecutter.model_name|title}}Serializer
from {{cookiecutter.project_slug}}.app.utils.pagination import CustomLimitOffsetPagination
from {{cookiecutter.project_slug}}.app.utils.responses import StandardResponse


class {{cookiecutter.model_name|title}}ListCreateAPIView(APIView, CustomLimitOffsetPagination):
    def get(self, request):
        {{cookiecutter.model_name}}s_qs = {{cookiecutter.model_name|title}}.objects.all()
        page = self.paginate_queryset({{cookiecutter.model_name}}s_qs, request, view=self)
        if page is not None:
            serializer = {{cookiecutter.model_name|title}}Serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # Return all the items
        serializer = {{cookiecutter.model_name|title}}Serializer({{cookiecutter.model_name}}s_qs, many=True)
        return StandardResponse(serializer.data)

    @staticmethod
    def post(request):
        serializer = {{cookiecutter.model_name|title}}Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return StandardResponse(serializer.data, status=status.HTTP_201_CREATED)
        return ValidationError(serializer.errors)


class {{cookiecutter.model_name|title}}RetrieveUpdateDeleteAPIView(APIView):
    @staticmethod
    def get(request, pk):
        {{cookiecutter.model_name}} = get_object_or_404({{cookiecutter.model_name|title}}, pk=pk)
        serializer = {{cookiecutter.model_name|title}}Serializer({{cookiecutter.model_name}})
        return StandardResponse(serializer.data)

    @staticmethod
    def put(request, pk):
        {{cookiecutter.model_name}} = get_object_or_404({{cookiecutter.model_name|title}}, pk=pk)
        serializer = {{cookiecutter.model_name|title}}Serializer({{cookiecutter.model_name}}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return StandardResponse(serializer.data)
        return ValidationError(serializer.errors)

    @staticmethod
    def delete(request, pk):
        {{cookiecutter.model_name}} = get_object_or_404({{cookiecutter.model_name|title}}, pk=pk)
        {{cookiecutter.model_name}}.delete()
        return StandardResponse(status=status.HTTP_204_NO_CONTENT)
