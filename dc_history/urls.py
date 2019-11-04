from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getDynastyList', views.getDynastyList, name='getDynastyList'),
    path('saveDynasty', views.saveDynasty, name='saveDynasty'),
]
