from django import forms
#from .models import Car
#from .getInfoFromModel import getAllCars
#
# class BaseForm(forms.Form):
#     brand = forms.CharField(label='Brand', max_length=80)
#     model = forms.CharField(label='Model', max_length=80)
#     #consumption = forms.FloatField(label='Consumption')
#     #mileage = forms.FloatField(label='Mileage')
#

class NewUserGenre(forms.Form):
    genre = forms.CharField(label='Choose genre:', widget=forms.Select(choices=[('first', 'first'), ('second', 'second'), ('third', 'third')]))
    pages = forms.IntegerField(label='Pages count')


class NewCarForm(forms.Form):
    brand = forms.CharField(label='Brand', max_length=80)
    model = forms.CharField(label='Model', max_length=80)
    consumption = forms.FloatField(label='Consumption')


# class ChooseCar(forms.Form):
#
#     def getCars(self):
#         carQuery = Car.objects.all()
#         carChoices = []
#         for car in carQuery:
#             carChoices.append((car.identifier, str(car)))
#         return carChoices
#
#
#     def __init__(self, *args, **kwargs):
#         super(ChooseCar, self).__init__(*args, **kwargs)
#         self.fields['requiredCar'] = forms.CharField(label='Choose your car:', widget=forms.Select(choices=self.getCars()))
#
#
class LogIn(forms.Form):
    username = forms.CharField(label='Username', max_length=80)
    password = forms.CharField(label='Password', max_length=80)
#
#
# class SearchMileage(forms.Form):
#     mileage = forms.FloatField(label='Mileage')
#
#

#
#
class AddMiles(forms.Form):
    mileage = forms.FloatField(label='Mileage')
