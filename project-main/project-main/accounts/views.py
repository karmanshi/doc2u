from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import otherDetails

# Create your views here.

# login function
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                if otherDetails.objects.get(user=user.id).status=='User':
                    return redirect('/usrdbd')
                else:
                    return redirect('/dlvrydbd')
            else:
                print("\n\n\n\n\nInvalid credentials")
                return redirect('/')
        else:
            return render(request, 'home.html')


# logout function
def logout(request):
    auth.logout(request)
    return redirect('/')


# register function
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            dob = request.POST['dob']
            gender = request.POST['gender']
            phoneNumber = request.POST['phoneNumber']
            status = request.POST['status']
            
            if password1 == password2:
                if User.objects.filter(username = username).exists():
                    messages.info(request,'Username already taken')
                    return redirect('/')
                elif User.objects.filter(email = email).exists():
                    messages.info(request,'EmailId already taken')
                    return redirect('/')
                else:
                    user=User.objects.create_user(username = username,password = password1,first_name = first_name,last_name = last_name,email = email)
                    user.save()
                    UpdateDetails=otherDetails.objects.create(user=user,dob=dob,gender=gender,phoneNumber=phoneNumber,status=status)
                    UpdateDetails.save()


                    messages.info(request,'User Created')
                    return redirect('/')
            else:
                messages.info(request,"Incorrect Password")
                return redirect('/')
        else:
            return render(request, "home2.html")


@login_required(login_url="/accounts/login/")
def addDetails(request):
    if request.method=="POST":
        user = request.user
        aadharNo = request.POST['aadharNo']
        drivingLicenseNo = request.POST['drivingLicenseNo']
        address = request.POST['address']
        otherDetails.objects.filter(user=user).update(aadharNo=aadharNo,drivingLicenseNo=drivingLicenseNo,address=address)
        
        # UpdateDetails=otherDetails.objects.update(user=user,aadharNo=aadharNo,drivingLicenseNo=drivingLicenseNo,address=address)
        # UpdateDetails.save()

        return redirect('/accounts/addDetails')
    else:
        return render(request,"addDetails.html")