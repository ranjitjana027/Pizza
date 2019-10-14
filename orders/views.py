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
        # Regular Small
        regular_small=request.POST.getlist("regular-small")
        if regular_small is not None:
            for reg in regular_small:
                r=Regular.objects.get(pk=reg)
                order=Order(dish=r.name, type="regular_small",quantity=1,price=r.small)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()

        # Regular large
        regular_large=request.POST.getlist("regular-large")
        if regular_large is not None:
            for reg in regular_large:
                r=Regular.objects.get(pk=reg)
                order=Order(dish=r.name, type="regular_large",quantity=1,price=r.large)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()



        #### Sicilian Small
        sicilian_small=request.POST.getlist("sicilian-small")
        if sicilian_small is not None:
            for sic in sicilian_small:
                s=Sicilian.objects.get(pk=sic)
                order=Order(dish=s.name, type="sicilian_small",quantity=1,price=s.small)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()


        #### Sicilian Large
        sicilian_large=request.POST.getlist("sicilian-large")
        if sicilian_large is not None:
            for sic in sicilian_large:
                s=Sicilian.objects.get(pk=sic)
                order=Order(dish=s.name, type="sicilian_large",quantity=1,price=s.large)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()

        #### Subs Small
        subs_small=request.POST.getlist("sub-small")
        if subs_small is not None:
            for sub in subs_small:
                s=Subs.objects.get(pk=sub)
                order=Order(dish=s.name, type="subs_small",quantity=1,price=s.small)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()
        #### Subs Large
        subs_large=request.POST.getlist("sub-large")
        if subs_large is not None:
            for sub in subs_large:
                s=Subs.objects.get(pk=sub)
                order=Order(dish=s.name, type="subs_large",quantity=1,price=s.large)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()
        #### Pasta
        pastas=request.POST.getlist("pasta")
        if pastas is not None:
            for pas in pastas:
                p=Pasta.objects.get(pk=pas)
                order=Order(dish=p.name, type="Pasta",quantity=1,price=p.price)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()

        #### Salad
        salad=request.POST.getlist("salad")
        if salad is not None:
            for sal in salad:
                s=Salad.objects.get(pk=sal)
                order=Order(dish=s.name, type="Salad",quantity=1,price=s.price)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()
        #### Dinner Small
        dinner_small=request.POST.getlist("dinner-small")
        if dinner_small is not None:
            for din in dinner_small:
                d=Dinner_Platters.objects.get(pk=din)
                order=Order(dish=d.name, type="Dinner_Platters_small",quantity=1,price=d.small)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()
        #### Dinner Large
        dinner_large=request.POST.getlist("dinner-large")
        if dinner_large is not None:
            for din in dinner_large:
                d=Dinner_Platters.objects.get(pk=din)
                order=Order(dish=d.name, type="Dinner_Platters_Large",quantity=1,price=d.large)
                order.save()
                od=Order_Details(username=request.user,order=order,payment='N')
                od.save()

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
