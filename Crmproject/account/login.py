from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['id']=self.user.id
        data['vchr_name'] = self.user.vchr_name
        data['username'] = self.user.username
        data['email']=self.user.email
        data['is_admin'] = self.user.is_admin
        if self.user.is_manager == True:
            data['role'] = 'Manager'
        elif self.user.is_telecallers == True:
            data['role'] = 'Telecaller'
        elif self.user.is_sales == True:
            data['role']='Sale'
        elif self.user.is_operations == True:
            data['role']='Operations'
        elif self.user.is_admin == True:
            data['role']='Admin' 
        elif self.user.is_superuser == True:
            data['role']='Superuser' 
        # data['is_superuser'] = self.user.is_superuser       
       
        
       
        return data    

class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer