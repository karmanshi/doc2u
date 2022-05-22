from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('addDetails/', views.addDetails),

]
