from django.urls import path
from employee import views

urlpatterns = [
    # path('index',views.index),
    # path('index',views.IndexView.as_view()),
    #
    # path('signup',views.RegView.as_view(),name="emp-reg"),

    path('add',views.EmployeeCreateView.as_view(),name="emp-add"),
    path('all',views.EmployeeListView.as_view(),name="emp-list"),
    path('details/<str:emp_id>',views.EmployeeDetailsView.as_view(),name="emp-detail"),
    path('change/<str:e_id>',views.EmployeeEditView.as_view(),name="emp-edit"),
    path('remove/<str:eid>',views.remove_employee,name="emp-delt"),
    path('',views.index,name="index"),
    path('accounts/signup',views.SignUpView.as_view(),name="signup"),
    path('accounts/signin',views.LoginView.as_view(),name="signin"),
    path('accounts/signout',views.sign_out,name="signout")
]