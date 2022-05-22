from django.shortcuts import redirect, render
from accounts.models import otherDetails
from .models import pickup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User





# usrdbd starts============================================================================================
"""
for user dashboard
This function will render the dashboard whenever a user loggs in.
for 'User' this function will send information and the ui will render different menus according to the status of user.
"""
@login_required(login_url='/accounts/login/')
def usrdbd(request):
    if request.user.otherdetails.status=="Delivery":
        return redirect('/dlvrydbd/')
    else:
        latestPickUps=pickup.objects.filter(pickupRequestByUserId=request.user.id,status=0)
        return render(request, 'usrdashboard.html',{'latestPickUps':latestPickUps})

# usrdbd ends============================================================================================



# dlvrydbd starts============================================================================================
"""
for user dashboard
for 'User' this function will send information and the ui will render different menus according to the status of user.
"""
@login_required(login_url='/accounts/login/')
def dlvrydbd(request):
    if request.user.otherdetails.status=="User":
        return redirect('/usrdbd/')
    else:
        latestPickUps=pickup.objects.filter(pickupDeliveryPersonId=0)
        if request.method=='POST':
            latestPickUps=pickup.objects.filter(pickupDeliveryPersonId=request.user.id)
            pickup.save()
            return redirect('/dlvrydbd/')
        else:
            return render(request,'dlvrydashboard.html',{'latestPickUps':latestPickUps})

# dlvrydbd ends============================================================================================









# dlvryhistory starts============================================================================================
"""
for checking the history of pickup requested/delivered
can be used by user and delivery person
"""
@login_required(login_url='/accounts/login/')
def dlvryhistory(request):
    id=request.user.id
    ot=otherDetails.objects.get(user=id)
    if ot.status=='Delivery':
        # this is for delivery Persons
        history=pickup.objects.filter(pickupDeliveryPersonId=request.user.id)
        return render(request, 'history.html', {'history':history})
    else:
        # this one is for the person who requested pickup
        history = pickup.objects.filter(pickupRequestByUserId=request.user.id)
        return render(request, 'history.html', {'history':history})

# dlvryhistory starts============================================================================================
