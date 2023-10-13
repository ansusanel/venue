from django.shortcuts import render,redirect
from.models import*
from UserApp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def AdminIndex(request):
    location=LocationTable.objects.all().count()
    venue=VenueTable.objects.all().count()
    manager=ManagerTable.objects.all().count()
    bookings=Booktable.objects.all().count()
    user=Registertable.objects.all().count()
    feedback=Contacttable.objects.all().count()
    return render(request,'AdminIndex.html',{'location':location,'venue':venue,'manager':manager,'bookings':bookings,'user':user,'feedback':feedback})

def AddLocation(request):    
    return render(request,'AddLocation.html')

def AddManager(request):
    data2=VenueTable.objects.all()
    return render(request,'AddManager.html',{'data2':data2})

def AddVenue(request):
    data1=LocationTable.objects.all()
    return render(request,'AddVenue.html',{'data1':data1})

def Bookings(request):    
    data=Booktable.objects.all()
    return render(request,'Bookings.html',{'data':data})

def Feedbacks(request):
    data3=Contacttable.objects.all()
    return render(request,'Feedbacks.html',{'data3':data3})

def RegisteredUsers(request):
    data4=Registertable.objects.all()
    return render(request,'RegisteredUsers.html',{'data4':data4})

def ViewManageLocations(request):
    data1=LocationTable.objects.all()
    return render(request,'ViewManageLocations.html',{'data1':data1})

def ViewManageManager(request):
    data=ManagerTable.objects.all()
    return render(request,'ViewManageManager.html',{'data':data})

def ViewManageVenues(request):
    data2=VenueTable.objects.all()
    return render(request,'ViewManageVenues.html',{'data2':data2})

def LocationData(request):
    if(request.method=='POST'):
        street=request.POST['street']
        city=request.POST['city']
        district=request.POST['district']
        image=request.FILES['image']
        state=request.POST['state']
        data=LocationTable(street=street,city=city,district=district,image=image,state=state)
        data.save()
        return redirect('ViewManageLocations')


def EditLocation(request):
    data1=LocationTable.objects.all()
    return render(request,'ViewManageLocations.html',{'data1':data1})

def EditLoc(request,id):
    data1=LocationTable.objects.filter(id=id)
    return render(request,'editLocation.html',{'data1':data1})

def UpdateLocation(request,id):
    if request.method=='POST':
        street=request.POST['street']
        city=request.POST['city']
        district=request.POST['district']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = LocationTable.objects.get(id=id).image
        state=request.POST['state']       
        LocationTable.objects.filter(id=id).update(street=street,city=city,district=district,image=file,state=state)
        return redirect('ViewManageLocations')
    
def DeleteLocation(request,id):
    LocationTable.objects.get(id=id).delete()
    return redirect('ViewManageLocations')   

def VenueData(request):
    if(request.method=='POST'):
        street=request.POST['street']
        VenuName=request.POST['VenuName']
        VenuType=request.POST['VenuType']
        VenuOwner=request.POST['VenuOwner']
        VenuNumber=request.POST['VenuNumber']
        VenuDescription=request.POST['VenuDescription']
        image=request.FILES['image']
        data=VenueTable(street=street,VenuName=VenuName,VenuType=VenuType,VenuOwner=VenuOwner,VenuNumber=VenuNumber,VenuDescription=VenuDescription,image=image)
        data.save()
        return redirect('ViewManageVenues')
    
def EditVenue(request):
    data2=VenueTable.objects.all()
    return render(request,'ViewManageVenues',{'data2':data2})

def EditVen(request,id):
    data1=LocationTable.objects.all()
    data2=VenueTable.objects.filter(id=id)
    return render(request,'EditVenue.html',{'data1':data1,'data2':data2})

def UpdateVenue(request,id):
    if request.method=='POST':
        street=request.POST['street']
        VenuName=request.POST['VenuName']
        VenuType=request.POST['VenuType']
        VenuOwner=request.POST['VenuOwner']
        VenuNumber=request.POST['VenuNumber']
        VenuDescription=request.POST['VenuDescription']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = VenueTable.objects.get(id=id).image
        VenueTable.objects.filter(id=id).update(street=street,VenuName=VenuName,VenuType=VenuType,VenuOwner=VenuOwner,VenuNumber=VenuNumber,VenuDescription=VenuDescription,image=file)        
        return redirect('ViewManageVenues')
    
def DeleteVenue(request,id):
    VenueTable.objects.get(id=id).delete()
    return redirect('ViewManageVenues')   

def Managerdata(request):
    if(request.method=='POST'):
        VenuName=request.POST['VenuName']
        ManagerName=request.POST['ManagerName']
        ManagerPlace=request.POST['ManagerPlace']
        ManagerNumber=request.POST['ManagerNumber']
        data=ManagerTable(VenuName=VenuName,ManagerName=ManagerName,ManagerPlace=ManagerPlace,ManagerNumber=ManagerNumber)
        data.save()
        return redirect('ViewManageManager')
    
def EditManger(request):
    data=ManagerTable.objects.all()
    return render(request,'ViewManageManager',{'data':data})

def EditMan(request,id):
    data2=VenueTable.objects.all()
    data=ManagerTable.objects.filter(id=id)
    return render(request,'EditManager.html',{'data2':data2,'data':data})

def UpdateManager(request,id):
    if(request.method=='POST'):
        VenuName=request.POST['VenuName']
        ManagerName=request.POST['ManagerName']
        ManagerPlace=request.POST['ManagerPlace']
        ManagerNumber=request.POST['ManagerNumber']       
        ManagerTable.objects.filter(id=id).update(VenuName=VenuName,ManagerName=ManagerName,ManagerPlace=ManagerPlace,ManagerNumber=ManagerNumber)        
        return redirect('ViewManageManager')
    
def DeleteManager(request,id):
    ManagerTable.objects.get(id=id).delete()
    return redirect('ViewManageManager')  