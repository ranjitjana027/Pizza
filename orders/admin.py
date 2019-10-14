from django.contrib import admin
from .models import Pasta, Salad,Regular,Sicilian,Dinner_Platters,Subs,Toppings,Order,Order_Details
# Register your models here.
admin.site.register(Regular)
admin.site.register(Sicilian)
admin.site.register(Subs)
admin.site.register(Toppings)

admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_Platters)
admin.site.register(Order)
admin.site.register(Order_Details)
