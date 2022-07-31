from django.urls import path
from mathoperations import views
urlpatterns =[
    path("home",views.HomeView.as_view(),name="math-home"),
    path("add",views.AddView.as_view(),name="math-add"),
    path("fact",views.FactorialView.as_view(),name="math-fact"),
    path("mul",views.MulView.as_view(),name="math-mul"),
    path("emp/addemp",views.EmpAddView.as_view(),name="math-empadd")
    ]