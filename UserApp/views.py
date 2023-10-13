from django.shortcuts import render,redirect
from django.contrib import messages
from.models import*
from AdminApp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def UserIndex(request):
    data1=LocationTable.objects.all()
    data2=VenueTable.objects.all()
    return render(request,'UserIndex.html',{'data1':data1,'data2':data2})


def About(request):
    return render(request,'About.html')

def BookVenues(request,id):
    data2=VenueTable.objects.filter(id=id)
    data3=Registertable.objects.filter(id=id)    
    return render(request,'BookVenues.html',{'data2':data2,'data3':data3})

def ContactUs(request):    
    return render(request,'ContactUs.html')

def Locations(request):
    data1=LocationTable.objects.all()
    return render(request,'Locations.html',{'data1':data1})

def Login(request):
    return render(request,'Login.html')

def OnecardVenue(request,id):
    data2=VenueTable.objects.filter(id=id)
    return render(request,'OnecardVenue.html',{'data2':data2})

def OneLocation(request,street):
    data2=VenueTable.objects.filter(street=street)
    return render(request,'OneLocation.html',{'data2':data2})
    
def Register(request):
    return render(request,'Register.html')

def Venues(request):
    data2=VenueTable.objects.all()
    return render(request,'Venues.html',{'data2':data2})

def ContactData(request):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    data=Contacttable(name=name,email=email,message=message)
    data.save()
    return redirect('UserIndex')

def RegisterData(request):
    name=request.POST['name']
    email=request.POST['email']
    number=request.POST['number']
    password=request.POST['password']
    data3=Registertable(name=name,email=email,number=number,password=password)
    data3.save()
    return redirect('UserIndex')


def Bookdata(request,id):    
    if request.method=="POST":
        u_id=request.session.get('u_id')
        id=request.POST['Venu_id']
        function=request.POST['function']
        date=request.POST['date'] 
        starttime=request.POST['starttime'] 
        endtime=request.POST['endtime']     
        data=Booktable(u_id=Registertable.objects.get(id=u_id),Venu_id=VenueTable.objects.get(id=id),function=function,date=date,starttime=starttime,endtime=endtime)
        data.save()
        return render(request,'BookVenues.html',{'msgs':"Successfully Booked"})        

def UserLogin(request):
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        if Registertable.objects.filter(name=name,password=password).exists():
           data = Registertable.objects.filter(name=name,password=password).values('email','id','number').first()
           request.session['email_u'] = data['email'] 
           request.session['u_id'] = data['id']
           request.session['u_number'] = data['number'] 
           request.session['username_u'] = name
           request.session['password_u'] = password 
           
           return redirect('UserIndex')          
        else:
            return render(request,'Login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('Login')

def userlogout(request):  
    del request.session['email_u']  
    del request.session['u_id']    
    del request.session['username_u']
    del request.session['password_u']
    return redirect('UserIndex')  

