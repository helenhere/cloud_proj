"""literaturetrackercadlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
import genrestracker.views

admin.autodiscover()

urlpatterns = [
    #url(r'^db', fuelconsumption.views.db, name='db'),
    #url(r'^$', fuelconsumption.views.login, name='login'),
    path('admin/', admin.site.urls),
    # url(r'^index/', fuelconsumption.views.index, name='index'),
    # url(r'^addCar/', fuelconsumption.views.addNewCar, name='addCar'),
    # url(r'^chooseCar/', fuelconsumption.views.chooseCar, name='chooseCar'),
    # url(r'^show/', fuelconsumption.views.show, name='show'),
    # url(r'^addMiles/', fuelconsumption.views.addMiles, name='addMiles'), #/(.*.{0,})
    #
    # url(r'^$', fuelconsumption.views.login, name='login'),
    # url(r'^login/', fuelconsumption.views.login, name='login'),
    #url(r'^logout/$', fuelconsumption.views.logout, name='logout')
]
