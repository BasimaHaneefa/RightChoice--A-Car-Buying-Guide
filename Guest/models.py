from django.db import models
from Admin.models import tbl_place,tbl_manufacturer     
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to='User/')
    user_password=models.CharField(max_length=30)

class tbl_sevicecenter(models.Model):
    scenter_name=models.CharField(max_length=30)
    scenter_email=models.CharField(max_length=50)
    scenter_address=models.CharField(max_length=100)
    scenter_contact=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    scenter_photo=models.FileField(upload_to='ScenterDocs/')
    scenter_proof=models.FileField(upload_to='ScenterDocs/')
    scenter_password=models.CharField(max_length=30)
    scenter_vstatus=models.CharField(max_length=10,default=0)
    manufacturer=models.ForeignKey(tbl_manufacturer,on_delete=models.CASCADE,null=True)
