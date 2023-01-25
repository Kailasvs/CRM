  
from django.contrib import admin
from leads.models import General_Information,Business_Category,Personal_Information
from django.contrib.auth.models import User,Group

# Remove Group and User Table in Admin Panel
# admin.site.unregister(User)
# admin.site.unregister(Group)


# View DB Table in Admin Panel
admin.site.register(General_Information)
admin.site.register(Business_Category)
admin.site.register(Personal_Information)
# ----------------------------------
# @admin.register(MyTableName)
# class MyTableName(admin.ModelAdmin):
#     list_display =  ['id','name']
        