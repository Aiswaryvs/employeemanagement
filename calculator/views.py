from django.shortcuts import render
from django.views.generic import View
from calculator.forms import OperationForm
# Create your views here.


class HomeView(View):
    def get(self,request):
        return render(request,"calc-home.html")
class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)+int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1+n2
            print(form.cleaned_data)
            return render(request,"add.html",{"res":result,"form":form})
        else:
            return render(request,"add.html",{"form":form})
class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"sub.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)-int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"sub.html",{"form":form})
        n1=form.cleaned_data.get("num1")
        n2=form.cleaned_data.get("num2")
        result=n1-n2
        return render(request,"sub.html",{"subres":result})
class MulView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"mult.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)*int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"mult.html",{"form":form})
        n1=form.cleaned_data.get("num1")
        n2=form.cleaned_data.get("num2")
        result=n1*n2
        return render(request,"mult.html",{"mulres":result})
class DivView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"div.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)/int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"div.html",{"form":form})
        n1=form.cleaned_data.get("num1")
        n2=form.cleaned_data.get("num2")
        result=n1/n2
        return render(request,"div.html",{"divres":result})
class ExpView(View):
    def get(self,request):
        return render(request,"expo.html")
    def post(self,request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)**int(n2)
        print(result)
        return render(request,"expo.html",{"exres":result})
class FlrView(View):
    def get(self,request):
        return render(request,"floor.html")
    def post(self,request):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)//int(n2)
        print(result)
        return render(request,"floor.html",{"flres":result})
class FactView(View):
    def get(self,request):
        return render(request,"fact.html")
    def post(self,request):
        n1=request.POST.get("num1")
        f=1
        while int(n1)>0:
            f=int(f)*int(n1)
            n1=int(n1)-1
        return render(request,"fact.html",{"fctres":f})
class WordCountView(View):
    def get(self,request):
        return render(request,"wordcount.html")
    def post(self,request):
        word=request.POST.get("word")
        words=word.split(" ")
        wc={}
        for w in words:
            if w not in wc:
                wc[w]=1
            else:
                wc[w]+=1
        print(wc)
        return render(request,"wordcount.html",{"wordres":wc})
class PrimeView(View):
    def get(self,request):
        return render(request,"prime.html")
    def post(self,request):
        l=[]
        n1 = request.POST.get("num1")
        n2 = request.POST.get("num2")
        n1=int(n1)
        n2=int(n2)
        for num in range(n1, n2):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                l.append(num)

        print(l)
        return render(request,"prime.html",{"primeres":l})

