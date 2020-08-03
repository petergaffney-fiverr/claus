from django.urls import path
from .views import *

urlpatterns = [

    #mieterperson
    path('create/mieterperson/', MieterpersonCreateFormView.as_view(),name="mieterperson_create"),
    path('update/mieterperson/<pk>', MieterpersonUpdateFormView.as_view(),name="mieterperson_update"),
    path('detele/mieterperson/<pk>', MieterpersonDeleteView.as_view(),name="mieterperson_delete"),
    #nebenmieter
    path('create/nebenmieter/', NebenmieterCreateFormView.as_view(),name="nebenmieter_create"),
    path('update/nebenmieter/<pk>', NebenmieterUpdateFormView.as_view(),name="nebenmieter_update"),
    path('detele/nebenmieter/<pk>', NebenmieterDeleteFormView.as_view(),name="nebenmieter_detele"),

    #wunschwohnung
    path('create/wunschwohnung/', WunschwohnungCreateFormView.as_view(),name="wunschwohnung_create"),
    path('update/wunschwohnung/<pk>', WunschwohnungUpdateFormView.as_view(),name="wunschwohnung_update"),
    path('detele/wunschwohnung/<pk>', WunschwohnungDeteleView.as_view(),name="wunschwohnung_detele"),

    path('detele/document/<pk>', DocumentDeteleView.as_view(),name="document_detele"),

    path('save/document/', DocumentsSaveView.as_view(),name="document_save"),
    path('update/active_inactive/', UpdateActiveInactive.as_view(),name="update_active_inactive"),
    path('matches/', MatchesView.as_view(),name="matches"),

]