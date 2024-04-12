from django.db import models
from Guest.models import tbl_user,tbl_sevicecenter
from Admin.models import tbl_car,tbl_servicetype
# Create your models here.
class tbl_review(models.Model):
    user_rating=models.IntegerField(max_length=20)
    user_review=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    review_datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    car= models.ForeignKey(tbl_car,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=100)
    complaint_status=models.CharField(default=0,max_length=5)
    complaint_reply=models.CharField(default="Not replied yet",max_length=100)
    complaint_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_servicerquest(models.Model):
    srequest_details=models.CharField(max_length=100)
    srequest_status=models.CharField(max_length=10,default=0)
    servicetype=models.ForeignKey(tbl_servicetype,on_delete=models.CASCADE)
    srequest_fordate=models.DateField()
    srequest_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    scenter=models.ForeignKey(tbl_sevicecenter,on_delete=models.CASCADE,null=True)
    srequest_car=models.CharField(max_length=100,null=True)

