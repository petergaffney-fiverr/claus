from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import ListView, TemplateView
from django.views.generic import FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect,HttpResponse
import json

# Create your views here.


class MieterpersonCreateFormView(LoginRequiredMixin, FormView):
	template_name = 'mieterperson_form.html'
	form_class = MieterpersonForm
	def get(self,request,*args,**wargs):
		familienstands = Familienstand.objects.all()
		return render(request,self.template_name, {'form': self.form_class, 'familienstands': familienstands})

	def post(self, request, *args, **kargs):
		form = self.form_class(self.request.POST)

		familienstands = self.request.POST.getlist("familienstands")

		if form.is_valid():
			data = form.save(commit=False)
			data.mieter = self.request.user
			data.save()
			for familienstand in familienstands:
				MieterpersonFamilienstand.objects.create(mieterperson=data, familienstand=Familienstand.objects.get(pk=familienstand))
			return redirect('/')

		return redirect('/')

class MieterpersonUpdateFormView(LoginRequiredMixin, UpdateView):
	template_name = 'mieterperson_update_form.html'
	model = Mieterperson

	#control the user permission for manipulate the data
	def dispatch(self, request, *args, **kwargs):
		handler = super().dispatch(request, *args, **kwargs)
		user = request.user
		post = self.get_object()
		if not (post.mieter == user):
			return redirect('/')
		return handler

	def get(self,request,*args,**wargs):
		familienstands = Familienstand.objects.all()
		form_class = MieterpersonForm(instance=self.get_object())
		return render(request,self.template_name, {'form': form_class, 'information': self.get_object(), 'familienstands': familienstands})

	def post(self, request, *args, **kargs):
		form = MieterpersonForm(request.POST or None, instance=self.get_object())

		familienstands_ = self.request.POST.getlist("familienstands")

		if form.is_valid():
			data = form.save(commit=False)
			data.save()
			familienstands = Familienstand.objects.all()
			for familienstand in familienstands:
				if str(familienstand.pk) in familienstands_:
					if not MieterpersonFamilienstand.objects.filter(mieterperson=data, familienstand=familienstand).exists():
						MieterpersonFamilienstand.objects.create(mieterperson=data, familienstand=familienstand)
				else:
					if MieterpersonFamilienstand.objects.filter(mieterperson=data, familienstand=familienstand).exists():
						MieterpersonFamilienstand.objects.get(mieterperson=data, familienstand=familienstand).delete()
			return redirect('/')
		return redirect('/')

class MieterpersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Mieterperson
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
    	pk = self.kwargs['pk']
    	mieterperson = Mieterperson.objects.get(pk=pk)
    	if mieterperson.mieter != self.request.user:
    		return redirect('/')
    	return self.post(request, *args, **kwargs)

class NebenmieterCreateFormView(LoginRequiredMixin, FormView):
	template_name = 'nebenmieter_form.html'
	form_class = NebenmieterForm
	def get(self,request,*args,**wargs):
		beziehungs = Beziehung.objects.all()
		return render(request,self.template_name, {'form': self.form_class, 'beziehungs': beziehungs})

	def post(self, request, *args, **kargs):
		form = self.form_class(self.request.POST)

		beziehungs = self.request.POST.getlist("beziehung")

		if form.is_valid():
			data = form.save(commit=False)
			data.mieter = self.request.user
			data.save()
			for beziehung in beziehungs:
				NebenmieterBeziehung.objects.create(nebenmieter=data, beziehung=Beziehung.objects.get(pk=beziehung))
			return redirect('/')

		return redirect('/')


class NebenmieterUpdateFormView(LoginRequiredMixin, UpdateView):
	template_name = 'nebenmieter_update_form.html'
	model = Nebenmieter

	#control the user permission for manipulate the data
	def dispatch(self, request, *args, **kwargs):
		handler = super().dispatch(request, *args, **kwargs)
		user = request.user
		post = self.get_object()
		if not (post.mieter == user):
			return redirect('/')
		return handler

	def get(self,request,*args,**wargs):
		beziehungs = Beziehung.objects.all()
		form_class = NebenmieterForm(instance=self.get_object())
		return render(request,self.template_name, {'form': form_class, 'information': self.get_object(), 'beziehungs': beziehungs})

	def post(self, request, *args, **kargs):
		form = NebenmieterForm(request.POST or None, instance=self.get_object())

		beziehungs_ = self.request.POST.getlist("beziehung")
		print(beziehungs_)

		if form.is_valid():
			data = form.save(commit=False)
			data.save()
			beziehungs = Beziehung.objects.all()
			for beziehung in beziehungs:
				if str(beziehung.pk) in beziehungs_:
					if not NebenmieterBeziehung.objects.filter(nebenmieter=data, beziehung=beziehung).exists():
						NebenmieterBeziehung.objects.create(nebenmieter=data, beziehung=beziehung)
				else:
					if NebenmieterBeziehung.objects.filter(nebenmieter=data, beziehung=beziehung).exists():
						NebenmieterBeziehung.objects.get(nebenmieter=data, beziehung=beziehung).delete()
			return redirect('/')

class NebenmieterDeleteFormView(LoginRequiredMixin, DeleteView):
    model = Nebenmieter
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
    	pk = self.kwargs['pk']
    	nebenmieter = Nebenmieter.objects.get(pk=pk)
    	if nebenmieter.mieter != self.request.user:
    		return redirect('/')
    	return self.post(request, *args, **kwargs)

