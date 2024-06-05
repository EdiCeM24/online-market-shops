from django.shortcuts import render, redirect
# this is to import database module below
from item .models import Category, Item
# this below is importing from forms.py.
from .forms import SignupForm, LoginForm # type: ignore



def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'app/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'app/contact.html')

    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
       form = SignupForm() #then if it is not POST request then it will use this line.

    return render(request, 'app/signup.html', {
        'form': form,
    })


def login(request):
    return render(request, 'app/login.html')



