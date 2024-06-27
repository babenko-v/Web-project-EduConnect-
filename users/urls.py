from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('',  views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration, name='registration'),
]
