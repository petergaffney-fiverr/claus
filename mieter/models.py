import uuid
import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Mieterperson(models.Model):
	BOOL_CHOICES = ((None, 'N/A'), (True, 'Yes'), (False, 'No'))
	mieter = models.ForeignKey(User, on_delete=models.CASCADE)

	# Identity
	nachname = models.CharField(max_length=50, null=True, blank=True, default=None)
	vorname = models.CharField(max_length=50, null=True, blank=True, default=None)
	# familienstand = models.CharField(max_length=50, default=None)
	geburtsdatum = models.DateField(null=True, blank=True, default=None)

	# Address
	anschrift_strasse = models.CharField(max_length=50, null=True, blank=True, default=None)
	anschrift_hausnummer = models.CharField(max_length=50, null=True, blank=True, default=None)
	anschrift_plz = models.CharField(max_length=5, null=True, blank=True, default=None)
	anschrift_stadt = models.CharField(max_length=50, null=True, blank=True, default=None)

	telefonnummer = models.CharField(max_length=30, default=None, null=True, blank=True)

	# Job
	beruf = models.CharField('Ausgeübter Beruf', max_length=50, null=True, blank=True, default=None)
	einkommen = models.IntegerField('Mtl. Nettoeinkommen', null=True, blank=True, default=None)

	# Current employer
	arbeitgeber_name = models.CharField('Dezeitiger Arbeitgeber', max_length=50, null=True, blank=True, default=None)
	arbeitgeber_anschrift = models.CharField(max_length=100, null=True, blank=True, default=None)
	arbeitgeber_telefonnummer = models.CharField(max_length=30, null=True, blank=True, default=None)
	arbeitsgeber_datum_besch = models.DateField( null=True, blank=True,default=None)

	arbeitgeber_festanstellung = models.BooleanField(choices=BOOL_CHOICES, null=True, blank=True,  default=None)
	arbeitgeber_probezeit = models.BooleanField(choices=BOOL_CHOICES, null=True, blank=True,  default=None)

	# Current landlord
	vermieter_name = models.CharField(max_length=100, null=True, blank=True, default=None)
	vermieter_anschrift = models.CharField(max_length=100, null=True, blank=True, default=None)
	vermieter_telefonnummer = models.CharField(max_length=30, null=True, blank=True, default=None)

	# Questions
	mietrueckstellungen = models.BooleanField('Bestehen Mietrückstände aus bisherigen Mietverhältnissen?', choices=BOOL_CHOICES, null=True, blank=True,  default=None)
	raeumungsklage = models.BooleanField('In den letzten fünf Jahren wurde Räumungsklage gegen mich erhoben', choices=BOOL_CHOICES, null=True, blank=True, default=None)
	raeumungsklage_date = models.DateField(null=True, blank=True)
	zwangsvollstraeckung = models.BooleanField('In den letzten fünf Jahren wurde Zwangsvollstreckung gegen mich eingeleitet', choices=BOOL_CHOICES, null=True, blank=True, default=None)
	zwangsvollstraeckung_date = models.DateField(null=True, blank=True)
	eid_versicherung = models.BooleanField('In den letzten fünf Jahren habe ich eine eidesstattliche Versicherung abgegeben', choices=BOOL_CHOICES, null=True, blank=True, default=None)
	eid_versicherung_date = models.DateField(null=True, blank=True)
	insolvenzverfahren = models.BooleanField('In den letzten fünf Jahren wurde ein Insolvenzverfahren gegen mich eröffnet', choices=BOOL_CHOICES, null=True, blank=True, default=None)
	insolvenzverfahren_date = models.DateField(null=True, blank=True)
	vorstrafen = models.BooleanField('Vorstrafen / Haftbefehl', choices=BOOL_CHOICES, null=True, blank=True, default=None)
	vorstrafen_date = models.DateField(null=True, blank=True)
	sozialleistungen = models.BooleanField('Ich beziehe Sozialleistungen zur Zahlung der Miete / Kaution', choices=BOOL_CHOICES,null=True, blank=True, default=None)
	sozialleistungen_beschreibung = models.CharField('Welche und in welchem Umfang', max_length=200,null=True, blank=True, default=None)
	gewerbliche_nutzung = models.BooleanField('Ist einge gewerbliche Nutzung der Wohnung beabsichtigt?', choices=BOOL_CHOICES,null=True, blank=True, default=None)
	gewerbliche_nutzung_zweck = models.CharField('Zweck angeben', max_length=200,null=True, blank=True, default=None)
	tierhaltung = models.BooleanField('Tierhaltung beabsichtigt', choices=BOOL_CHOICES,null=True, blank=True, default=None)
	tierhaltung_beschreibung = models.CharField('Tierart / Rasse', max_length=200,null=True, blank=True, default=None)

	def __str__(self):
		return f"{self.vorname} {self.nachname}"


