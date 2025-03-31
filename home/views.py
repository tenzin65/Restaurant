from django.shortcuts import render, HttpResponse, redirect # type: ignore
from datetime import datetime
from home.models import Contact
from django.contrib import messages # type: ignore
# from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from home.models import Product
from home.models import Users
import razorpay
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
# from home.models import Userss
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
    if request.user.is_authenticated:  
        return render(request, 'index.html')
    return redirect('login')  # Redirects to login if not authenticated


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
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request),
    return redirect("/login")


def product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        product = Product(name=name, description=description, price=price, image=image)
        product.save()
    return render(request, 'product.html')

def items(request):
    product = Product.objects.filter()
    return render(request, 'items.html', {'product': product})

def users(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        if Users.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('users')

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('users')

        user = Users(username=username, email=email, password=password, phone=phone)
        user.save()  # Password is automatically hashed in the model

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')

    return render(request, 'users.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Users.objects.get(username=username)
            if user.check_password(password):  # Verify password
                request.session['user_id'] = user.id  # Store session
                request.session['username'] = user.username
                messages.success(request, "Login successful!")
                return redirect("home")  # Redirect to homepage
            else:
                messages.error(request, "Invalid password!")
        except Users.DoesNotExist:
            messages.error(request, "User not found!")

    return render(request, "login.html")

# def logoutUser(request):
#     logout(request)
#     messages.success(request, "Logged out successfully!")
#     return redirect("login")
def logoutUser(request):
    request.session.flush()  # Clear session
    messages.success(request, "Logged out successfully!")
    return redirect("login")  # Redirect to login page

def cart(request):
    return render(request, 'cart.html')

def initiate_payment(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount")) * 100  # Convert to paise (Razorpay needs amount in paise)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": "1"
        })
        return JsonResponse(payment)
    return JsonResponse({"error": "Invalid request"}, status=400)

def order_success(request):
    return render(request, "order_success.html")
