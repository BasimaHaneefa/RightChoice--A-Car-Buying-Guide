from django.http import JsonResponse
from django.shortcuts import render,redirect
from Guest.models import tbl_user,tbl_sevicecenter
from Admin.models import *
from UserApp.models import *
# Create your views here.
def Home(request):
    if 'userid' in request.session:
        user=request.session["username"]
        return render(request,"UserApp/Home.html",{"User":user})
    else:
         return render(request,"Guest/Login.html")
  
def Myprofile(request):
    user=tbl_user.objects.get(id=request.session["userid"])
    return render(request,"UserApp/MyProfile.html",{"User":user})

def EditProfile(request):
    user=tbl_user.objects.get(id=request.session["userid"])
    if request.method=="POST":
        user.user_name=request.POST.get("name")
        user.user_email=request.POST.get("Email")
        user.user_contact=request.POST.get("Contact")
        user.user_address=request.POST.get("Address")
        user.save()
        return redirect("webuser:MyProfile")
    else:
        return render(request,"UserApp/EditProfile.html",{"User":user})

def ChangePassword(request):
    if request.method=="POST":
        Current=request.POST.get("current")
        New=request.POST.get("new")
        Confirm=request.POST.get("confirm")
        user=tbl_user.objects.get(id=request.session["userid"])
        password=user.user_password
        if password == Current:
            if New == Confirm:
                user.user_password=New
                user.save()
                return redirect("webuser:MyProfile")
            else:
                return render(request,"UserApp/ChangePassword.html",{"msg":"Error in Confirm Password!!"})
        else:
            return render(request,"UserApp/ChangePassword.html",{"msg":"Invalid Current Password!!"})
    else:
        return render(request,"UserApp/ChangePassword.html")

def Search(request):
    ar=[1,2,3,4,5]
    cardata=tbl_car.objects.all()
    manufact=tbl_manufacturer.objects.all()
    make=tbl_make.objects.all()
    variant=tbl_bodytype.objects.all()
    bodytype=tbl_bodytype.objects.all()
    fueltype=tbl_fueltype.objects.all()
    avg_list = []  # Create a list to store average ratings for each car

    reviewcount = 0
    for c in cardata:
        reviewcount = tbl_review.objects.filter(car=c.id).count()
        # print(reviewcount)
        res = 0
        avg = 0
        review = tbl_review.objects.filter(car=c.id)
        for rev in review:
            res = res + rev.user_rating
            # print(res)
            avg = res//reviewcount
            # print(avg)
        avg_list.append(avg)
    print(avg_list)
    cdata = zip(cardata,avg_list)
    # for car in cardata:
    #     rating_count = tbl_review.objects.filter(car=car.id).count()
    #     if rating_count > 0:
    #         res = 0
    #         rating = tbl_review.objects.filter(car=car.id)
    #         for r in rating:
    #             res += int(r.user_rating)
    #         avg = res / rating_count
    #         avg_list.append(avg)
    #     else:
    #         avg_list.append(0)  # If no ratings, set average to 0

    return render(request, "UserApp/SearchCar.html", {"cars": cdata, "manufact": manufact, "make": make, "variant": variant, "bodytype": bodytype, "fueltype": fueltype, "avg": avg_list,"ar":ar})

