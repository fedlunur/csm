from django.urls import path
from .views import *

urlpatterns = [
    path('structures/', StructureListCreateView.as_view(), name='structure-list-create'),
    path('structures/<int:pk>/', StructureDetailView.as_view(), name='structure-detail'),
    path('pulls/', PullListCreateView.as_view(), name='pull-list-create'),
    path('pulls/<int:pk>/', PullDetailView.as_view(), name='pull-detail'),
     path('regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('regions/<int:pk>/', RegionRetrieveUpdateDestroyView.as_view(), name='region-detail'),
    path('zones/', ZoneListCreateView.as_view(), name='zone-list-create'),
    path('zones/<int:pk>/', ZoneRetrieveUpdateDestroyView.as_view(), name='zone-detail'),
    path('weredas/', WeredaListCreateView.as_view(), name='wereda-list-create'),
    path('weredas/<int:pk>/', WeredaRetrieveUpdateDestroyView.as_view(), name='wereda-detail'),
]