class Familienstand(models.Model):
	familienstand = models.CharField(max_length=200)

	class Meta:
		ordering = ('familienstand',)
	def __str__(self):
		return f"{self.familienstand}"

class MieterpersonFamilienstand(models.Model):
	mieterperson = models.ForeignKey(Mieterperson, on_delete=models.CASCADE)
	familienstand = models.ForeignKey(Familienstand, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.mieterperson.pk} {self.familienstand.familienstand}"



# All about Nebenmieter form
class Beziehung(models.Model):
	beziehung = models.CharField(max_length=200)
	class Meta:
		ordering = ('beziehung',)

	def __str__(self):
		return f"{self.beziehung}"

class Nebenmieter(models.Model):
	mieter = models.ForeignKey(User, on_delete=models.CASCADE)
	nachname = models.CharField(max_length=50,null=True, blank=True, default='')
	vorname = models.CharField(max_length=50,null=True, blank=True, default='')
	geburtsdatum = models.DateTimeField(auto_now_add=False,null=True, blank=True)

	def __str__(self):
		return f"{self.pk} {self.vorname} {self.nachname}"

class NebenmieterBeziehung(models.Model):
	nebenmieter = models.ForeignKey(Nebenmieter, on_delete=models.CASCADE)
	beziehung = models.ForeignKey(Beziehung, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.nebenmieter.pk} {self.beziehung.beziehung}"


class Wunschwohnung(models.Model):
	BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
	mieter = models.ForeignKey(User, on_delete=models.CASCADE)

	# Most important information
	max_miete = models.IntegerField('Maximale Kaltmiete pro Monat', default=None,null=True, blank=True)
	flaeche = models.CharField('Wohnfläche ab',max_length=250, default=None,null=True, blank=True)
	anzahl_zimmer = models.FloatField('Anzahl der Zimmer ab', default=None,null=True, blank=True)
	bezugsfertig = models.DateField('Bezugsfertig ab', default=None,null=True, blank=True)

	# Location
	land = models.CharField('Land', max_length=50, default='Deutschland',null=True, blank=True)
	stadt = models.CharField('Stadt', max_length=50, default='München',null=True, blank=True)

	# Furnishing
	balkon_terrasse = models.BooleanField('Balkon / Terrasse', default=None)
	barrierefrei = models.BooleanField('Barrierefrei', default=None)
	haustiere = models.BooleanField('Haustiere erlaubt', default=None)
	garage_stellplatz = models.BooleanField('Garage / Stellplatz', default=None)
	einbaukueche = models.BooleanField('Einbauküche', default=None)
	keller = models.BooleanField('Keller', default=None)
	gaeste_wc = models.BooleanField('Gäste-WC', default=None)

	aktiv = models.BooleanField('Gibt an, ob Gesuch aktiv ist', choices=BOOL_CHOICES, null=True, blank=True, default=False)

	def __str__(self):
		return f"{self.pk} {self.mieter.email}"

class Stadtteil(models.Model):
	stadtteil = models.CharField(max_length=200)
	class Meta:
		ordering = ('stadtteil',)

	def __str__(self):
		return f"{self.stadtteil}"

class WunschwohnungStadtteil(models.Model):
	wunschwohnung = models.ForeignKey(Wunschwohnung, on_delete=models.CASCADE)
	stadtteil = models.ForeignKey(Stadtteil, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.wunschwohnung.pk} {self.stadtteil.stadtteil}"

class Wohnungstyp(models.Model):
	wohnungstyp = models.CharField(max_length=200)
	class Meta:
		ordering = ('wohnungstyp',)

	def __str__(self):
		return f"{self.wohnungstyp}"

class WunschwohnungWohnungstyp(models.Model):
	wunschwohnung = models.ForeignKey(Wunschwohnung, on_delete=models.CASCADE)
	wohnungstyp = models.ForeignKey(Wohnungstyp, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.wunschwohnung.pk} {self.wohnungstyp.wohnungstyp}"



class Documents(models.Model):
    mieter = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()

class Type(models.Model):
	type = models.CharField(max_length=200)
	class Meta:
		ordering = ('type',)

	def __str__(self):
		return f"{self.type}"

class DocumentsType(models.Model):
	documents = models.ForeignKey(Documents, on_delete=models.CASCADE)
	type = models.ForeignKey(Type, on_delete=models.CASCADE)
	def __str__(self):
		return f"{self.documents.pk} {self.type.type}"