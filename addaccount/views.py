from django.shortcuts import render,redirect
from seekaccount import views
from .models import accounts
# Create your views here.
def adc(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        dob = request.POST.get('dob') 
        email = request.POST.get('email') 
        passwod = request.POST.get('passwod') 
        post = request.POST.get('post') 
        data = accounts(name=name,email=email,passwod=passwod,dob=dob,post=post)
        data.save()
    
    return render(request,'adc.html')