from django.db import models

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, unique=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'country'
        ordering = ['country']

    def str(self):
        return self.country
    

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'city'
        ordering = ['city']

    def __str__(self):
        return self.city
    