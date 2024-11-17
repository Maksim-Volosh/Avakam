from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, UserCreationForm


def register(request):
    """
    Register a new user.

    If the request method is POST and the form is valid, create a new user
    with the provided email and password. Log in the new user and redirect
    to the URL specified in the GET parameter 'next'. If 'next' is not
    provided, redirect to the 'main:main' URL.

    If the request method is GET, display the registration form.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_url = request.GET.get('next', 'main:main')
            return redirect(next_url)
    else:
        form = UserCreationForm()
        
    return render(request, 'user/register.html', {'form': form})

def loginview(request):
    """
    Log in a user.

    If the request method is POST and the form is valid, authenticate the user
    with the provided email and password. If authentication is successful, log
    in the user and redirect to the URL specified in the GET parameter 'next'.
    If 'next' is not provided, redirect to the 'main:main' URL.

    If the request method is GET, display the login form.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'main:main')
                return redirect(next_url)
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

@login_required
def logoutview(request):
    """
    Log out a user.

    If the user is authenticated, log out the user and redirect to the 'main:main' URL.
    If the user is not authenticated, redirect to the 'user:login' URL.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    user = request.user
    if user.is_authenticated:
        logout(request)
        return redirect('main:main')
    else:
        return redirect('user:login')
