
from django.urls import path
from . import views

update_user = views.Updateview.as_view({

    'put':'update'


})


education = views.EducationView.as_view({

    'post':'create',
    'put':'update'




})

urlpatterns = [ path('users', views.listUsers,name ='getUser'),
                path('users/',views.createUser,name= "createuser"),
                path('login/',views.log_in,name="login user"),
                path('logout/', views.log_out, name="logout user"),
                path('users/<int:pk>/',update_user,name="update user"),
                path('users/<int:pk>/education/',education,name='add_education'),
                path('users/<int:pk>/education/<int:pk2>/',education,name="update_educauion")

                ]

