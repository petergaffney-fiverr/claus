from django.urls import path
from . import views

urlpatterns = [
    
    path('landing_page/', views.LandingPage.as_view(),name="landing_page"),
    path('', views.AfterPage.as_view(),name="index"),
    path('user/reg/mi/', views.Reg_mi.as_view(), name='reg'),
    path('user/reg/vi/', views.Reg_vi.as_view(), name='reg'),
    path('log/in/', views.Log_in.as_view(), name='log_in'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('email_check/', views.check_email, name='email_check'),


]