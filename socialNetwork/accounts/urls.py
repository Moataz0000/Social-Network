from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('sign-up/', views.SignUp, name='sign-up'),
    path('sign-in/', views.SignIn, name='sign-in'),
    path('sign-out/', views.SignOut, name='sign-out'),
    path('profile/', views.profile, name='profile'),
]