from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view,name="login"),
    path("logout", views.logout_view,name="logout"),
    path("register", views.register_view,name="register"),
    path("order",views.order_view,name="order"),
    path("checkout",views.checkout_view,name="checkout"),
    path("payment",views.payment_view,name="payment")
]
