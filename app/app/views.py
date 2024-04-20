from django.shortcuts import render,redirect

from groceryapp.models  import product2,category,product2,Order,details
from django.contrib.auth import authenticate,login
from groceryapp.models import Usercreateform
# Create your views here.
def index(request):
    categoryy = category.objects.all()

    cont = {
        'categoryy':categoryy
    }
    return render(request,'index.html',cont)

def list(request):
    product = product2.objects.all()
    CATID = request.GET.get('category')
    if CATID:
        product = product2.objects.filter(category=CATID)
    else:
        product = product2.objects.all()
    context = {
        'product':product
    }
    return render(request,'listing.html',context)

from django.shortcuts import render, get_object_or_404
# Import your model

from django.shortcuts import render, get_object_or_404


def product_detail(request, product_id):
    product = get_object_or_404(product2, id=product_id)
    context = {'product': product}
    return render(request, 'product-detail.html', context)

        









from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from groceryapp.models import Usercreateform ,contact_us 

def signup(request):
    if request.method == 'POST':
        form = Usercreateform(request.POST)
        if form.is_valid():
            # Form processing and user creation
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            if new_user is not None:
                login(request, new_user)
                return render( request,'signin.html')
    else:
        form = Usercreateform()

    context = {'form': form}
    return render(request, 'signup.html', context)

def shopcart(request):
    return render(request,'shop-cart.html')

def shopfullwidth(request):
    return render(request,'shop-fullwidth.html')

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a successful login page, e.g., home page
            categories = category.objects.all()  # Fetch all category objects from the database
            # Redirect to a successful login page, e.g., home page
            return render(request, 'index.html', {'categoryy': categories})  # Change 'home' to your actual home page's name
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})
   
from django.contrib.auth.decorators import login_required
from cart.cart import Cart  # If cart.py is in the same directory as your views


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
@login_required(login_url="/users/signin")
def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'view_cart.html', {'cart': cart})


@login_required(login_url="/users/signin")
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(product2, id=id)
    
    cart.add(product=product)
    
    # Fetch the category associated with the product
    category = product.category
    
    # Pass the category to the template context
    context = {
        'category': category
    }
    
    # Redirect the user to the product detail page after adding the item to the cart
    return HttpResponseRedirect(reverse('shopcart'), context)



@login_required(login_url="/users/signin")
def cart_detail(request):
    # Logic to retrieve the cart details
    cart = Cart(request)
    context = {
        'cart': cart,
    }
    return render(request, 'shop-cart.html', context)

@login_required(login_url="/users/signin")
def cart_update(request, product_id):
    # Logic to update item quantities in the cart
    cart = Cart(request)
    product = get_object_or_404(product2, id=product_id)
    quantity = int(request.POST.get('quantity'))
    cart.update(product=product, quantity=quantity)
    return redirect('shopcart')

@login_required(login_url="/users/signin")
def cart_clear(request, product_id):
    # Logic to clear a specific item from the cart
    cart = Cart(request)
    product = get_object_or_404(product2, id=product_id)
    cart.remove(product=product)
    return redirect('shopcart')

@login_required(login_url="/users/signin")
def item_decrement(request, product_id):
    # Logic to decrement item quantity in the cart
    cart = Cart(request)
    product = get_object_or_404(product2, id=product_id)
    cart.decrement(product=product)
    return redirect('shopcart')

@login_required(login_url="/users/signin")
def item_increment(request, product_id):
    # Logic to increment item quantity in the cart
    cart = Cart(request)
    product = product2.objects.get(id=product_id)
    cart.add(product)
    return redirect('shopcart')

@login_required(login_url="/users/signin")
def cart_remove(request, product_id):
    # Logic to remove an item from the cart
    cart = Cart(request)
    product = get_object_or_404(product2, id=product_id)
    cart.remove(product)
    return redirect('shopcart')
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.core.exceptions import ObjectDoesNotExist



from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from groceryapp.models  import product2,category







from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist





                    
                




