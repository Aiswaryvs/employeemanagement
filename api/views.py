from django.shortcuts import render
from rest_framework.views import APIView
from api.serializers import EmpModelSerializer,EmpRegSeializer
from rest_framework.response import Response
from rest_framework import status
from employee.models import Employee
from rest_framework import viewsets

# Create your views here.

class EmpCreateView(APIView):
    serializer_class=EmpModelSerializer

    def get(self,requst,*args,**kwargs):
        all_emp=Employee.objects.all()
        serializer=self.serializer_class(all_emp,many=True)
        return Response(data=serializer.data)


    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class EmpDeatailsView(APIView):
    serializer_class=EmpModelSerializer

    def get(self,request,*args,**kwargs):
        eid=kwargs.get("eid")
        try:
            emp=Employee.objects.get(eid=eid)
            serializer=self.serializer_class(emp)
            return Response(data=serializer.data)
        except:
            return Response({"msg":"invalid"},status=status.HTTP_404_NOT_FOUND)


    def delete(self,request,*args,**kwargs):
        eid=kwargs.get("eid")
        try:
            emp=Employee.objects.get(eid=eid)
            emp.delete()
            return Response(data=request.data)
        except:
            return Response({"msg":"invalid"},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,*args,**kwargs):
        eid=kwargs.get("eid")
        emp=Employee.objects.get(eid=eid)
        serializer=self.serializer_class(data=request.data,instance=emp)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class EmpSignupView(APIView):
    serializer_class=EmpRegSeializer

    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class EmpViewsetView(viewsets.ViewSet):
    serializer_class=EmpModelSerializer
    def list(self,request,*args,**kwargs):
        emp=Employee.objects.all()
        if "designation" in request.query_params:
            designation=request.query_params.get("designation")
            emp=Employee.objects.filter(designation=designation)
        if "salary_lte" in request.query_params:
            salary=request.query_params.get("salary_lte")
            emp=Employee.objects.filter(salary__lte=salary)
        serializer=EmpModelSerializer(emp,many=True)
        return Response(data=serializer.data)




    def create(self,request,*args,**kwargs):
        serializer=EmpModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        eid=kwargs.get("pk")
        emp=Employee.objects.get(eid=eid)
        serializer=EmpModelSerializer(emp)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        eid=kwargs.get("pk")
        instance=Employee.objects.get(eid=eid)
        serializer=EmpModelSerializer(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        eid = kwargs.get("pk")
        emp=Employee.objects.get(eid=eid)
        emp.delete()
        return Response({"msg":"Profile has been removed"})

