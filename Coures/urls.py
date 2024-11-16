from django.urls import path 
from .views import *
from APP.views import *



urlpatterns = [
    path('home/' ,homepage.as_view()) ,
    path('user/' ,UserLogin.as_view() ),
    # path('user/' , User_Detils.as_view() ),
    path('student/' , Student_details.as_view()), 
    path('coures/' , Coures_details.as_view()),
    # path('studentlist/', Studentd_list.as_view() ),
    path('studentFeed/' ,Students_feedBack.as_view() ),
    path('logout/' , LogOut),
    path('cardAdd/' , Card_add.as_view()),
    # path('studentlist/<int:id>/' , Studentd_list.as_view()),
 
    #   Admin
    
    path('admin/' , AdminLogin.as_view()),
    path('adminlist/' , Admin_List.as_view()),
    path('adminhome/' , AminHome.as_view()),
    path('admincoures/' , ACoures__details.as_view() ),
    path('admincoures/delete/<int:id>/' , Admin_Delete.as_view() , name="del"),
    path('adminData/delete/<int:id>/' , Admin_data_delete.as_view() , name="delete"),
    path('admincoures/update/<int:id>/' , Admin_update.as_view() , name="update"),
    path('couresAdd/', CouresForms.as_view() , name = "couresAdd"),

]
