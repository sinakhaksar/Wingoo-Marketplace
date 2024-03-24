from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login
from item.models import Category, Item

# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold = False).all()
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request, user)

            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)
            else:
                return redirect('core:index')  # Redirect to a default page if 'next' parameter is not present

    else: 
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