def my_orders(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('products')
    return render(request, 'account-orders.html', {'orders': orders})










# views.py

from django.shortcuts import render
# Assuming your model is named 'order'
from django.shortcuts import render



from django.shortcuts import render



def ordernow(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = product2.objects.filter(id__in=product_ids)

    total_price = sum(product.price for product in products)

    context = {
        'products': products,
        'total_price': total_price,
    }
    return render(request, 'checkout.html', context)
from django.shortcuts import render, redirect

 
from django.shortcuts import render, redirect
from groceryapp.forms import OrderForm


from datetime import datetime
from django.shortcuts import redirect

from django.shortcuts import redirect, render
from datetime import datetime
from django.shortcuts import redirect, render
from datetime import datetime

def place_order(request):
    if request.method == 'POST':
        # Process cart items and fetch products
        cart = request.session.get('cart', {})
        product_ids = cart.keys()
        products = product2.objects.filter(id__in=product_ids)
        
        total_price = sum(product.price for product in products)
        
        # Create a new order instance
        order = Order(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone_number=request.POST.get('phone_number'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            pincode=request.POST.get('pincode'),
            landmark=request.POST.get('landmark'),
            user=request.user if request.user.is_authenticated else None,
            total_price=total_price,
            order_date=datetime.now()
        )
        
        order.save()
        
        # Add products to the order
        order.products.add(*products)
        
        # Clear the cart after order placement
        del request.session['cart']
        
        return render(request,'a.html')  # Redirect to success page
    
    else:
        form = OrderForm()
    
    return render(request, 'checkout.html', {'form': form})




from django.shortcuts import render


def contact(request):
    if request.method == 'POST':
        contact = contact_us(
            name=request.POST.get('name'),
            email=request.POST.get('email'), 
            message=request.POST.get('message'), 
        )
        contact.save()
    return render(request, 'contact.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def status(request):
    details_list = request.user.details_set.all()  # Fetching details related to the logged-in user
    
    # Extracting order related fields for each details object
    orders_data = []
    for detail in details_list:
        order_data = {
            'products': detail.order.products.all(),  # Fetching products related to the order
            'address': detail.order.address,
            'delivery_status': detail.delivery_status,
            'delivery_boy_name': detail.delivery_boy.username if detail.delivery_boy else "Not Assigned"
        }
        orders_data.append(order_data)
    
    delivery_status_choices = [(choice[0], choice[1]) for choice in details.STATUS_CHOICES]  # Converting STATUS_CHOICES to a list of tuples
    
    context = {
        'orders_data': orders_data,
        'delivery_status_choices': delivery_status_choices
    }
    
    return render(request, 'status.html', context)
def view_details(request, order_id):
    order = Order.objects.get(id=order_id)
    products = order.products.all()
    return render(request, 'view_details.html', {'order': order, 'products': products})

def order_status_view(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        order_status = [
            ('pending', 'Pending'),
            ('out_for_delivery', 'Out for Delivery'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled'),
            ('returned', 'Returned'),
        ]
        
        context = {
            'order': order,
            'order_status': order_status,
        }
        
        return render(request, 'b.html', context)
    
    except Order.DoesNotExist:
        return print('<h1>Order not found</h1>')




from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def invoice(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        
        # Directly fetch products from the order
        order_items = order.products.all()
        
        total_price = sum(product.price for product in order_items)
        
        context = {
            'user': request.user,
            'order': order,
            'total_price': total_price,
        }
        
        return render(request, 'invoice.html', context)
    
    except Order.DoesNotExist:
        # Handle the case when the order does not exist
        return render(request, 'error.html', {'message': 'Order does not exist.'})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def orderry(request):
    # Fetch orders associated with the logged-in user
    user_orders = Order.objects.filter(user=request.user)

    # Extract unique addresses from the orders
    addresses = set([(order.address, order.pincode, order.city) for order in user_orders if order.address])

    return render(request, 'my-account.html', {'addresses': addresses})
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from django.urls import reverse

def add_to_wishlist(request, product_id):
    product = product2.objects.get(id=product_id)
    
    wishlist = request.session.get('wishlist', [])
    
    if product_id not in wishlist:
        wishlist.append(product_id)
        request.session['wishlist'] = wishlist
    
    return redirect(reverse('wishlist'))

def wishlist(request):
    wishlist_ids = request.session.get('wishlist', [])
    products = product2.objects.filter(id__in=wishlist_ids)
    
    context = {
        'products': products
    }
    
    return render(request, 'wishlist.html', context)
