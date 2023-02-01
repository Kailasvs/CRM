from django.db import models
from account.models import *



class Business_Category(models.Model):
    name=models.CharField(max_length=1024)
    
    
    def __str__(self):
        return self.name
    
    
class General_Information(Created_Model,Created_by,models.Model):   
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
        return self.company_name


class Personal_Information(Created_by,Created_Model,models.Model):
    contact_person=models.CharField(max_length=1024)
    designation=models.CharField(max_length=1024,null=True)
    mob_number=models.CharField(max_length=15,null=True)
    insta_id=models.CharField(max_length=1024,null=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    whatsapp_no=models.CharField(max_length=1024,null=True)
    fb_id=models.CharField(max_length=1024,null=True)
    front_office_assistant=models.CharField(max_length=1024,null=True)
    company_id=models.ForeignKey(General_Information,on_delete=models.CASCADE,null=True)


class Business_Information(Created_Model,models.Model):
    trade_line=models.CharField(max_length=1024,null=True)
    major_sector=models.CharField(max_length=1024,null=True)
    existing_service_providers=models.CharField(max_length=1024,null=True)
    crrnt_shipping_lines=models.CharField(max_length=1024,null=True)
    business_volumes=models.CharField(max_length=1024,null=True)
    special_remarks=models.CharField(max_length=1024,null=True)
    company_id=models.ForeignKey(General_Information,on_delete=models.CASCADE,null=True)
    
    
    