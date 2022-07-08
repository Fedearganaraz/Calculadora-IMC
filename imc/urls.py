from django.urls import path
from imc.views import index

urlpatterns = [
    path("index/", index),
 ]