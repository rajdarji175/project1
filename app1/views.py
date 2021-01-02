from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserTypeMaster,UserMaster
from .forms import LoginForms,RegisterForms
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

def home(request):
	data1=UserMaster.objects.all()
	print('data1:',data1)
	data2=UserMaster.objects.filter(UserTypeID=1).values()
	print('data2:',data2)
	data3=UserMaster.objects.filter(UserTypeID__UserType='student')
	print('data3:',data3)
	data4=UserMaster.objects.filter(UserTypeID=1).values()
	print('data4:',data4)
	data5=UserMaster.objects.filter(UserTypeID=1).values('UserName','UserTypeID__UserType')
	print('data5:',data5)
	data6=UserMaster.objects.filter(UserTypeID=1).values('UserName','UserTypeID__UserType')[0]['UserName']
	print('data6:',data6)
	return render(request,'base.html',context={'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6})

def login(request,pk):
	msg=''
	form=LoginForms(request.POST or None)
	if request.POST:
		if UserMaster.objects.filter(UserEmail=request.POST['UserEmail'],UserPassword=request.POST['UserPassword']).exists():
			return render(request,'base.html')
		else:
			msg=form.errors
	return render(request,'login.html',context={'form':form,'msg':msg})

def register(request):
	#print('GET:',request.GET)
	#print('POST:',request.POST)
	reg_form=RegisterForms(request.POST)
	#print('form:',reg_form)
	if request.POST:
		if not UserMaster.objects.filter(UserEmail=request.POST['UserEmail']).exists():
			data7=UserMaster.objects.create(UserName=request.POST['UserName'],UserPassword=request.POST['UserPassword'],UserMobile=request.POST['UserMobile'],UserEmail=request.POST['UserEmail'])
			return render(request,'login.html')
	return render(request,'register.html',context={'reg_form':reg_form})

class viewuser(APIView):
	def post(self,request):
		UserData=UserMaster.objects.all().values()
		return Response({'response':UserData})

