from rest_framework  import serializers
from . models import *




class Users_serailizer(serializers.ModelSerializer):
    class Meta :
        model = Users
        fields=['id','vchr_name','username','email','password','int_mobile']
        
        extra_kwargs = {
            'password':{'write_only': True},
         
        }
    def create(self, validated_data):
        user = Users.objects.create_user(**validated_data)
		
        return user
    
class Users_UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['vchr_name','username','email','int_mobile']
        read_only_fields =('password',)
        extra_kwargs = {
            'password':{'read_only': True}
            
        }

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
        
    def to_representation(self, instance):
        rep= super().to_representation(instance)
        rep['country_id']=Country.objects.filter(id=rep['country_id']).values('id','name').first()
        
        return rep