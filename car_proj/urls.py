"""car_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from car_app.views import multi_step_form, AddressCreateView, CustomerCreateView, CarCreateView, AllDataView
from django.views.generic import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('form/', multi_step_form, name='multi_step_form'),
    path('api/address/', AddressCreateView.as_view(), name='address-create'),
    path('api/customer/', CustomerCreateView.as_view(), name='customer-create'),
    path('api/car/', CarCreateView.as_view(), name='car-create'),
    path('api/data/', AllDataView.as_view(), name='all-data'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
