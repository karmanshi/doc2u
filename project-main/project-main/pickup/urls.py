from . import views
from . import pickupFunctions as pF
from . import dashboard as dbd
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('about_us/', views.about_us),
    path('usrdbd/', dbd.usrdbd),
    path('dlvrydbd/', dbd.dlvrydbd),
    path('dlvryhistory/', dbd.dlvryhistory),
    path('addPick/', pF.addPick),
    path('registerPickup/', pF.registerPickup),
    
]
