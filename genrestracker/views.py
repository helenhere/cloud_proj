from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

"""
#from .models import Greeting
from .models import Car, Mileage, UserCar#, User#, Mileage, User,
from fuelconsumption.forms import NewCarForm, ChooseCar, AddMiles, LogIn#, AddMiles#, BaseForm, LogIn,
import datetime
from django.contrib.auth.models import User
from hashlib import sha1
from django.contrib.auth.hashers import check_password
from django.conf import settings

# Create your views here.


# def db(request):
#
#     greeting = Greeting()
#     greeting.save()
#
#     greetings = Greeting.objects.all()
#
#     return render(request, 'db.html', {'greetings': greetings})


def index(request):
    return render(request, 'index.html')


def addNewCar(request):
    if request.method == 'POST':
        form = NewCarForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            consumption = form.cleaned_data['consumption']

            newCar = Car.objects.create(brand_text=brand, model_text=model, consumption=consumption)
            newCar.setId()
            newCar.save()

            currentUserCars = UserCar.objects.filter(username=request.session['username'])
            if currentUserCars:
                currentUserCars[0].cars.add(newCar)
                currentUserCars[0].save()
            else:
                newCurrentUserCars = UserCar.objects.create(username=request.session['username'])
                newCurrentUserCars.cars.add(newCar)
                newCurrentUserCars.save()

            result = str(Car.objects.get(brand_text=brand, model_text=model, consumption=consumption)) + ' successfully added'
            #result
            #result = search[0].brand_text + ' ' + search[0].model_text + ': ' + str(search[0].consumption)
            #result = consumption * mileage / 100

            return render(request, 'result.html', {'result': result})
    else:
        form = NewCarForm()

    return render(request, 'addCar.html', {'form': form})


def chooseCar(request):
    if request.method == 'POST':
        form = ChooseCar(request.POST)
        if form.is_valid():
            car = form.cleaned_data['requiredCar']
            return HttpResponse(car)
            #return redirect(addMiles, car)

    else:
        #form = ChooseCar()
        #request.session['username']
        currentUserCars = UserCar.objects.filter(username=request.session['username'])
        if currentUserCars:
            carQuery = currentUserCars[0].cars.all()
        else:
            return render(request, 'redirectPage.html')
        #carQuery = Car.objects.all()
        form = '<label for="id_requiredCar">Choose your car:</label><select name="requiredCar" id="id_requiredCar">'

        for car in carQuery:
            form += '<option value="' + str(car) + '">' + str(car) + '</option>'

        form += '</select>'

    return render(request, 'chooseCar.html', {'form': form})

# def addMiles(request):#, carID):
#     return HttpResponse("ADD MILES")


def addMiles(request):#, carID):
    try: #for first run
        carID = request.POST.get('requiredCar')
        carID = carID.replace(' ', '').replace(':', '').replace('l.', '')
        #return HttpResponse("1111")
        carModel = Car.objects.get(identifier=carID)
        request.session['carID'] = carID
    except:
        carID = ''

    if request.method == 'POST':
        form = AddMiles(request.POST)
        if form.is_valid():
            carModel = Car.objects.get(identifier=request.session['carID'])
            miles = form.cleaned_data['mileage']

            track = Mileage(date=datetime.datetime.now(), distance=miles, liters=carModel.consumption * miles / 100)
            #track.auto.set(carModel)
            track.auto = carModel
            track.save()
            return render(request, 'result.html', {'result': str(carModel) + ' ' + str(miles)})
    else:
        form = AddMiles()

    return render(request, 'addMiles.html', {'car': str(carModel), 'form': form})
#
#
#

def login(request):
    if request.method == 'POST':
        form = LogIn(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                currentUser = User.objects.get(username=username)
            except:
                return HttpResponse('No user(')
            #return HttpResponse(currentUser.password)
            #_, salt, hashpw = currentUser.password.split('$')

            if currentUser.check_password(password):
                request.session['username'] = username

                return redirect('index/')#, username=username)
            else:
                return HttpResponse('Incorrect password')

    else:
        form = LogIn()

    return render(request, 'login.html', {'form': form})

#
# def login(request): #python manage.py createsuperuser
#     if request.method == 'POST':
#         form = LogIn(request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#
#             searchUser = User.objects.filter(username=username, password=password)
#
#             if searchUser:
#                 print("0")
#
#
#
#

#
#
def show(request):
    queryset = Mileage.objects.filter(auto__usercar__username=request.session['username'])
    cars = {}
    for carInfo in queryset:
        if not str(carInfo.auto) in cars:
            cars[str(carInfo.auto)] = (0, 0)

        distance = cars[str(carInfo.auto)][0] + carInfo.distance
        liters = cars[str(carInfo.auto)][1] + carInfo.liters

        cars[str(carInfo.auto)] = (distance, liters)

    summary = "<h3>Summary</h3>"
    for carSum in cars:
        summary += '<p>Car: %s</p>' % carSum
        summary += '<p>Sum distance: %s</p>' % cars[carSum][0]
        summary += '<p>Sum liters used: %s</p>' % cars[carSum][1]
        summary += '<hr>'

    return render(request, 'show.html', {'queryset': queryset, 'summary': summary})


"""