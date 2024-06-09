
from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [

    path('',  views.main_index, name='main'),
    path('about/', views.about, name='about'),
]
