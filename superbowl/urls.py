from django.urls import path
from . import views

app_name = 'superbowl'
urlpatterns = [
    path('', views.index, name='index'),
    path('allData', views.allData, name='allData'),
    path('getAirtableData', views.getAirtableData, name='getAirtableData'),
    path('chart', views.chart, name='chart')
]