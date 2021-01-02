from django.urls import path,re_path
from app1 import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/<int:pk>',views.login,name='login'),
    path('register/',views.register,name='register'),
    re_path(r'^api/',views.viewuser.as_view(),name='viewuser'),
]

