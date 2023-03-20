from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('application/',views.application,name='application'),
    path('final/',views.final,name='final'),
    path('logout',views.logout,name='logout')

]