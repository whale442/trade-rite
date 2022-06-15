from django.urls import path

from .import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('activation/<slug:uidb64>/<slug:token>/',views.activate,name='activate'),
]