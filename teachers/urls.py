from django.urls import path
from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('',  views.roster, name='roster'),
    path('search/',  views.roster, name='search'),
    path('forms/<int:mentors_id>/', views.MentorView.as_view(), name='mentors'),
]
