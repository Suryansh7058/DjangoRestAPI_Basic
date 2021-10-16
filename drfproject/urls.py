from os import name
from django.contrib import admin
from django.urls import path, include
from .views import TestView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain')
]
