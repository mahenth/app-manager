from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Product

@csrf_exempt
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect(my_home)
    else:
        return render(request, 'index.html', context)

@login_required
def my_home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)




from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(home)
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if request.user.is_superuser:
            return render(request, 'admin/home.html')
        elif user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect(home) # Replace 'home' with your desired URL name
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')




from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect(home)




from .forms import ProductForm

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', product.pk)
    else:
        form = ProductForm()
    return render(request, 'add_app.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'home.html', {'product': product})


from .models import Product
from .forms import ScreenshotForm

def task(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = ScreenshotForm()
    context = {'product': product, 'form': form}  # Define the context variable before the if statement
    if request.method == 'POST':
        form = ScreenshotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Process the uploaded screenshot here...
        else:
            # If the form is not valid, continue to render the form with validation errors
            pass
    return render(request, 'task.html', context)


def points(request):
    products = Product.objects.all()
    context = {
        'products': products
    }   
    return render(request, 'points.html', context)


from .models import UserProfile

def profile(request):
    user = UserProfile.objects.all()
    context = {'user': user}
    return render(request, 'profile.html', context)
