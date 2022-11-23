from django.urls import path
from dsApp.views import home

urlpatterns = [
    path('', home, name='home')
]
