"""
URL configuration for csm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

from structure.views import *;
from appointment.views import *;
from structure.views import *;
from complain.views import *;
from department.views import *;
urlpatterns = [
    path('admin/', admin.site.urls),
 # this is for Structure app 
    path('api/structures/', StructureListCreateView.as_view(), name='structure-list-create'),
    path('api/structures/<int:pk>/', StructureDetailView.as_view(), name='structure-detail'),
    path('api/pulls/', PullListCreateView.as_view(), name='pull-list-create'),
    path('api/pulls/<int:pk>/', PullDetailView.as_view(), name='pull-detail'),
    path('api/regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('api/regions/<int:pk>/', RegionRetrieveUpdateDestroyView.as_view(), name='region-detail'),
    path('api/zones/', ZoneListCreateView.as_view(), name='zone-list-create'),
    path('api/zones/<int:pk>/', ZoneRetrieveUpdateDestroyView.as_view(), name='zone-detail'),
    path('api/weredas/', WeredaListCreateView.as_view(), name='wereda-list-create'),
    path('api/weredas/<int:pk>/', WeredaRetrieveUpdateDestroyView.as_view(), name='wereda-detail'),
# this is for Appointments app 
    path('api/appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('api/appointments/<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail'),
    path('api/employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
# this is for complain
    path('complains/', ComplainListCreateView.as_view(), name='complain-list-create'),
    path('api/complains/<int:pk>/', ComplainRetrieveUpdateDestroyView.as_view(), name='complain-detail'),
    path('api/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
    path('api/results/', ResultListCreateView.as_view(), name='result-list-create'),
    path('api/results/<int:pk>/', ResultRetrieveUpdateDestroyView.as_view(), name='result-detail'),
    path('api/complain_feedbacks/', ComplainFeedbackListCreateView.as_view(), name='complain_feedback-list-create'),
    path('api/complain_feedbacks/<int:pk>/', ComplainFeedbackRetrieveUpdateDestroyView.as_view(), name='complain_feedback-detail'),
    path('api/files_attached/', FilesAttachedListCreateView.as_view(), name='files_attached-list-create'),
    path('api/files_attached/<int:pk>/', FilesAttachedRetrieveUpdateDestroyView.as_view(), name='files_attached-detail'),
    # for departments 
    path('api/positions/', PositionListCreateView.as_view(), name='position-list-create'),
    path('api/positions/<int:pk>/', PositionRetrieveUpdateDestroyView.as_view(), name='position-detail'),
    path('api/departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('api/departments/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),
    path('api/services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('api/services/<int:pk>/', ServiceRetrieveUpdateDestroyView.as_view(), name='service-detail'),
   
]
