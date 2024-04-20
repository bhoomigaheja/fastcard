"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf  import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name = 'index'),
    path('list/',views.list,name = 'list'),

    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),

    
    
     path('',views.signup,name = 'signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('shopfullwidth',views.shopfullwidth,name = 'shopfullwidth'),
    path('signin',views.signin,name = 'signin'), 
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    # View cart details
    path('cart/', views.cart_detail, name='cart_detail'),
    path('shopcart/',views.shopcart,name = 'shopcart'),
    # Update item quantities in the cart
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('cart/cart_clear/<int:product_id>/', views.cart_clear, name='cart_clear'),
    path('cart/item_decrement/<int:product_id>/', views.item_decrement, name='item_decrement'),
    path('cart/item_increment/<int:product_id>/', views.item_increment, name='item_increment'),
    # Remove item from the cart
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # Checkout or any other additional URLs you need
     
    path('contact/', views.contact, name='contact'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('ordernow/', views.ordernow, name='ordernow'),
    path('place_order/', views.place_order, name='place_order'),
    path('status/', views.status, name='status'),
    path('view_details/<int:order_id>/', views.view_details, name='view_details'),
    path('order/status/<int:order_id>/', views.order_status_view, name='order_status'),

    path('invoice/<int:order_id>/', views.invoice, name='invoice'),
    path('orderry', views.orderry, name='orderry'),
     path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist', views.wishlist, name='wishlist'),
    
    

    



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

'''#addtocart
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    # View cart details
    path('cart/', views.cart_detail, name='cart_detail'),
    # Update item quantities in the cart
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('cart/cart_clear/<int:product_id>/', views.cart_clear, name='cart_clear'),
    path('cart/item_decrement/<int:product_id>/', views.item_decrement, name='item_decrement'),
    path('cart/item_increment/<int:product_id>/', views.item_increment, name='item_increment'),
    # Remove item from the cart
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    # Checkout or any other additional URLs you need
    path('checkout/', views.checkout, name='checkout'),'''
    


