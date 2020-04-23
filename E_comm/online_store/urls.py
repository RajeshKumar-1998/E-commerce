from django.urls import path
from .views import cart, category, product, Home, Order, add_to_cart, remove_from_cart
from . import views

app_name = 'online_store'

urlpatterns = [
    path('',Home.as_view(),name= 'home'),
    path('cart/<slug>',add_to_cart,name='cart'),
    path('remove/<slug>',remove_from_cart,name ='remove'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name ='blog'),
    path('Catagori/',views.catagori,name = 'Catagori'),
    path('contact/',views.contact,name ='contact'),
    path('elements/',views.elements,name= 'elements'),
    path('login/',views.login,name='login'),
    path('main/',views.main,name='main'),
    path('product_list/',views.prod_list,name ='prod'),
    path('single/',views.single_blog,name='single'),
    path('single_prod/',views.single_prod,name='pro'),
    path('checkout/',views.checkout,name='checkout'),
    path('industries/',views.industries,name ='industries'),
]