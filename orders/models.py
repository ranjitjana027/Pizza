from django.db import models

# Create your models here.
class Regular(models.Model):
    name=models.CharField(max_length=64)
    small=models.FloatField()
    large=models.FloatField()

    def __str__(self):
        return f"{self.name} Small Price: {self.small} Large Price: {self.large}"

class Sicilian(models.Model):
    name=models.CharField(max_length=64)
    small=models.FloatField()
    large=models.FloatField()

    def __str__(self):
        return f"{self.name} Small Price: {self.small} Large Price: {self.large}"

class Toppings(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Subs(models.Model):
    name=models.CharField(max_length=64)
    small=models.FloatField()
    large=models.FloatField()

    def __str__(self):
        return f"{self.name} Small Price: {self.small} Large Price: {self.large}"

class Pasta(models.Model):
    name=models.CharField(max_length=64)
    price=models.FloatField()


    def __str__(self):
        return f"{self.name} Price: {self.price}"

class Salad(models.Model):
    name=models.CharField(max_length=64)
    price=models.FloatField()

    def __str__(self):
        return f"{self.name} Price: {self.price}"

class Dinner_Platters(models.Model):
    name=models.CharField(max_length=64)
    small=models.FloatField()
    large=models.FloatField()

    def __str__(self):
        return f"{self.name} Small Price: {self.small} Large Price: {self.large}"


class Order(models.Model):
    dish=models.CharField(max_length=64)
    type=models.CharField(max_length=64) # small or large
    quantity=models.IntegerField()
    price=models.FloatField()

    def __str__(self):
        return f"{self.dish} {self.type} quantity={self.quantity} Price for {self.quantity}= {self.price}"

class Order_Details(models.Model):
    username=models.CharField(max_length=64)
    order=models.ForeignKey(Order,related_name="order",on_delete=models.CASCADE)
    payment=models.CharField(max_length=2)

    def __str__(self):
        return f"{self.username} {self.order}"
