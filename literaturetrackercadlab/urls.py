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
    #url(r'^db', genrestracker.views.db, name='db'),
    #url(r'^$', genrestracker.views.login, name='login'),
    path('admin/', admin.site.urls),
    url(r'^index/', genrestracker.views.index, name='index'),
    # url(r'^addCar/', genrestracker.views.addNewCar, name='addCar'),
    # url(r'^chooseCar/', genrestracker.views.chooseCar, name='chooseCar'),
    url(r'^show/', genrestracker.views.show, name='show'),
    # url(r'^addMiles/', genrestracker.views.addMiles, name='addMiles'), #/(.*.{0,})
    #
    url(r'^$', genrestracker.views.login, name='login'),
    url(r'^login/', genrestracker.views.login, name='login'),
    #url(r'^logout/$', genrestracker.views.logout, name='logout')
]
