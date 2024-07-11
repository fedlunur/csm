from django.http import Http404
from django.db.models import Q
from rest_framework import generics, serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .utils import import_all_models

# Fetch all models from utils.py
models = import_all_models()
print("All models:", models)

class GenericPagination(PageNumberPagination):
    page_size_query_param = 'items'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })

class GenericListAPIView(generics.ListAPIView):
    pagination_class = GenericPagination

    def get_queryset(self):
        model_name = self.kwargs['model_name']
        model = self.get_model(model_name)
        queryset = model.objects.all()

        query_params = self.request.query_params
        search_query = query_params.get('q', '')
        fields = query_params.get('fields', '')

        if search_query and fields:
            fields = fields.split(',')
            queries = Q()
            for field in fields:
                queries |= Q(**{f"{field}__icontains": search_query})
            queryset = queryset.filter(queries)

        return queryset

    def get_serializer_class(self):
        model_name = self.kwargs['model_name']
        fetchedmodel = self.get_model(model_name)
        return self.get_serializer_for_model(fetchedmodel)

    def get_model(self, model_name):
        try:
            # Dynamically get the model from the imported models dictionary
            model_class = models.get(model_name.capitalize())
            if model_class is None:
                raise KeyError
            return model_class
        except KeyError:
            raise Http404("Model not found")

    def get_serializer_for_model(self, fetchedmodel):
        class DynamicSerializer(serializers.ModelSerializer):
            class Meta:
                model = fetchedmodel
                fields = '__all__'
        return DynamicSerializer
