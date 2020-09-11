from django.contrib import admin
from django.urls import path
from shop.views import index,about,contact,tracker,search,productView,checkout

app_name = 'shop'

urlpatterns = [
    path('', index, name = 'ShopHome'),
    path('about/',about,name='AboutUs'),
    path('contact/',contact,name='ContactUs'),
    path('tracker/',tracker,name='TrackingStatus'),
    path('search/',search,name='Search'),
    path('product/<int:id>',productView,name='ProductView'),
    path('checkout/',checkout,name='Checkout'),

]
