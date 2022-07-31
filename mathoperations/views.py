from django.shortcuts import render
from django.views.generic import View
from mathoperations.forms import MathForm,FactForm,EmpForm

# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,"math-home.html")
class AddView(View):
    def get(self,request):
        form=MathForm()
        return render(request,"addition.html",{"form":form})
    def post(self,request):
        form=MathForm(request.POST)
        if not form.is_valid():
            return render(request,"addition.html",{"form":form})
        n1=form.cleaned_data.get("n1")
        n2=form.cleaned_data.get("n2")
        result=n1+n2
        print(result)
        return render(request,"addition.html",{"addres":result})
class FactorialView(View):
    def get(self,request):
        form=FactForm()
        return render(request,"factorial.html",{"form":form})
    def post(self,request):
        form=FactForm(request.POST)
        if not form.is_valid():
            return render(request,"factorial.html",{"form":form})
        n1=form.cleaned_data.get("n1")
        f=1
        while int(n1)>0:
            f=int(f)*int(n1)
            n1=int(n1)-1
        print(f)
        return render(request,"factorial.html",{"factres":f})
class MulView(View):
    def get(self,request):
        form=MathForm()
        return render(request,"multiplication.html",{"form":form})
    def post(self,request):
        form=MathForm(request.POST)
        if not form.is_valid():
            return render(request,"multiplication.html",{"form":form})
        n1=form.cleaned_data.get("n1")
        n2=form.cleaned_data.get("n2")
        result=int(n1)*int(n2)
        return render(request,"multiplication.html",{"mulres":result})
class EmpAddView(View):
    form_class=EmpForm
    template_class="math-addemp.html"
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_class,{"form":form})
    def post(self,request):
        form=self.form_class(request.POST)
        if not form.is_valid():
            return render(request,self.template_class,{"form":form})
        print(form.cleaned_data.get("name"))
        print(form.cleaned_data.get("email"))
        print(form.cleaned_data.get("exp"))
        return render(request,self.template_class,{"form":form})
