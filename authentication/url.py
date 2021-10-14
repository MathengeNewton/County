from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('registraion/', views.register_user_info, name="register_info"),
    path('register-constituency/', views.register_constituency, name="register_constituency"),
    path('home/', views.dashboard_home, name="home"),
    path('logout/',views.member_logout,name="logout")
]