def AjaxSearch(request):
    if (request.GET.get("man") != "") and (request.GET.get("make") != "") and (request.GET.get("variant") != "")  and (request.GET.get("budget") != "") and (request.GET.get("buget")):
        mandata=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        makedata = tbl_make.objects.get(id=request.GET.get("make"))
        vardata = tbl_bodytype.objects.get(id=request.GET.get("variant"))
        budget=request.GET.get("budget")
        car=tbl_car.objects.filter(bodytype=vardata,variant__make=makedata,variant__make__manufacturer=mandata,car_price__lte=budget)
        return render(request,"UserApp/AjaxSearch.html",{'cars':car})
    elif (request.GET.get("man") != "") and (request.GET.get("make") != "") and (request.GET.get("variant") != "") :
        mandata=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        makedata = tbl_make.objects.get(id=request.GET.get("make"))
        vardata = tbl_bodytype.objects.get(id=request.GET.get("variant"))
        car=tbl_car.objects.filter(bodytype=vardata,variant__make=makedata,variant__make__manufacturer=mandata)
        return render(request,"UserApp/AjaxSearch.html",{'cars':car})
    elif request.GET.get("man") != "":
        mandata=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        car = tbl_car.objects.filter(variant__make__manufacturer=mandata)
        return render(request,"UserApp/AjaxSearch.html",{'cars':car})
    elif request.GET.get("make") != "":
        makedata = tbl_make.objects.get(id=request.GET.get("make"))
        car=tbl_car.objects.filter(variant__make=makedata)
        return render(request,"UserApp/AjaxSearch.html",{'cars':car})
    elif (request.GET.get("man") != "") and (request.GET.get("make") != "") and (request.GET.get("variant") == ""):
        mandata=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        makedata = tbl_make.objects.get(id=request.GET.get("make"))
        car=tbl_car.objects.filter(variant__make=makedata,variant__make__manufacturer=mandata)
        return render(request,"UserApp/AjaxSearch.html",{'cars':car})
    elif (request.GET.get("man") != "") and (request.GET.get("variant") != "") and (request.GET.get("make") == ""):
        mandata=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        vardata = tbl_bodytype.objects.get(id=request.GET.get("variant"))
        print(vardata)
        car=tbl_car.objects.filter(bodytype=vardata,variant__make__manufacturer=mandata)
        return render(request,"UserApp/AjaxSearch.html",{'cars':car})
    else:
        vardata = tbl_bodytype.objects.get(id=request.GET.get("variant"))
        car=tbl_car.objects.filter(bodytype=vardata)
        return render(request,"UserApp/AjaxSearch.html",{'cars':car})
    
def ajaxbudget(request):
    if request.GET.get('budget') != "":
        budget_rate = request.GET.get('budget')  
        cardata= tbl_car.objects.filter(car_price__lte=request.GET.get('budget'))
    return render(request, 'UserApp/AjaxBudget.html', {'cars': cardata})


def ViewGallery(request,cid):
    car=tbl_car.objects.get(id=cid)
    gallery=tbl_gallery.objects.filter(car=car)
    return render(request,"UserApp/ViewGallery.html",{"gallery":gallery})

def rating(request,cid):
    if 'userid' in request.session:
        parray=[1,2,3,4,5]
        cid=cid
        cdata=tbl_car.objects.get(id=cid)
        wdata=tbl_user.objects.get(id=request.session["userid"])
        counts=0
        counts=stardata=tbl_review.objects.filter(car=cdata).count()
        if counts>0:
            res=0
            stardata=tbl_review.objects.filter(car=cdata).order_by('-review_datetime')
            for i in stardata:
                res = res + int(i.user_rating)
                avg=res//counts  
            return render(request,"UserApp/Rating.html",{"cid":cid,"data":stardata,"ar":parray,"avg":avg,"count":counts})
        else:
            return render(request,"UserApp/Rating.html",{'cid':cid})
    else:
        return redirect("webguest:login")

def ajaxrating(request):
    parray=[1,2,3,4,5]
    user_rating=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    car=request.GET.get('workid')
    cdata=tbl_car.objects.get(id=car)
    cust=tbl_user.objects.get(id=request.session["userid"])
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=user_rating,car=cdata,user=cust)
    stardata=tbl_review.objects.filter(car=car).order_by('-review_datetime')
    return render(request,"UserApp/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    car_id = request.GET.get("pdt")
    cdata = tbl_car.objects.get(id=car_id)
    rate = tbl_review.objects.filter(car=cdata)

    for i in rate:
        if int(i.user_rating) == 5:
            five += 1
        elif int(i.user_rating) == 4:
            four += 1
        elif int(i.user_rating) == 3:
            three += 1
        elif int(i.user_rating) == 2:
            two += 1
        elif int(i.user_rating) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)

def Complaint(request):
    userdata=tbl_user.objects.get(id=request.session["userid"])
    data=tbl_complaint.objects.filter(user=userdata)
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session["userid"])
        tbl_complaint.objects.create(complaint_title=request.POST.get("title"),
                                     complaint_content=request.POST.get("complaint"),
                                     user=userdata)
    return render(request,"UserApp/Complaint.html",{"Data":data})

def DelComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("webuser:complaint")

def EditComplaint(request,eid):
    com=tbl_complaint.objects.get(id=eid)
    if request.method=="POST":
        com.complaint_title=request.POST.get("title")
        com.complaint_content=request.POST.get("complaint")
        com.save()
        return redirect("webuser:complaint")
    else:
        return render(request,"UserApp/Complaint.html",{"com":com})
    
def Feedback(request):
    userdata=tbl_user.objects.get(id=request.session["userid"])
    data=tbl_feedback.objects.filter(user=userdata)
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session["userid"])
        tbl_feedback.objects.create(feedback_content=request.POST.get("complaint"),
                                     user=userdata)
    return render(request,"UserApp/Feedback.html",{"Data":data})

def DelFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("webuser:feedback")

def EditFeedback(request,eid):
    com=tbl_feedback.objects.get(id=eid)
    if request.method=="POST":
        com.feedback_content_content=request.POST.get("complaint")
        com.save()
        return redirect("webuser:feedback")
    else:
        return render(request,"UserApp/Feedback.html",{"com":com})
    
def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
        return redirect('webguest:Login')
    else:
        return redirect('webguest:Login')
def index(request):
    return render(request,"UserApp/Home.html")

def SearchCenter(request):
    district=tbl_district.objects.all()
    center=tbl_sevicecenter.objects.filter(scenter_vstatus=1)
    manufact=tbl_manufacturer.objects.all()
    return render(request,"UserApp/SearchServiceCenter.html",{'center':center,'district':district,'manufact':manufact})

def AjaxSearchCenter(request):
    if request.GET.get("dist") != "" and request.GET.get("place") !="" and  request.GET.get("man"):
        district=tbl_district.objects.get(id=request.GET.get("dist"))
        place=tbl_place.objects.get(id=request.GET.get("place"))
        man=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        data=tbl_sevicecenter.objects.filter(place__district=district,place=place,scenter_vstatus=1,manufacturer=man)
        return render(request,"UserApp/AjaxSearchCenter.html",{'center':data})
    elif request.GET.get("dist") != "" and request.GET.get("place") !="" :
        district=tbl_district.objects.get(id=request.GET.get("dist"))
        place=tbl_place.objects.get(id=request.GET.get("place"))
        data=tbl_sevicecenter.objects.filter(place__district=district,place=place,scenter_vstatus=1)
        return render(request,"UserApp/AjaxSearchCenter.html",{'center':data})  
    elif request.GET.get("place") !="" and  request.GET.get("man"):
        place=tbl_place.objects.get(id=request.GET.get("place"))
        man=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        data=tbl_sevicecenter.objects.filter(place=place,scenter_vstatus=1,manufacturer=man)
        return render(request,"UserApp/AjaxSearchCenter.html",{'center':data}) 
    elif request.GET.get("dist") != ""  and  request.GET.get("man"):
        district=tbl_district.objects.get(id=request.GET.get("dist"))
        man=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        data=tbl_sevicecenter.objects.filter(place__district=district,scenter_vstatus=1,manufacturer=man)
        return render(request,"UserApp/AjaxSearchCenter.html",{'center':data})
    if request.GET.get("man"):
        man=tbl_manufacturer.objects.get(id=request.GET.get("man"))
        data=tbl_sevicecenter.objects.filter(scenter_vstatus=1,manufacturer=man)
        return render(request,"UserApp/AjaxSearchCenter.html",{'center':data})
    elif request.GET.get("dist") != "":
        district=tbl_district.objects.get(id=request.GET.get("dist"))
        data=tbl_sevicecenter.objects.filter(place__district=district,scenter_vstatus=1)
        return render(request,"UserApp/AjaxSearchCenter.html",{'center':data})
    elif request.GET.get("place") !="":
        place=tbl_place.objects.get(id=request.GET.get("place"))
        data=tbl_sevicecenter.objects.filter(place=place,scenter_vstatus=1)
        return render(request,"UserApp/AjaxSearchCenter.html",{'center':data})
    else:
        center=tbl_sevicecenter.objects.filter(scenter_vstatus=1)
        return render(request,"UserApp/AjaxSearchCenter.html",{'center':data})
    
def Servicerequest(request,did):
    stype=tbl_servicetype.objects.all()
    center=tbl_sevicecenter.objects.get(id=did)
    userdata=tbl_user.objects.get(id=request.session["userid"])
    if request.method=="POST":
        type=tbl_servicetype.objects.get(id=request.POST.get("seltype"))
        tbl_servicerquest.objects.create(srequest_details=request.POST.get("details"),
                                         servicetype=type,
                                         srequest_fordate=request.POST.get("fordate"),
                                         srequest_car=request.POST.get("car"),
                                         scenter=center,
                                         user=userdata)
        return redirect("webuser:Index")
    else:
        return render(request,"UserApp/ServiceRequest.html",{'stype':stype})
    

def Viewmyrequest(request):
    userdata=tbl_user.objects.get(id=request.session["userid"])
    service=tbl_servicerquest.objects.filter(user=userdata)
    return render(request,"UserApp/ViewMyServiceRequest.html",{'data':service})