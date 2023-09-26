from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Mixture of login/home page. Template in home.html
def home(request):
    # Check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate User
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.success(
                request, "There was an error, please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    pass
