from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from {{cookiecutter.project_slug}}.app.models.{{cookiecutter.model_name}} import {{cookiecutter.model_name|title}}
from {{cookiecutter.project_slug}}.app.serializers.{{cookiecutter.model_name}} import {{cookiecutter.model_name|title}}Serializer


class {{cookiecutter.model_name|title}}ListCreateAPIView(APIView, LimitOffsetPagination):
    def get(self, request):
        {{cookiecutter.model_name}}s_qs = {{cookiecutter.model_name|title}}.objects.all()
        page = self.paginate_queryset({{cookiecutter.model_name}}s_qs, request, view=self)
        if page is not None:
            serializer = {{cookiecutter.model_name|title}}Serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # Return all the items
        serializer = {{cookiecutter.model_name|title}}Serializer({{cookiecutter.model_name}}s_qs, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = {{cookiecutter.model_name|title}}Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class {{cookiecutter.model_name|title}}RetrieveUpdateDeleteAPIView(APIView):
    @staticmethod
    def get(request, pk):
        {{cookiecutter.model_name}} = get_object_or_404({{cookiecutter.model_name|title}}, pk=pk)
        serializer = {{cookiecutter.model_name|title}}Serializer({{cookiecutter.model_name}})
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        {{cookiecutter.model_name}} = get_object_or_404({{cookiecutter.model_name|title}}, pk=pk)
        serializer = {{cookiecutter.model_name|title}}Serializer({{cookiecutter.model_name}}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        {{cookiecutter.model_name}} = get_object_or_404({{cookiecutter.model_name|title}}, pk=pk)
        {{cookiecutter.model_name}}.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
