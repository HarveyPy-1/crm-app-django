from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm
from .models import Record

# Mixture of login/home page. Template in home.html
def home(request):
    #Assign all records in the database to 'records'
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records': records})


# def login_user(request):
#     pass

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and log them in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You've successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render (request, 'register.html', {'form': form})
    
    return render (request, 'register.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You've been successfully logged out")
    return redirect ('home')
