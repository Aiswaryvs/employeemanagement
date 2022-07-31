from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.views.generic import View
from employee.forms import EmployeeForm,UserRegistrationForm,LoginForm
from django.contrib import messages
from employee.models import Employee
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator




# Create your views here.

# function based view
# class based view

# def index(request):
#     return render(request,"home.html")
# def login(request):
#     return render(request,"lg.html")
# def registration(request):
#     return HttpResponse("<h1> Signup </h1>")


# class IndexView(View):
#     def get(self,request):
#         return render(request,"home.html")
# class LoginView(View):
#     form_class=LoginForm
#     template_name="lg.html"
#     def get(self,request):
#         form=LoginForm()
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data.get("email"))
#             print(form.cleaned_data.get("password"))
#             # print(request.POST.get("email"))
#             # print(request.POST.get("password"))
#             # return render(request,self.template_name,{"form":form})
#             return redirect("emp-login")
#         else:
#             messages.error(request, "profile adding failed")
#             return render(request, self.template_name, {"form": form})


# class RegView(View):
#     form_class = RegisterForm
#     template_name = "reg.html"
#     def get(self,request):
#         form=RegisterForm()
#         return render(request,"reg.html",{"form":form})
#     def post(self,request):
#         form=RegisterForm(request.POST)
#         if form.is_valid():
#             print(request.POST.get("fname"))
#             print(request.POST.get("lname"))
#             print(request.POST.get("email"))
#             print(request.POST.get("uname"))
#             print(request.POST.get("password"))
#             # return render(request,"reg.html",{"form":form})
#             return redirect("emp-login")
# class EmployeeCreateView(View):
#     form_class=EmployeeForm
#     template_name="emp-add.html"
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         form=self.form_class(request.POST)
#         print("values in request.POSt")
#         print(request.POST)
#         if form.is_valid():
#             print("cleaned_data")
#             print(form.cleaned_data)
#             print(form.cleaned_data.get("eid"))
#             print(form.cleaned_data.get("employee_name"))
#             print(form.cleaned_data.get("designation"))
#             print(form.cleaned_data.get("salary"))
#             # return render(request,self.template_name,{"form":form})
#             messages.success(request,"profile has been saved")
#             return redirect("emp-add")
#         else:
#             messages.error(request,"profile adding failed")
#             return render(request,self.template_name,{"form":form})

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"user must login")
            return redirect("signin")
    return wrapper



@method_decorator(signin_required,name="dispatch")
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeForm()
        return render(request,"emp-nadd.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeeForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # Employee.objects.create(
            #     eid=form.cleaned_data.get("eid"),
            #     employee_name=form.cleaned_data.get("employee_name"),
            #     designation=form.cleaned_data.get("designation"),
            #     email=form.cleaned_data.get("email"),
            #     salary=form.cleaned_data.get("salary"),
            #     experience=form.cleaned_data.get("experience")
            # )
            messages.success(request,"profile has been added")
            return redirect("emp-add")
        else:
            messages.error(request, "profile adding failed")
            return render(request,"emp-nadd.html",{"form":form})


@method_decorator(signin_required,name="dispatch")
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"emp-list.html",{"employees":qs})

@method_decorator(signin_required,name="dispatch")
class EmployeeDetailsView(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        qs=Employee.objects.get(eid=kwargs.get("emp_id"))
        return render(request,"emp-detail.html",{"employee":qs})


@method_decorator(signin_required,name="dispatch")
class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("e_id")
        employee=Employee.objects.get(eid=eid)
        form=EmployeeForm(instance=employee)
        return render(request,"emp-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        eid = kwargs.get("e_id")
        employee = Employee.objects.get(eid=eid)
        form = EmployeeForm(request.POST,instance=employee,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "profile has been updated")
            return redirect("emp-add")
        else:
            messages.error(request, "profile updating failed")
            return render(request, "emp-nadd.html", {"form": form})

@signin_required
def remove_employee(request,*args,**kwargs):
    eid = kwargs.get("eid")
    employee = Employee.objects.get(eid=eid)
    form = EmployeeForm(instance=employee)
    employee.delete()
    messages.success(request,"profile has been removed")
    return redirect("emp-list")

def index(request):
    return render(request,"base.html")

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"registration is successful")
            return redirect("signin")
        else:
            messages.error(request, "registration failed")
            return render(request, "registration.html",{"form": form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"lg.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("success")
                return redirect("emp-list")
            else:
                messages.error(request,"Invalid Credentials")
                return render(request,"lg.html",{"form":form})

@signin_required
def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")




