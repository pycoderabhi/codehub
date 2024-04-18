from django.shortcuts import render,redirect
from addaccount.models import accounts

# Create your views here.
def ska(request):

    data = accounts.objects.all()
    
    return render(request,'ska.html',{'data':data})