from django.urls import path
from . import views


urlpatterns = [
    path('address/', views.address_page, name='address_page'),
    
]
