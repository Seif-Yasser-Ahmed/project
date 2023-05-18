from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('cart', views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name="add"),
]
