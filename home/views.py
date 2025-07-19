from django.shortcuts import render, HttpResponse, redirect # type: ignore
from datetime import datetime
from home.models import Contact
from django.contrib import messages # type: ignore
# from django.contrib.auth.models import User
# from django.contrib.auth import logout, authenticate, login
from home.models import Product
from .forms import ProductForm
# from home.models import Users
# from django.shortcuts import render
from .models import Product
import razorpay
from django.conf import settings
# from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
# from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse, HttpResponseForbidden
# from django.views.decorators.csrf import csrf_exempt

# from django.contrib.auth.decorators import login_required
# from .models import Userss
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.hashers import make_password




# Create your views here.
# def index(request):
#     # return HttpResponse("This is Home page")
#     context = {
#         'variable':"This is sent",
#     }
    
#     if request.user.is_anonymous:
#         return redirect("/login")
#     return render(request, 'index.html', context)

def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')  # Redirect to login page if not authenticated

    # popup_shown = cache.get('popup_shown', False)  # Get cache value (default: False)
    # return render(request, 'index.html', {'popup_shown': popup_shown})
    contact_messages = Contact.objects.values('name', 'desc').order_by('-id')
    return render(request, 'index.html', {'contact_messages': contact_messages})
    


def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent!')
    return render(request, 'contact.html')


def product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category = request.POST.get('category')

        try:
            product = Product(name=name, description=description, price=price, image=image, category=category )
            product.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return render(request, 'product.html')


def items(request):
    categories = ['veg', 'non_veg', 'cold_drinks', 'snacks']
    categorized_products = {}

    for cat in categories:
        categorized_products[cat] = Product.objects.filter(category=cat)

    return render(request, 'items.html', {'categorized_products': categorized_products})




def cart(request):
    return render(request, 'cart.html')

# def initiate_payment(request):
#     if request.method == "POST":
#         amount = int(request.POST.get("amount")) * 100  # Convert to paise (Razorpay needs amount in paise)
#         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         payment = client.order.create({
#             "amount": amount,
#             "currency": "INR",
#             "payment_capture": "1"
#         })
#         return JsonResponse(payment)
#     return JsonResponse({"error": "Invalid request"}, status=400)

# def order_success(request):
#     return render(request, "order_success.html")

# def users(request):
#     if request.method == "POST":
#         # handle form saving here...
#         pass
#     return render(request, 'users.html')  # or whatever your registration template is called



def create_order(request):
    if request.method == "POST":
        amount = int(float(request.POST.get('amount')) * 100)  # Razorpay uses paise
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        order_data = {
            'amount': amount,
            'currency': 'INR',
            'payment_capture': 1
        }
        order = client.order.create(data=order_data)

        return render(request, 'payment_page.html', {
            'order_id': order['id'],
            'amount': amount,
            'razorpay_key': settings.RAZORPAY_KEY_ID
        })