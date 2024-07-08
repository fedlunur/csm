# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('complains/', ComplainListCreateView.as_view(), name='complain-list-create'),
    path('complains/<int:pk>/', ComplainRetrieveUpdateDestroyView.as_view(), name='complain-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
    path('results/', ResultListCreateView.as_view(), name='result-list-create'),
    path('results/<int:pk>/', ResultRetrieveUpdateDestroyView.as_view(), name='result-detail'),
    path('complain_feedbacks/', ComplainFeedbackListCreateView.as_view(), name='complain_feedback-list-create'),
    path('complain_feedbacks/<int:pk>/', ComplainFeedbackRetrieveUpdateDestroyView.as_view(), name='complain_feedback-detail'),
 
    path('files_attached/', FilesAttachedListCreateView.as_view(), name='files_attached-list-create'),
    path('files_attached/<int:pk>/', FilesAttachedRetrieveUpdateDestroyView.as_view(), name='files_attached-detail'),

]
