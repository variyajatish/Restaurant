from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from .models import User,Counts,Items,Chef,Party,Chefs,Gimg 


def Home(request):
    data = User.objects.all()   
    print(data) 

    view = Counts.objects.all()   
    print(view)

    menu = Items.objects.all()   
    print(view)

    profle = Chef.objects.all()   
    print(view)

    about = Party.objects.all()   
    print(view)

    info = Chefs.objects.all()   
    print(view)

    gallery = Gimg.objects.all()   
    print(view)

    return render(request, 'index.html', {'title': "Home Page", "data": data, "view": view, "menu": menu, "profle": profle, "about": about, "info": info, "gallery": gallery})
    
def AddUser(request):
    print(request.GET)
    icon = request.POST.get('icon')
    heding = request.POST.get('heding')
    desc = request.POST.get('desc')
    updateId = request.POST.get('id')

    if(heding and desc and icon):
        User.objects.create(icon=icon,heding=heding,desc=desc)

    return render(request, 'demo.html')
    
    # return redirect('/')

def About(request):
    print(request.GET)
    number = request.POST.get('number')
    name = request.POST.get('name')
    updateId = request.POST.get('id')

    if(number and name):
        Counts.objects.create(number=number,name=name)

    return render(request, 'demo.html')
    
def ViewUser(request):
    # print(request.POST)
    # print(request.FILES)
    itemimage = request.FILES.get('itemimage')
    itemname = request.POST.get('itemname')
    itemabout = request.POST.get('itemabout')
    itemprice = request.POST.get('itemprice')
    updateId = request.POST.get('id')

    if(itemimage and itemname and itemabout and itemprice):
        Items.objects.create(itemimage=itemimage,itemname=itemname,itemabout=itemabout,itemprice=itemprice)

    return render(request, 'demo.html')

def ChefData(request):
    print(request.GET)
    about = request.POST.get('about')
    chefname = request.POST.get('chefname')
    postion = request.POST.get('postion')
    chefimage = request.POST.get('chefimage')
    updateId = request.POST.get('id')

    if(about and chefname and postion and chefimage):
        Chef.objects.create(about=about,chefname=chefname,postion=postion,chefimage=chefimage)

    return render(request, 'demo.html') 

def ChefPart(request):
    print(request.GET)
    pryimg = request.POST.get('pryimg')
    pryname = request.POST.get('pryname')
    pryamount = request.POST.get('pryamount')
    pryabout = request.POST.get('pryabout')
    updateId = request.POST.get('id')

    if(pryimg and pryname and pryamount and pryabout):
        Party.objects.create(pryimg=pryimg,pryname=pryname,pryamount=pryamount,pryabout=pryabout)

    return render(request, 'demo.html')  

def Chefsinfo(request):       
    print(request.GET)
    chefimg = request.POST.get('chefimg')
    chefsname = request.POST.get('chefsname')
    chefpostion = request.POST.get('chefpostion')
    chefinfo = request.POST.get('chefinfo')
    updateId = request.POST.get('id')

    if(chefimg and chefsname and chefpostion and chefinfo):
        Chefs.objects.create(chefimg=chefimg,chefsname=chefsname,chefpostion=chefpostion,chefinfo=chefinfo)

    return render(request, 'demo.html')

def GalleryImg(request):
    print(request.GET)
    galleryimg = request.POST.get('galleryimg')

    if(galleryimg):
        Gimg.objects.create(galleryimg=galleryimg)

    return render(request, 'demo.html')