class WunschwohnungCreateFormView(LoginRequiredMixin, FormView):
	template_name = 'wunschwohnung_form.html'
	form_class = WunschwohnungForm
	def get(self,request,*args,**wargs):
		stadtteils = Stadtteil.objects.all()
		wohnungstyps = Wohnungstyp.objects.all()
		return render(request,self.template_name, {'form': self.form_class, 'stadtteils': stadtteils, 'wohnungstyps': wohnungstyps})

	def post(self, request, *args, **kargs):
		form = self.form_class(self.request.POST)

		stadtteils = self.request.POST.getlist("stadtteil")
		wohnungstyps = self.request.POST.getlist("wohnungstyp")

		if form.is_valid():
			data = form.save(commit=False)
			data.mieter = self.request.user
			data.save()

			for stadtteil in stadtteils:
				WunschwohnungStadtteil.objects.create(wunschwohnung=data, stadtteil=Stadtteil.objects.get(pk=stadtteil))

			for wohnungstyp in wohnungstyps:
				WunschwohnungWohnungstyp.objects.create(wunschwohnung=data, wohnungstyp=Wohnungstyp.objects.get(pk=wohnungstyp))
			return redirect('/')

		return redirect('/')

class WunschwohnungUpdateFormView(LoginRequiredMixin, UpdateView):
	template_name = 'wunschwohnung_update_form.html'
	model = Wunschwohnung

	#control the user permission for manipulate the data
	def dispatch(self, request, *args, **kwargs):
		handler = super().dispatch(request, *args, **kwargs)
		user = request.user
		post = self.get_object()
		if not (post.mieter == user):
			return redirect('/')
		return handler

	def get(self,request,*args,**wargs):
		stadtteils = Stadtteil.objects.all()
		wohnungstyps = Wohnungstyp.objects.all()
		form_class = WunschwohnungForm(instance=self.get_object())
		return render(request,self.template_name, {'form': form_class, 'information': self.get_object(), 'stadtteils': stadtteils, 'wohnungstyps': wohnungstyps})

	def post(self, request, *args, **kargs):
		form = WunschwohnungForm(request.POST or None, instance=self.get_object())

		stadtteils_ = self.request.POST.getlist("stadtteil")
		wohnungstyp_ = self.request.POST.getlist("wohnungstyp")
		# print(beziehungs_)

		if form.is_valid():
			data = form.save(commit=False)
			data.save()

			stadtteils = Stadtteil.objects.all()
			for stadtteil in stadtteils:
				if str(stadtteil.pk) in stadtteils_:
					if not WunschwohnungStadtteil.objects.filter(wunschwohnung=data, stadtteil=stadtteil).exists():
						WunschwohnungStadtteil.objects.create(wunschwohnung=data, stadtteil=stadtteil)
				else:
					if WunschwohnungStadtteil.objects.filter(wunschwohnung=data, stadtteil=stadtteil).exists():
						WunschwohnungStadtteil.objects.get(wunschwohnung=data, stadtteil=stadtteil).delete()
			
			wohnungstyps = Wohnungstyp.objects.all()
			for wohnungstyp in wohnungstyps:
				if str(wohnungstyp.pk) in wohnungstyp_:
					if not WunschwohnungWohnungstyp.objects.filter(wunschwohnung=data, wohnungstyp=wohnungstyp).exists():
						WunschwohnungWohnungstyp.objects.create(wunschwohnung=data, wohnungstyp=wohnungstyp)
				else:
					if WunschwohnungWohnungstyp.objects.filter(wunschwohnung=data, wohnungstyp=wohnungstyp).exists():
						WunschwohnungWohnungstyp.objects.get(wunschwohnung=data, wohnungstyp=wohnungstyp).delete()

			return redirect('/')

class WunschwohnungDeteleView(LoginRequiredMixin, DeleteView):
    model = Wunschwohnung
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
    	pk = self.kwargs['pk']
    	wunschwohnung = Wunschwohnung.objects.get(pk=pk)
    	#if the authenticate user is not the owner then he can't access it
    	if wunschwohnung.mieter != self.request.user:
    		return redirect('/')
    	return self.post(request, *args, **kwargs)


class DocumentsSaveView(LoginRequiredMixin, FormView):
	form_class = DocumentsForm

	def post(self, request, *args, **kargs):
		file = self.request.FILES.get('file')
		types = self.request.POST.getlist("type")

		doc = Documents.objects.create(mieter=self.request.user, file=file)
		for types in types:
			DocumentsType.objects.create(documents=doc, type=Type.objects.get(pk=types))
		return redirect('/')


class DocumentDeteleView(LoginRequiredMixin, DeleteView):
    model = Documents
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
    	pk = self.kwargs['pk']
    	documents = Documents.objects.get(pk=pk)
    	#if the authenticate user is not the owner then he can't access it
    	if documents.mieter != self.request.user:
    		return redirect('/')
    	return self.post(request, *args, **kwargs)

class UpdateActiveInactive(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		wunschwohnungid = self.request.GET.get('wunschwohnungid')
		btn = self.request.GET.get('btn')
		print(wunschwohnungid)
		print(btn)
		if btn:
			check = 0
		else:
			check = 1
		BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
		wunschwohnung = Wunschwohnung.objects.get(pk=wunschwohnungid)
		wunschwohnung.aktiv=BOOL_CHOICES[int(check)][0]
		wunschwohnung.save()
		
		return HttpResponse(json.dumps("ok"), content_type="application/json")

class MatchesView(LoginRequiredMixin, TemplateView):
	template_name = 'matches.html'