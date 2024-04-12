from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import tbl_admin,tbl_district,tbl_place
# Create your views here.
def User(request):
    if request.method=="POST":
        tbl_user.objects.create(user_name=request.POST.get("name"),
                                user_email=request.POST.get("email"),
                                user_contact=request.POST.get("contact"),
                                user_address=request.POST.get("address"),
                                user_photo=request.FILES.get("photo"),
                                user_password=request.POST.get("password"))
        return render(request,"Guest/UserRegistration.html")
    else:
        return render(request,"Guest/UserRegistration.html")

def Login(request):
    if request.method=="POST":
        Email=request.POST.get("Email")
        Password=request.POST.get("password")
        acount=tbl_admin.objects.filter(admin_email=Email,admin_password=Password).count()
        ucount=tbl_user.objects.filter(user_email=Email,user_password=Password).count()
        scount=tbl_sevicecenter.objects.filter(scenter_email=Email,scenter_password=Password,scenter_vstatus=1).count()
        if acount>0:
            admin=tbl_admin.objects.get(admin_email=Email,admin_password=Password)
            request.session["adminid"]=admin.id
            request.session["adminname"]=admin.admin_name
            return redirect("Webadmin:Home")
        elif ucount>0:
            user=tbl_user.objects.get(user_email=Email,user_password=Password)
            request.session["userid"]=user.id
            request.session["username"]=user.user_name
            return redirect("webuser:Home")
        elif scount>0:
            scenter=tbl_sevicecenter.objects.get(scenter_email=Email,scenter_password=Password,scenter_vstatus=1)
            request.session["centerid"]=scenter.id
            request.session["centername"]=scenter.scenter_name
            return redirect("webcenter:Home")
        else:
            return render(request,"Guest/Login.html")
    else:
        return render(request,"Guest/Login.html")
def index(request):
    return render(request,"Guest/index.html")

def AjaxPlace(request):
    dist=tbl_district.objects.get(id=request.GET.get("disd"))
    placedata=tbl_place.objects.filter(district=dist)
    return render(request,"Guest/Ajaxplace.html",{"place":placedata})

def Servicecenter(request):
    district=tbl_district.objects.all()
    manufact=tbl_manufacturer.objects.all()
    if request.method=="POST":
        placeid=tbl_place.objects.get(id=request.POST.get("place"))
        selmanufact=tbl_manufacturer.objects.get(id=request.POST.get("manufacturer"))
        tbl_sevicecenter.objects.create(scenter_name=request.POST.get("txt_name"),
                                        scenter_email=request.POST.get("txt_email"),
                                        scenter_contact=request.POST.get("txt_contant"),
                                        scenter_address=request.POST.get("address"),
                                        place=placeid,
                                        manufacturer=selmanufact,
                                        scenter_photo=request.FILES.get("photo"),
                                        scenter_proof=request.FILES.get("proof"),
                                        scenter_password=request.POST.get("txt_password"))
        return redirect("webguest:Servicecenter")
    else:
        return render(request,"Guest/ServiceCenter.html",{'district':district,'manufact':manufact})