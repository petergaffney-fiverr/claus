from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Mieterperson)

admin.site.register(Nebenmieter)
admin.site.register(Beziehung)
admin.site.register(NebenmieterBeziehung)


admin.site.register(Wunschwohnung)

admin.site.register(Stadtteil)
admin.site.register(WunschwohnungStadtteil)

admin.site.register(Wohnungstyp)
admin.site.register(WunschwohnungWohnungstyp)

admin.site.register(Familienstand)
admin.site.register(MieterpersonFamilienstand)

admin.site.register(Documents)
admin.site.register(Type)
admin.site.register(DocumentsType)
