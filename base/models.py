from django.db import models
from django.contrib.auth.models import User

# Erstellen Sie hier Ihre model.

class Liste(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=30, verbose_name = "Titel")
    item1 = models.CharField(max_length=30, blank=True, verbose_name = "1")
    preis1 = models.DecimalField(max_digits=5, decimal_places=2, default = 0, verbose_name = "Preis")
    item2 = models.CharField(max_length=30, blank=True, verbose_name = "2")
    preis2 = models.DecimalField(max_digits=5, decimal_places=2, default = 0, verbose_name = "Preis")
    item3 = models.CharField(max_length=30, blank=True, verbose_name = "3")
    preis3 = models.DecimalField(max_digits=5, decimal_places=2, default = 0, verbose_name = "Preis")
    item4 = models.CharField(max_length=30, blank=True, verbose_name = "4")
    preis4 = models.DecimalField(max_digits=5, decimal_places=2, default = 0, verbose_name = "Preis")
    item5 = models.CharField(max_length=30, blank=True, verbose_name = "5")
    preis5 = models.DecimalField(max_digits=5, decimal_places=2, default = 0, verbose_name = "Preis")

    @property
    def rate(self):
        total = (self.preis1) + (self.preis2) + (self.preis3) + (self.preis4) + (self.preis5)   
        return total

    def __str__(self):    
        return self.title    


        

