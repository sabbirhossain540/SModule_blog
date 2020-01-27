from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request, f'Account created for {username}!')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html',{'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_from = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        #a = request.POST.get('username')

        if u_from.is_valid() and p_form.is_valid():
            u_from.save()
            p_form.save()

            messages.success(request, f'Your Profile has been updated Successfully')
            return redirect('login')
    else:
        u_from = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form' : u_from,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
