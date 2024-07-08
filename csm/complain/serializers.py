from rest_framework import serializers
from .models import *

class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'        

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class ComplainFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplainFeedback
        fields = '__all__'        

class FilesAttachedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesAttached
        fields = '__all__'        