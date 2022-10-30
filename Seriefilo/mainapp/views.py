from django.shortcuts import render, get_object_or_404, redirect
from mainapp.models import Serie, Platform, Category
from django.db.models.functions import Lower
from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def index (request):
    return render(request, 'mainapp/index.html', {
        'title' : 'Index'
    })


"""def about_us (request):
    return render(request, 'mainapp/about-us.html', {
        'title' : 'About us'
    })


def contact (request):
    return render(request, 'mainapp/contact.html', {
        'title' : 'Contact'
    })"""

@login_required(login_url="login")
def list(request):
    
    #Sacar series
    series = Serie.objects.all().order_by(Lower('title')) 
    
    #Paginar series
    paginator = Paginator(series, 2)
    

    #recoger numero pagina
    page = request.GET.get('page')
    page_series = paginator.get_page(page)
    
    return render(request, 'mainapp/list.html', {
        'title': 'Series',
        'series': page_series
    })

@login_required(login_url="login")
def category(request, genre):

    category = get_object_or_404(Category, genre=genre)


    return render(request, 'mainapp/category.html', {
        'category' : category,
        
        
    })
   
@login_required(login_url="login")
def platform(request, wheretosee):

    platform = get_object_or_404(Platform, wheretosee=wheretosee)
    
    return render(request, 'mainapp/platform.html', {
        'platform' : platform
    })

def serie(request, title):
    serie = get_object_or_404(Serie, title=title)

    return render(request, 'mainapp/detail.html', {
        'serie' : serie

    })


def register_page(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
    
        register_form = RegisterForm()

        if request.method =='POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Registered successfully!')

                return redirect('index')



        return render(request, 'users/register.html',
        {
            'title': 'Register',
            'register_form' : register_form

        })




def login_page(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'It failed. Try again')

        return render(request, 'users/login.html',{
            'title': 'Login'

        })

def logout_user(request):
    logout(request)
    return redirect('login')


