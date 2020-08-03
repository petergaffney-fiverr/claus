from django import template
from mieter.models import *

register = template.Library()

@register.simple_tag()
def check_Nebenmieter_Beziehung_select(nebenmieter, beziehung):
	try:
		return NebenmieterBeziehung.objects.get(nebenmieter=nebenmieter, beziehung=beziehung )
	except:
		pass
	return None


@register.simple_tag()
def check_Wunschwohnung_Stadtteil_select(wunschwohnung, stadtteil):
	try:
		return WunschwohnungStadtteil.objects.get(wunschwohnung=wunschwohnung, stadtteil=stadtteil )
	except:
		pass
	return None

@register.simple_tag()
def check_Wunschwohnung_Wohnungstyp_select(wunschwohnung, wohnungstyp):
	try:
		return WunschwohnungWohnungstyp.objects.get(wunschwohnung=wunschwohnung, wohnungstyp=wohnungstyp )
	except:
		pass
	return None
	
@register.simple_tag()
def check_Mieterperson_Familienstand_select(mieterperson, familienstand):
	try:
		return MieterpersonFamilienstand.objects.get(mieterperson=mieterperson, familienstand=familienstand )
	except:
		pass
	return None