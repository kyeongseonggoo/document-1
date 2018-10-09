from django.db import models

class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)
    age1 = models.IntegerField(blank=True)
    age2 = models.IntegerField(null=True)
    age3 = models.IntegerField(blank=True, null=True)