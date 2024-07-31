from django.urls import path
from . import views

urlpatterns = [
    path('',views.semmarks,name='semmarks'),
    path('getmarks',views.getmarks,name='getmarks')
]
