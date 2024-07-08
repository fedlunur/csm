from rest_framework import serializers
from .models import *

class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ['id', 'structureName', 'date_registered']

class PullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pull
        fields = ['id', 'pullName', 'date_registered']
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

class WeredaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wereda
        fields = '__all__'