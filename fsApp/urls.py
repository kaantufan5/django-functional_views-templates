from django.urls import path
from fsApp.views import home

urlpatterns = [
    path('', home, name='home')
]
