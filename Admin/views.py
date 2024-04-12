from django.shortcuts import render,redirect
from Admin.models import *
from UserApp.models import *
from Guest.models import tbl_sevicecenter
# Create your views here.
def Home(request):
    if 'adminid' in request.session:
        admin=request.session["adminname"]
        usercount=tbl_user.objects.all().count()
        carcount=tbl_car.objects.all().count()
        user=tbl_user.objects.all()
        return render(request,"Admin/Home.html",{"Admin":admin,"user":usercount,"Car":carcount,"UserData":user})
    else:
         return render(request,"Guest/Login.html")
    

def Bodytype(request):
    bodytype=tbl_bodytype.objects.all()
    if request.method=="POST":
        tbl_bodytype.objects.create(bodytype_name=request.POST.get("Bodytype"))
        return render(request,"Admin/Bodytype.html",{"Type":bodytype})
    else:   
        return render(request,"Admin/Bodytype.html",{"Type":bodytype})

def DelBodyType(request,did):
    tbl_bodytype.objects.get(id=did).delete()
    return redirect("Webadmin:Bodytype")

def updateBodytype(request,did):
    body=tbl_bodytype.objects.get(id=did)
    if request.method=="POST":
        body.bodytype_name=request.POST.get("Bodytype")   
        body.save() 
        return redirect("Webadmin:Bodytype")
    else:
        return render(request,"Admin/Bodytype.html",{"Body":body})

def Fueltype(request):
    fueltype=tbl_fueltype.objects.all()
    if request.method=="POST":
        tbl_fueltype.objects.create(fueltype_name=request.POST.get("Fueltype"))
        return render(request,"Admin/Fueltype.html",{"type":fueltype})
    else:
        return render(request,"Admin/Fueltype.html",{"type":fueltype})

def DelFueltype(request,did):
    tbl_fueltype.objects.get(id=did).delete()
    return redirect("Webadmin:Fueltype")

def updateFueltype(request,did):
    fuel=tbl_fueltype.objects.get(id=did)
    if request.method=="POST":
        fuel.fueltype_name=request.POST.get("Fueltype")
        fuel.save()
        return redirect("Webadmin:Fueltype")
    else:
        return render(request,"Admin/Fueltype.html",{"Fuel":fuel})

def Transmission(request):
    transmission=tbl_transmission.objects.all()
    if request.method=="POST":
        tbl_transmission.objects.create(transmission_name=request.POST.get("Transmission"))
        return render(request,"Admin/Transmission.html",{"type":transmission})    
    else:
        return render(request,"Admin/Transmission.html",{"type":transmission})

def delTransmission(request,did):
    tbl_transmission.objects.get(id=did).delete()
    return redirect("Webadmin:Transmission")

def updateTransmission(request,did):
    trans=tbl_transmission.objects.get(id=did)
    if request.method=="POST":
        trans.transmission_name=request.POST.get("Transmission")
        trans.save()
        return redirect("Webadmin:Transmission")
    else:
        return render(request,"Admin/Transmission.html",{"Trans":trans})

def Manufacturer(request):
    manufacturer=tbl_manufacturer.objects.all()
    if request.method=="POST":
        tbl_manufacturer.objects.create(manufacturer_name=request.POST.get("Manufacturer"))
        return render(request,"Admin/Manufacturer.html",{"type":manufacturer})
    else:
        return render(request,"Admin/Manufacturer.html",{"type":manufacturer})

def delManufacturer(request,did):
    tbl_manufacturer.objects.get(id=did).delete()
    return redirect("Webadmin:Manufacturer")

def updateManufacturer(request,did):
    manufact=tbl_manufacturer.objects.get(id=did)
    if request.method=="POST":
        manufact.manufacturer_name=request.POST.get("Manufacturer")
        manufact.save()
        return redirect("Webadmin:Manufacturer")
    else:
        return render(request,"Admin/Manufacturer.html",{"manufact":manufact})

