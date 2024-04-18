from django.shortcuts import render,redirect
from addaccount.models import accounts
from home import views
# Create your views here.

def upa(request):
   
    if request.method == 'POST':
     
        listdata = request.POST.getlist('userid')
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        post = request.GET.get('post')
        dob = request.GET.get('dob')
        passwod = request.GET.get('passwod')
        accounts.objects.update(name = name, email=email, post=post, dob=dob,passwod=passwod)
        data = accounts.objects.filter(name = name).all()
      
        return render(request,'upa.html',{'data':data})
    for i in listdata:
        data =accounts.objects.filter(name = i).all()
    return render(request,'upa.html',{'data':data})