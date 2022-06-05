from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('signa', views.signa, name='signa'),
    path('signd', views.signd, name='signd'),
    path('home2',views.home2,name='patient'),
    path('signn', views.signn, name='signn'),
     path('home1',views.home1,name='patient'),
    path('signp', views.signp, name='signp'),
    path('home',views.home,name='patient'),
    path('signp', views.signp, name='signp'),
    path('doctor', views.doctor,name='doctor'),
    path('nurse', views.nurse,name='nurse'),
    path('patient' ,views.patient,name='patient'),
    path('appointment' ,views.appointment,name='appointment'),
    path('appointmentp', views.appointmentp, name='appointmentp'),
]