def Make(request):
    make=tbl_make.objects.all()
    data=tbl_manufacturer.objects.all()
    if request.method=="POST":
        selectedmanufact=tbl_manufacturer.objects.get(id=request.POST.get("manufacture"))
        tbl_make.objects.create(make_name=request.POST.get("makename"),manufacturer=selectedmanufact)
        return render(request,"Admin/Make.html",{"Data":data,"data":make})
    else:
        return render(request,"Admin/Make.html",{"Data":data,"data":make})

def deletemake(request,did):
    tbl_make.objects.get(id=did).delete()
    return redirect("Webadmin:Make")

def updateMake(request,did):
    data=tbl_manufacturer.objects.all()
    make=tbl_make.objects.get(id=did)
    if request.method=="POST":
        man=tbl_manufacturer.objects.get(id=request.POST.get("manufacture"))
        make.make_name=request.POST.get("makename")
        make.manufacturer=man
        make.save()
        return redirect("Webadmin:Make")
    else:
        return render(request,"Admin/Make.html",{"Data":data,"Make":make})

def variant(request):
    manufact=tbl_manufacturer.objects.all()
    variant=tbl_variant.objects.all()
    if request.method=="POST":
        makeid=tbl_make.objects.get(id=request.POST.get("make"))
        tbl_variant.objects.create(variant_name=request.POST.get("Variant"),make=makeid)
        return render(request,"Admin/variant.html",{"manufact":manufact,"variant":variant})
    else:
        return render(request,"Admin/variant.html",{"manufact":manufact,"variant":variant})

def Deletevariant(request,did):
    tbl_variant.objects.get(id=did).delete()
    return redirect("Webadmin:variant")


def ajaxmake(request):
    manufact=tbl_manufacturer.objects.get(id=request.GET.get("disd"))
    make=tbl_make.objects.filter(manufacturer=manufact)
    return render(request,"Admin/AjaxMake.html",{"make":make})

def car(request):
    manufact=tbl_manufacturer.objects.all()
    fuel=tbl_fueltype.objects.all()
    trans=tbl_transmission.objects.all()
    body=tbl_bodytype.objects.all()
    car=tbl_car.objects.all()
    if request.method=="POST":
        variantid=tbl_variant.objects.get(id=request.POST.get("variant"))
        fuelid=tbl_fueltype.objects.get(id=request.POST.get("fueltype"))
        transid=tbl_transmission.objects.get(id=request.POST.get("transmission"))
        bodyid=tbl_bodytype.objects.get(id=request.POST.get("bodytype"))
        tbl_car.objects.create(variant=variantid,transmission=transid,fueltype=fuelid,bodytype=bodyid,
                                production_year=request.POST.get("productionYear"),
                                car_mileage=request.POST.get("mileage"),
                                car_price=request.POST.get("price"),
                                engine_size=request.POST.get("engineSize"),
                                car_horsepower=request.POST.get("horsepower"),
                                car_torque=request.POST.get("torque"),
                                car_photo=request.FILES.get("carPhoto"),
                                seat_capacity=request.POST.get("seatCapacity"),
                                car_gear=request.POST.get("gear"),
                                car_tire=request.POST.get("tire"))
        return render(request,"Admin/Car.html",{"manufact":manufact,"fuel":fuel,"trans":trans,"body":body,"car":car})
    else:
        return render(request,"Admin/Car.html",{"manufact":manufact,"fuel":fuel,"trans":trans,"body":body,"car":car})

def ajaxvariant(request):
    makeid=tbl_make.objects.get(id=request.GET.get("disd"))
    variant=tbl_variant.objects.filter(make=makeid)
    return render(request,"Admin/AjaxVariant.html",{"variant":variant})

def delcar(request,did):
    tbl_car.objects.get(id=did).delete()
    return redirect("Webadmin:car")

