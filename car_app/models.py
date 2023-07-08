from django.db import models

class Address(models.Model):
    street_name = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)

    def __str__(self):
        return self.street_name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Car(models.Model):
    MANUFACTURERS = (
        ('Lamborghini', 'Lamborghini'),
        ('Koenigsegg', 'Koenigsegg'),
        ('Ferrari', 'Ferrari'),
    )
    MODELS = (
        ('Aventador', 'Aventador'),
        ('Gallardo', 'Gallardo'),
        ('Murcielago', 'Murcielago'),
        ('Agera', 'Agera'),
        ('Jesko', 'Jesko'),
        ('One:1', 'One:1'),
        ('La Ferrari', 'La Ferrari'),
        ('Stradale', 'Stradale'),
        ('F40', 'F40'),
    )
    COLORS = (
        ('Black', 'Black'),
        ('White', 'White'),
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Orange', 'Orange'),
        ('Yellow', 'Yellow'),
    )
    model_name = models.CharField(max_length=20, choices=MODELS)
    manufacturer = models.CharField(max_length=20, choices=MANUFACTURERS)
    color = models.CharField(max_length=20, choices=COLORS)
    manufacturing_date = models.DateTimeField()

    def __str__(self):
        return f'{self.manufacturer} {self.model_name}'
