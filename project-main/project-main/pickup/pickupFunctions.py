from django.shortcuts import redirect, render
from .models import pickup
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# addPick starts=================================================================================
"""
To add a pickup request by user
When the user adds a pickup this request will be made and the data regarding the pickup will be saved in the database along with that some information regarding the user will also be stick to the product.
"""
@login_required(login_url='/accounts/login/')
def addPick(request):
    if request.method=="POST":
        # when a new pickup is added

        pickupPersonName = request.POST['pickupPersonName']
        pickupAddress = request.POST['pickupAddress']
        pickupPersonNumber = request.POST['pickupPersonNumber']
        deliveryAddress = request.POST['deliveryAddress']
        pickupRequestByUserId = request.user.id
        pickupRequestByUserName = request.user.first_name +" "+ request.user.last_name
        contactNumber = request.user.otherdetails.phoneNumber
        pickupDeliveryPersonId = False
        timeLimit = request.POST['timeLimit']

        # now add pickup object to the pickup table in database
        newPick = pickup.objects.create(pickupAddress=pickupAddress,pickupPersonName=pickupPersonName,pickupPersonNumber=pickupPersonNumber,deliveryAddress=deliveryAddress,pickupRequestByUserId=pickupRequestByUserId,pickupDeliveryPersonId=pickupDeliveryPersonId,timeLimit=timeLimit,pickupRequestByUserName=pickupRequestByUserName,contactNumber=contactNumber)

        newPick.save()

        return redirect('/addPick')
    else:
        return render(request, 'addPick.html')

# addPick ends=================================================================================



# registerPickup starts=================================================================================
"""
For delivery person to accept a pickup
This function is called when the delivery boy will accept a pickup.
This function will register the respective pickup in the name of the delivery person.
"""

@login_required(login_url='/accounts/login/')
def registerPickup(request):
    postId=request.POST['button']
    pickupDeliveryPersonId = request.user.id
    deliveryPersonName = request.user.first_name+" "+request.user.last_name
    deliveryPersonPhNo = request.user.otherdetails.phoneNumber
    deliveryPersonAadharNo = request.user.otherdetails.aadharNo
    pickup.objects.filter(id=postId).update(pickupDeliveryPersonId=pickupDeliveryPersonId,deliveryPersonName=deliveryPersonName,deliveryPersonPhNo=deliveryPersonPhNo,deliveryPersonAadharNo=deliveryPersonAadharNo)
    return redirect('/dlvrydbd/')

# registerPickup ends=================================================================================