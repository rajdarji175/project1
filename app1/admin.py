from django.contrib import admin
from .models import UserTypeMaster,UserMaster

# class UserAdmin(admin.ModelAdmin):
# 	list_display=['UserName','UserPassword']
# 	list_filter=['UserName','UserEmail']
# 	search_fields=['UserPassword','UserEmail']
# 	ordering=['UserPassword','UserName']	

ModelField= lambda model: type('Subclass'+model.__name__,(admin.ModelAdmin,),{
	'list_display':[x.name for x in model._meta.fields],	
})

# Register your models here.

admin.site.register(UserTypeMaster,ModelField(UserTypeMaster))
admin.site.register(UserMaster,ModelField(UserMaster))
