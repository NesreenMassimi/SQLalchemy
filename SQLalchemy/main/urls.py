
from django.urls import path
from . import views

urlpatterns = [ path('users', views.listUsers,name ='getUser'),
                path('users/',views.createUser,name= "createuser"),
                path('login/',views.login,name="login user")

                ]

