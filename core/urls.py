from django.urls import path
from . import views

urlpatterns = [
    #homepage
    path('', views.chart, name='chart')
    
    #template for a new page to redirect to
    #path('plot1/', views.plot1, name='plot1')
]