from django.urls import path
from teachers import views

app_name = 'teachers'

urlpatterns = [
    path('',  views.RosterView.as_view(), name='roster'),
    path('search/',  views.RosterView.as_view(), name='search'),
    path('forms/<int:mentors_id>/', views.MentorView.as_view(), name='mentors'),
]
