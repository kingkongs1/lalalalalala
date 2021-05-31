from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('https://testbkj.azurewebsites.net/', include('catalog.urls')),
    path('', include('catalog.urls')),
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
