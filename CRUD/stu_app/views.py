from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# List View
class StudentListView(LoginRequiredMixin, ListView):
    login_url = "login_url"
    model = Student

# Create View
class StudentCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login_url'
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('stu_list')


# Update View
class StudentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "login_url"
    model = Student
    fields = "__all__"
    template_name_suffix = 'stu_update'
    success_url = reverse_lazy('stu_list')

#Delete View
class StudentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "login_url"
    model = Student
    success_url = reverse_lazy("stu_list")

