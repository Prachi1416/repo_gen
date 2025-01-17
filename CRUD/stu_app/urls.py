from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView , StudentDeleteView

urlpatterns = [
     path('show/', StudentListView.as_view(), name = "stu_list"),
     path('add/', StudentCreateView.as_view(), name = "stu_create"),
     path('update/<pk>/', StudentUpdateView.as_view(), name="stu_update"),
     path('delete/<pk>/', StudentDeleteView.as_view(), name="stu_delete")

]
