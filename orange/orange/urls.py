from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WorkingModel.urls')),
    path('', include('Address.urls')),
    path('', include('NotWorkingModel.urls')),
] 
        
if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
