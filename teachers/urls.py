from django.urls import path
from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('',  views.roster, name='roster'),

    path('forms/<int:mentors_id>/', views.mentors, name='mentors'),
]
