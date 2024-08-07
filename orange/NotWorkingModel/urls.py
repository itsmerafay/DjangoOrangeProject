from django.urls import path
from . import views


urlpatterns = [
    path('no-model-found/', views.no_model_found, name='no_model_found'),
    path('heating-area/', views.heating_area, name='heating_area'),
]