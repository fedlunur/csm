from rest_framework import generics
from .models import *
from .serializers import *

class StructureListCreateView(generics.ListCreateAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer

class StructureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer

class PullListCreateView(generics.ListCreateAPIView):
    queryset = Pull.objects.all()
    serializer_class = PullSerializer

class PullDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pull.objects.all()
    serializer_class = PullSerializer
class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class ZoneListCreateView(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class ZoneRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class WeredaListCreateView(generics.ListCreateAPIView):
    queryset = Wereda.objects.all()
    serializer_class = WeredaSerializer

class WeredaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wereda.objects.all()
    serializer_class = WeredaSerializer