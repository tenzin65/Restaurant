from django.contrib import admin
from django.urls import path
from home import views
# from home.views import login_view
# from home.views import registerUser

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('product', views.product, name='product'), 
    path('items', views.items, name='items'),
    path('users', views.users, name='users'),
    path('cart', views.cart, name='cart'),
    path('initiate-payment', views.initiate_payment, name='initiate_payment'),
    path('order-success', views.order_success, name='order_success'),
    # path('login/', login_view, name='login'),
    
    # path("register/", views.registerUser, name="register"),
   
]