from django.urls import path
from . import views

urlpatterns = [
    path('', views.urun_list, name='urun_list'),
]