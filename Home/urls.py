from django.urls import path, include
from . import views
urlpatterns=[
            path('Home', views.Home, name="Home"),
            path('Info', views.Info, name="Info"),
            path('Transfer', views.Transfer, name="Transfer"),
            path('Transfer1', views.Transfer1, name="Transfer1"),   
            path('TranInfo', views.TranInfo, name="TranInfo")    
        ]