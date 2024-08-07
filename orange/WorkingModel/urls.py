from django.urls import path
from . import views


urlpatterns = [
    path('model-page-one/', views.model_page_one, name='model_page_one'),
    path('delete-model-page/', views.delete_model_page, name='delete_model_page'),
    path('customize-window-planner/', views.customize_window_planner, name='customize_window_planner'),
    path('general-info/', views.general_info, name='general_info'), 
    path('expansion-and-cultivation/', views.expansion_and_cultivation, name='expansion_and_cultivation'), 
    path('thermal-cover/', views.thermal_cover, name='thermal_cover'), 
    

]
