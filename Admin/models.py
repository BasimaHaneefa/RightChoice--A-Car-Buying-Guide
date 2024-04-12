from django.db import models

# Create your models here.
class tbl_bodytype(models.Model):
    bodytype_name=models.CharField(max_length=20)

class tbl_fueltype(models.Model):
    fueltype_name=models.CharField(max_length=20)

class tbl_transmission(models.Model):
    transmission_name=models.CharField(max_length=50)

class tbl_manufacturer(models.Model):
    manufacturer_name=models.CharField(max_length=50)

class tbl_make(models.Model):
    make_name=models.CharField(max_length=30)
    manufacturer=models.ForeignKey(tbl_manufacturer,on_delete=models.CASCADE)

class tbl_variant(models.Model):
    variant_name=models.CharField(max_length=50)
    make=models.ForeignKey(tbl_make,on_delete=models.CASCADE)

class tbl_year(models.Model):
    production_year=models.CharField(max_length=4)


class tbl_car(models.Model):
    variant=models.ForeignKey(tbl_variant,on_delete=models.CASCADE)
    transmission=models.ForeignKey(tbl_transmission,on_delete=models.CASCADE)
    fueltype=models.ForeignKey(tbl_fueltype,on_delete=models.CASCADE)
    bodytype=models.ForeignKey(tbl_bodytype,on_delete=models.CASCADE)
    production_year=models.CharField(max_length=20)
    car_mileage=models.CharField(max_length=30)
    car_price=models.IntegerField(max_length=50)
    engine_size=models.CharField(max_length=30)
    car_horsepower=models.CharField(max_length=30)
    car_torque=models.CharField(max_length=30)
    car_photo=models.FileField(upload_to='Car/')
    seat_capacity=models.CharField(max_length=30)
    car_gear=models.CharField(max_length=30)
    car_tire=models.CharField(max_length=30)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

class tbl_gallery(models.Model):
    gallery_image=models.FileField(upload_to='CarGallery/')
    car=models.ForeignKey(tbl_car,on_delete=models.CASCADE)

class tbl_district(models.Model):
    district_name=models.CharField(max_length=20)
    
class tbl_place(models.Model):
    place_name=models.CharField(max_length=20)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)


class tbl_servicetype(models.Model):
    service_name=models.CharField(max_length=50)