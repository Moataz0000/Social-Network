from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Account is created successfully.')
                # sent an email
                return redirect('accounts:sign-in')
        except Exception as e:
            messages.error(request, 'Invalid Sign Up, Please try againe!')
            return redirect('accounts:sign-up')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/sign_up.html', context)





def SignIn(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have signed in successfully.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('accounts:sign-in')
        else:
            messages.error(request, 'Username and password didn\'t match!')
            return redirect('accounts:sign-in')

    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/sign_in.html', context)





def profile(request):
    return render(request, 'accounts/profile.html')



def SignOut(request):
    logout(request)
    messages.success(request, 'You are logged out now')
    return redirect('accounts:sign-in')