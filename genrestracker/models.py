from django.db import models

class Genre(models.Model):
    genreName = models.CharField(max_length=140)

    def __str__(self):
        return self.genreName
#
#
class UserGenre(models.Model):
    username = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    pages = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return '%s - %s - %s pages (%s)' % \
               (self.username, str(self.genre), str(self.pages), self.date.strftime('%d %B %Y - %H:%M:%S'))

# Create your models here.
# class Greeting(models.Model):
#     when = models.DateTimeField('date created', auto_now_add=True)

#
# class Car(models.Model):
#     brand_text = models.CharField(max_length=80)
#     model_text = models.CharField(max_length=90)
#     consumption = models.FloatField(max_length=3, null=False)
#     identifier = models.CharField(max_length=175, null=False)
#
#     def setId(self):
#         self.identifier = self.brand_text + self.model_text + str(self.consumption)
#
#     def __str__(self):
#         return self.brand_text+' '+self.model_text+': '+str(self.consumption)+' l.'
#
#
# class UserCar(models.Model):
#     username = models.CharField(max_length=200)
#     cars = models.ManyToManyField(Car)
#
#     def __str__(self):
#         return self.username + " (" + str(self.cars.count()) + ")"
# #
# #
# class Mileage(models.Model):
#     date = models.DateField()
#     distance = models.FloatField(max_length=6, null=False)
#     liters = models.FloatField(max_length=3, null=False)
#     auto = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return str(self.auto) + " " + str(self.distance) + " km.  " + str(self.liters) + " liters used"
