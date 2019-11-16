
from django.urls import path
from .views import sign_up as r , sign_in as s , logout as l

urlpatterns=[
    path('register',r,name='register' ),
    path('login', s, name='login' ),
    path('logout',l,name ='logout')

]