def Gallery(request,cid):
    images=tbl_gallery.objects.all()
    if request.method=="POST":
        car = tbl_car.objects.get(id=cid)
        for file in request.FILES.getlist("car_photos"):
            tbl_gallery.objects.create(gallery_image=file, car=car)
        return render(request,"Admin/Gallery.html",{"gallery":images})
    else:
        return render(request,"Admin/Gallery.html",{"gallery":images})
    
def DeleteGallery(request,did):
    tbl_gallery.objects.get(id=did).delete()
    return redirect("Webadmin:car")

def ViewComplaint(request):
    com=tbl_complaint.objects.filter(complaint_status=0)
    replied=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{"new":com,"replied":replied})

def Reply(request,cid):
    com=tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("Reply")
        com.complaint_status=1
        com.save()
        return redirect("Webadmin:viewcomplaint")
    else:
        return render(request,"Admin/Reply.html")    
    
def ViewFeedback(request):
    com=tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{"new":com})

def logout(request):
    if 'adminid' in request.session:
        del request.session['adminid']
        return redirect('webguest:Login')
    else:
        return redirect('webguest:Login')

def district(request):
    district=tbl_district.objects.all()    
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("district"))
        return render(request,"Admin/district.html",{"Type":district})
    else:
        return render(request,"Admin/district.html",{"Type":district})

def Deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Webadmin:district")

def updatedistrict(request,did):
    district=tbl_district.objects.get(id=did)
    if request.method=="POST":
        district.district_name=request.POST.get("district")
        district.save()
        return redirect("Webadmin:district")
    else:
        return render(request,"Admin/district.html",{"district":district})
    
def place(request):
   place=tbl_place.objects.all()
   district=tbl_district.objects.all()
   if request.method=="POST":
        selecteddistrict=tbl_district.objects.get(id=request.POST.get("district"))
        tbl_place.objects.create(place_name=request.POST.get("place"),district=selecteddistrict)
        return render(request,"Admin/place.html",{"Type":place,"District":district})
   else:
        return render(request,"Admin/place.html",{"Type":place,"District":district}) 
        
def Delplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Webadmin:place")

def updateplace(request,did):
    district=tbl_district.objects.all()
    place=tbl_place.objects.get(id=did)
    if request.method=="POST":
        place.place_name_=request.POST.get("place")
        place.save()
        return redirect("Webadmin:place")
    else:
        return render(request,"Admin/place.html",{"place":place,"District":district})


def CenterVerification(request):
    new=tbl_sevicecenter.objects.filter(scenter_vstatus=0)
    accept=tbl_sevicecenter.objects.filter(scenter_vstatus=1)
    rejected=tbl_sevicecenter.objects.filter(scenter_vstatus=2)
    return render(request,"Admin/ServicecenterVerification.html",{'new':new,'accept':accept,'rejected':rejected})

def AcceptCenter(request,did):
    center=tbl_sevicecenter.objects.get(id=did)
    center.scenter_vstatus=1
    center.save()
    return redirect("Webadmin:CenterVerification")

def RejectCenter(request,did):
    center=tbl_sevicecenter.objects.get(id=did)
    center.scenter_vstatus=2
    center.save()
    return redirect("Webadmin:CenterVerification")

def Servicetype(request):
    servicetype=tbl_servicetype.objects.all()
    if request.method=="POST":
        tbl_servicetype.objects.create(service_name=request.POST.get("Servicetype"))
        return redirect("Webadmin:Servicetype")
    else:
        return render(request,"Admin/ServiceType.html",{'service':servicetype})

def Delservice(request,did):
    tbl_servicetype.objects.get(id=did).delete()
    return redirect("Webadmin:Servicetype")

def updateservice(request,did):
    service=tbl_servicetype.objects.get(id=did)
    if request.method=="POST":
        service.service_name=request.POST.get("Servicetype")
        service.save()
        return redirect("Webadmin:Servicetype")
    else:
        return render(request,"Admin/ServiceType.html",{"servicetype":service})