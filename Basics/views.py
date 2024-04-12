from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
        num1=int(request.POST.get("number 1"))
        num2=int(request.POST.get("number 2"))
        sum=num1+num2
        return render(request,"Basics/sum.html",{"Result":sum})
    else:
        return render(request,"Basics/sum.html")


def Calculate(request):
    if request.method=="POST":
        num1=float(request.POST.get("number1"))
        num2=float(request.POST.get("number2"))
        operator=request.POST.get("button")
        if operator == "+":
            result = num1 + num2
            return render(request,"Basics/calculator.html",{"result":result})
        elif operator == "-":
            result = num1 - num2
            return render(request,"Basics/calculator.html",{"result":result})
        elif operator == "*":
            result = num1 * num2
            return render(request,"Basics/calculator.html",{"result":result})
        elif operator == "/":
            result = num1 / num2
            return render(request,"Basics/calculator.html",{"result":result})
        else:
            return render(request,"Basics/calculator.html")
    else:
        return render(request,"Basics/calculator.html")
        
def Salary(request):
    if request.method=="POST":
        name1=request.POST.get("fname")
        name2=request.POST.get("lname")
        name=name1+name2
        gender=request.POST.get("gender")
        gender=gender
        martial=request.POST.get("martial")
        martial=martial
        department=request.POST.get("department")
        department=department
        salary=int(request.POST.get("salary"))
        salary=salary
        if 10000<salary:
            TA=.4*salary
            DA=.35*salary
            HRA=.3*salary
            LIC=.25*salary
            PF=.20*salary
        elif 5000<salary<10000:
            TA=.35*salary
            DA=.30*salary
            HRA=.25*salary
            LIC=.20*salary
            PF=.15*salary
        elif salary<5000:
            TA=.30*salary
            DA=.25*salary
            HRA=.20*salary
            LIC=.15*salary
            PF=.10*salary
        else:
            return render(request,"Basics/salary.html") 
        deduction=LIC+PF
        NETAMOUNT=salary+TA+DA+HRA-(LIC+PF)
        return render(request,"Basics/salary.html",{"name":name,"gender":gender,"martial":martial,"department":department,"salary":salary,"TA":TA,"DA":DA,"HRA":HRA,"LIC":LIC,"PF":PF,"deduction":deduction,"NETAMOUNT":NETAMOUNT})
    else:
        return render(request,"Basics/salary.html")     