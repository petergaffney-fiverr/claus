from django.contrib import messages, auth
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView, FormView, RedirectView
from .forms import *
from django.contrib.auth import views
from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate,login,logout,get_user
from django.template.loader import render_to_string,get_template
from .models import *
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.template import Context
from django.views.generic import CreateView,FormView,ListView,DetailView,DeleteView,UpdateView,TemplateView
from django.views import View
import json
from mieter.models import *


User = get_user_model()

#this class is for user login
class Log_in(View):
	template_name='landing_page.html'
	form_class=Loginform
	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			email=form.cleaned_data['email']
			password=form.cleaned_data['password']
			#check user authentication
			user=authenticate(email=email,password=password)
			#if successfully logged in
			if user:
				login(request,user)
				check='True'
				return HttpResponse(json.dumps(check), content_type="application/json")
			#if not successfully logged in
			else:
				check='False'
				return HttpResponse(json.dumps(check), content_type="application/json")
		else:
			check='False'
			return HttpResponse(json.dumps(check), content_type="application/json")


#for mieter registration
class Reg_mi(View):
	template_name='landing_page.html'
	form_class=CustomUserCreationForm

	def post(self,request):
		form=self.form_class(request.POST or None)

		if form.is_valid():

			user=form.save(commit=False)
			user.is_active=True
			user.save()
			login(self.request,user)
			messages.add_message(request,messages.SUCCESS,'account created succesfully')
			return HttpResponse("ok")
		return HttpResponse("wrong")

#for Vermieter registration
class Reg_vi(View):
	template_name='landing_page.html'
	form_class=CustomUserCreationForm
	def post(self,request):
		form=self.form_class(request.POST or None)
		if form.is_valid():

			user=form.save(commit=False)
			user.is_active=True
			user.save()
			login(self.request,user)
			messages.add_message(request,messages.SUCCESS,'account created succesfully')
			return redirect('index')
		return render(request,self.template_name, {'form': form})


#for logout
class LogoutView(views.LogoutView):
    next_page = reverse_lazy('landing_page')



class LandingPage(TemplateView):
	template_name='landing_page.html'
	def get(self,request,*args,**kwargs):
		#check if user is already logged in or nor
		if self.request.user.is_authenticated:
			return redirect('index')
		else:
			form_class=Loginform
			return render(request, self.template_name,{'form_class':form_class})

#this class is activate after successfully logged in
class AfterPage(LoginRequiredMixin, TemplateView):
	template_name='after_page.html'
	def get(self,request,*args,**kwargs):
		if self.request.user.role=='mieter':
			mieterpersons = Mieterperson.objects.filter(mieter=self.request.user)
			nebenmieters = Nebenmieter.objects.filter(mieter=self.request.user)
			wunschwohnungs = Wunschwohnung.objects.filter(mieter=self.request.user)
			documents = Documents.objects.filter(mieter=self.request.user)
			types = Type.objects.all()
			return render(request,'mieter_landing_page.html',{'mieterpersons': mieterpersons,
			 'nebenmieters': nebenmieters, 'wunschwohnungs': wunschwohnungs, 'documents': documents, 'types': types})
		return render(request, self.template_name)


#for email check whether the email is already registered or nor
def check_email(request):
	email=request.GET.get('email')
	check="False"
	if User.objects.filter(email=email,is_active=True).exists():

		check="True"
	return HttpResponse(json.dumps(check), content_type="application/json")



