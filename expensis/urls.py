from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "expensis"),
    path('add-expensis', views.add_expensis, name = 'add-expensis'),
]