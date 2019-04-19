
from django.urls import path
from . import views

details_user = views.Userview.as_view({

    'put':'update',
    'delete':'destroy'


})


education = views.EducationView.as_view({

    'post':'create',
    'put':'update',
    'delete':'destroy'




})

profile_details = views.ProfileView.as_view({

    'put':'update'

})

urlpatterns = [ path('users', views.listUsers,name ='getUser'),
                path('users/',views.createUser,name= "createuser"),
                path('users/<int:pk>/profile',profile_details,name='update_profile'),
                path('login/',views.log_in,name="login user"),
                path('logout/', views.log_out, name="logout user"),
                path('users/<int:pk>/',details_user,name="delete,update user"),
                path('users/<int:pk>/education/',education,name='add_education'),
                path('users/<int:pk>/education/<int:pk2>/',education,name="update_educauion")

                ]

