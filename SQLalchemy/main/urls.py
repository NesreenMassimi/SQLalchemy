
from django.urls import path
from . import views

update_user = views.Updateview.as_view({

    'put':'update'


})

urlpatterns = [ path('users', views.listUsers,name ='getUser'),
                path('users/',views.createUser,name= "createuser"),
                path('login/',views.log_in,name="login user"),
                path('logout/', views.log_out, name="logout user"),
                path('users/<int:pk>/',update_user,name="update user")

                ]

