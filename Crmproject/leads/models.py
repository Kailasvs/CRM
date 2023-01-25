
from django.db import models
from account.models import *



class Business_Category(models.Model):
    name=models.CharField(max_length=1024)
    
class General_Information(models.Model):   
    company_name = models.CharField(max_length=1024)
    address=models.TextField(null=True)
    landline_number=models.CharField(max_length=15,null=True)
    mobile_number=models.CharField(max_length=15,null=True)
    website=models.URLField(max_length=200,null=True)
    email=models.EmailField(max_length=254,null=True)
    nature_of_business=models.CharField(max_length=1024,null=True)
    business_ctgry=models.ForeignKey(Business_Category,on_delete=models.SET_NULL,null=True)
    management=models.CharField(max_length=1024,null=True)
    business_since=models.BigIntegerField(null=True)
    product_line=models.CharField(max_length=1024,null=True)
    

    def __str__(self):
        return self.name


class Personal_Information(models.Model):
    contact_person=models.CharField(max_length=1024)
    designation=models.CharField(max_length=1024,null=True)
    mob_number=models.CharField(max_length=15,null=True)
    insta_id=models.CharField(max_length=1024,null=True)
    nationality=models.ForeignKey(Nationality,on_delete=models.CASCADE)
    whatsapp_no=models.CharField(max_length=1024,null=True)
    fb_id=models.CharField(max_length=1024,null=True)
    company_id=models.ForeignKey(Business_Category,on_delete=models.PROTECT,null=True)

    