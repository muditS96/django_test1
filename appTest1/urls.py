from django.urls import path

from . import views
# ise banana padta hai 
# project ka url pehle se hi hota hai usme hum app ka url include karte hai
urlpatterns=[
     path('patdetails',views.PatDetails,name='patientdetails'), 
    path('register',views.add,name='register'), 
    path('',views.showall,name='login')
    # path('login',views.login,name='login')
]
