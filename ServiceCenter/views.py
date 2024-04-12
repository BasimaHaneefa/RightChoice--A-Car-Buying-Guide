from django.shortcuts import redirect, render
from Guest.models import tbl_sevicecenter
from UserApp.models import tbl_servicerquest
# Create your views here.
def Home(request):
    if 'centerid' in request.session:
        center=request.session["centername"]
        return render(request,"ServiceCenter/Home.html",{"center":center})
    else:
         return render(request,"Guest/Login.html")
  
def Myprofile(request):
    center=tbl_sevicecenter.objects.get(id=request.session["centerid"])
    return render(request,"ServiceCenter/MyProfile.html",{"center":center})

def EditProfile(request):
    center=tbl_sevicecenter.objects.get(id=request.session["centerid"])
    if request.method=="POST":
        center.scenter_name=request.POST.get("name")
        center.scenter_email=request.POST.get("Email")
        center.scenter_contact=request.POST.get("Contact")
        center.scenter_address=request.POST.get("Address")
        center.save()
        return redirect("webcenter:MyProfile")
    else:
        return render(request,"ServiceCenter/EditProfile.html",{"center":center})

def ChangePassword(request):
    if request.method=="POST":
        Current=request.POST.get("current")
        New=request.POST.get("new")
        Confirm=request.POST.get("confirm")
        center=tbl_sevicecenter.objects.get(id=request.session["centerid"])
        password=center.scenter_password
        if password == Current:
            if New == Confirm:
                center.scenter_password=New
                center.save()
                return redirect("webcenter:MyProfile")
            else:
                return render(request,"ServiceCenter/ChangePassword.html",{"msg":"Error in Confirm Password!!"})
        else:
            return render(request,"ServiceCenter/ChangePassword.html",{"msg":"Invalid Current Password!!"})
    else:
        return render(request,"ServiceCenter/ChangePassword.html")
    

def Viewmyrequest(request):
    center=tbl_sevicecenter.objects.get(id=request.session["centerid"])
    service=tbl_servicerquest.objects.filter(scenter=center)
    return render(request,"ServiceCenter/ViewMyServiceRequest.html",{'data':service})

def AcceptRequest(request,aid):
    req=tbl_servicerquest.objects.get(id=aid)
    req.srequest_status=1
    req.save()
    return redirect("webcenter:Viewmyrequest")

def RejectRequest(request,aid):
    req=tbl_servicerquest.objects.get(id=aid)
    req.srequest_status=2
    req.save()
    return redirect("webcenter:Viewmyrequest")

def logout(request):
    if 'centerid' in request.session:
        del request.session['centerid']
        return redirect('webguest:Login')
    else:
        return redirect('webguest:Login')