from rest_framework  import serializers
from . models import *



class General_Information_serializer(serializers.ModelSerializer):
    class Meta :
        model = General_Information
        fields ='__all__' 
        extra_kwargs={"created_by":{'required':False}}
        
           
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if rep['business_ctgry']:
            rep['business_ctgry']=Business_Category.objects.filter(id=int(rep['business_ctgry'])).values('id','name').first()
        rep['created_by']=Users.objects.filter(id=rep['created_by']).values('id','username')
        
        return rep
 
        
        
class Business_Category_serializer(serializers.ModelSerializer):
    class Meta :
        model = Business_Category
        fields ='__all__' 

class Personal_Information_serializer(serializers.ModelSerializer):
    class Meta :
        model = Personal_Information
        fields ='__all__' 
        extra_kwargs={"created_by":{'required':False}}
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if rep['country']:
            rep['country']=Country.objects.filter(id=int(rep['country'])).values('id','name').first()
        if rep['created_by']:
            rep['created_by']=Users.objects.filter(id=rep['created_by']).values('id','username')
        if rep['company_id']:
            rep['company_id']=General_Information.objects.filter(id=rep['company_id']).values('id','company_name')
        
        return rep
    
class Business_Information_serializer(serializers.ModelSerializer):
    class Meta :
        model = Business_Information
        fields ='__all__' 
        extra_kwargs={"created_by":{'required':False}}
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # if rep['created_by'] is not :
        #     rep['created_by']=Users.objects.filter(id=rep['created_by']).values('id','username')
        if rep['company_id']:
            rep['company_id']=General_Information.objects.filter(id=rep['company_id']).values('id','company_name')
        
        return rep