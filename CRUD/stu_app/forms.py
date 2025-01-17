from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            'roll_no' : "ROLL NO",
            'first_name' : "FIRST NAME",
            'last_name' :  "LAST NAME",
            'email' : "EMAIL",
            'age' : "AGE",
            'enrollment_date' : "ENROLLMENT DATA"
        }
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date','abcd':"mno"}),
        }