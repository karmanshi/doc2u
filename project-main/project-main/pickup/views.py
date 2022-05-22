from django.shortcuts import redirect, render
from accounts.models import otherDetails
from .models import pickup, contact_us
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.



# home starts============================================================================================
"""This is redirect to the home page when logged out and to the dashboard when user is logged in"""
def home(request):
    if request.user.is_authenticated==True:
        user=request.user
        if user.otherdetails.status=="User":
            return redirect("/usrdbd")
        else:
            return redirect("/dlvrydbd")

    else:
        return render(request, 'home.html')

# home starts============================================================================================



# contact_us starts============================================================================================
"""This will redirect user to the contact_us page it doesnt matter weater the user is logged in or not"""
def contact(request):
    if request.method=="POST":
        senderName=request.POST["sender"]
        senderEmail=request.POST["email"]
        message=request.POST["message"]
        newMessage=contact_us.objects.create(senderName=senderName, senderEmail=senderEmail, message=message)
        newMessage.save()
        return redirect('/contact')
    else:
        return render(request,"contact_us.html")
            
# contact_us starts============================================================================================


# about_us starts============================================================================================
"""Redirects to About us page/Section and here also its not nedded for user to log in"""
def about_us(request):
    return render(request,"about_us.html")

# about_us ends============================================================================================