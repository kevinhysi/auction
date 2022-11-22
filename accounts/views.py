from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('website:homepage')
    else:
        form = SignUpForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save(commit=False)
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                user = authenticate(email=email, password=password)

                if user is not None:
                    login(request, user)
                return redirect('accounts:profile')

    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('website:homepage')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, email=email, password=password)

                if user is not None:
                    login(request, user)
                return render(request, 'profile.html')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})


@login_required(login_url='accounts:login')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='accounts:login')
def user_logout(request):
    logout(request)

    return redirect('website:homepage')
