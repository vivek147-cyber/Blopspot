from django.urls import path
from .import views


urlpatterns = [
    path("",views.index,name="Blog"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("Logout/",views.Logout,name="Logout"),
    path("Logout/",views.Logout,name="Logout"),
    path("blogdesc/<int:id>",views.blogdesc,name="blogdesc"),
   

   
]

