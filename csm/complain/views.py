# views.py
from rest_framework import generics
from .models import *
from .serializers import *

class ComplainListCreateView(generics.ListCreateAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer

class ComplainRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class ResultListCreateView(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class ResultRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer    

class ComplainFeedbackListCreateView(generics.ListCreateAPIView):
    queryset = ComplainFeedback.objects.all()
    serializer_class = ComplainFeedbackSerializer

class ComplainFeedbackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComplainFeedback.objects.all()
    serializer_class = ComplainFeedbackSerializer   
     
class FilesAttachedListCreateView(generics.ListCreateAPIView):
    queryset = FilesAttached.objects.all()
    serializer_class = FilesAttachedSerializer

class FilesAttachedRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FilesAttached.objects.all()
    serializer_class = FilesAttachedSerializer    