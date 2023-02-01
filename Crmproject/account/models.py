from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager, BaseUserManager,AbstractBaseUser
# Create your models here.



class SalesManager(models.Manager):
  '''first we get all objects from the database by
  calling the get_queryset method of the inherited class
  i.e. Manager class using super().get_queryset().
  After that we are filtering objects having city attribute equal to kolkata
  and return the filtered objects'''
  def get_queryset(self,username=None):
    if username :
        return super().get_queryset().filter(username=username,is_sales=True)
    return super().get_queryset().filter(is_sales=True)



class AdminManager(models.Manager):
  def get_queryset(self,username=None):
    if username :
        return super().get_queryset().filter(username=username,is_admin=True)
    return super().get_queryset().filter(is_admin=True)

class OperationManager(models.Manager):
  def get_queryset(self,username=None):
    if username :
        return super().get_queryset().filter(username=username,is_operations=True)
    return super().get_queryset().filter(is_operations=True)


class TeleCallManager(models.Manager):
  def get_queryset(self,username=None):
    if username :
        return super().get_queryset().filter(username=username,is_telecallers=True)
    return super().get_queryset().filter(is_telecallers=True)


class Manager_Manager(models.Manager):
  def get_queryset(self,username=None):
    if username :
        return super().get_queryset().filter(username=username,is_manager=True)
    return super().get_queryset().filter(is_manager=True)

class Country(models.Model):
    name = models.CharField(max_length=250,null=True)
    country_code = models.CharField(max_length=250,null=True)
    
    def __str__(self):
        return self.name
    
class State(models.Model):
    name=models.CharField(max_length=1024)
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE,null=True)

class Nationality(models.Model):
    name=models.CharField(max_length=1024)
    
class Created_Model(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Created_by(models.Model):
    created_by=models.PositiveIntegerField()
    
    class Meta:
        abstract = True
class Users(AbstractUser):
    vchr_name = models.CharField(max_length=250,null=True)
    int_mobile = models.BigIntegerField(null=True)
    bln_active = models.BooleanField(null=True)
    email=models.EmailField(max_length=254,unique=True,null=True)
    address = models.TextField(null=True) 
    profile_pic=models.ImageField(upload_to='profile',null=True)
    is_telecallers  = models.BooleanField(default = False)
    is_sales = models.BooleanField(default=False)
    is_operations=models.BooleanField(default=False)
    is_manager=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    objects = UserManager()
    sales_objects=SalesManager()
    admin_objects=AdminManager()
    operation_objects=OperationManager()
    telecaller_objects=TeleCallManager()
    manager_objects=Manager_Manager()
    
    USERNAME_FIELD = 'username'
    
    