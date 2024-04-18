from django.shortcuts import render,redirect,get_object_or_404
from addaccount.models import accounts
# Create your views here.
def dla(request):  
    data=accounts.objects.all()
  
    return render(request,'dla.html',{'data':data})

def dlac(request):
    if request.method == "POST":
        name = request.POST.getlist("userid") 
        for i in name:
            da = accounts.objects.get(id=i)
            da.delete()
    return redirect('dla')     
