from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Pasta, Salad,Regular,Sicilian,Dinner_Platters,Subs,Toppings, Order_Details, Order
import json
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"orders/login.html",{"message":None})

    context={ "regulars":Regular.objects.all(), "pastas":Pasta.objects.all(), "salads": Salad.objects.all(),
    "sicilians":Sicilian.objects.all(), "dinners":Dinner_Platters.objects.all(), "toppings":Toppings.objects.all(),
    "subs":Subs.objects.all(),"user":request.user  }

    return render(request,"orders/index.html",context)

def login_view(request):
    try:
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context={"message":"No User Found"}
            return render(request,"orders/login.html",context)
    except KeyError:
        return render(request,"orders/login.html",{"message":"No Information found"})
    except:
        return render(request,"orders/login.html",{"message":"Something went wrong"})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('index'))

def register_view(request):
    try:
        username=request.POST["username"]
        password=request.POST["password"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        if user is not None:
            user.save()
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,"orders/register.html",{"message":"Something went wrong"})
    except:
        return render(request,"orders/register.html",{"message":"Something went wrong"})

def order_view(request):
    try:
        regular_small=request.POST.getlist("regular-small")
        cnt=0
        if regular_small is not None:
            for reg in regular_small:
                r=Regular.objects.get(pk=reg)
                order=Order(dish=r.name, type="regular_small",quantity=1,price=r.small)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()


                cnt+=1
        return HttpResponseRedirect(reverse('checkout'))
    except:
        return HttpResponseRedirect(reverse('index'))

def checkout_view(request):
    if not request.user.is_authenticated:
        return render(request,"orders/login.html",{"message":None})
#    try:
    orders_list= Order_Details.objects.filter(username=request.user).exclude(payment='Y')
    sum=0
    for element in orders_list:
        sum+=element.order.price
    context={
            "user":request.user, "orders_list": orders_list, "price":sum
        }
    return render(request,"orders/order.html",(context))
    #except:
    #        return HttpResponseRedirect(reverse('index'))

def payment_view(request):
    orders_list= Order_Details.objects.filter(username=request.user).exclude(payment='Y').update(payment='Y')
    return HttpResponse("Payment Successfull")
