from django import forms
from employee.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class LoginForm(forms.Form):
#     email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter email"}))
#     password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         email=cleaned_data.get("email")
#         password=cleaned_data.get("password")
# class RegisterForm(forms.Form):
#     fname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Firstname"}))
#     lname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Lastname"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter email"}))
#     uname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username"}))
#     password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
#
#
# class EmployeeForm(forms.Form):
#     eid=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter employee id"}))
#     employee_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter employee name" }))
#     designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter employee designation"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter email"}))
#     salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter salary"}))
#     experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter experience"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         exp=cleaned_data.get("experience")
#         if int(exp)<0:
#             msg="Invalid Experience"
#             self.add_error("experience",msg)
#
#

# class EmployeeForm(forms.Form):
#     eid=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     employee_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
#     salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

        widgets={
            "eid":forms.TextInput(attrs={"class":"form-control"}),
            "employee_name":forms.TextInput(attrs={"class":"form-control"}),
            "designation":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "experience":forms.NumberInput(attrs={"class": "form-control"}),
        }
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2"
        ]
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))