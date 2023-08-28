from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, UserForm, UserProfileForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Member
from django.contrib.auth.models import User

# cannot be called login as this is 
# a library that has been imported.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('office:home')
        else:
            messages.success(request,("There was an error logging in, Try Again....."))
            return redirect('members:login_user')
            # Return an 'invalid login' error message.
            
    else:
        return render(request, 'authenticate/login.html', {} )


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration complete!"))
            return redirect('members:profile')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {'form':form})

# makes sure the user is logged in
# the transaction atomic makes sure both forms are required
#@login_required
#@transaction.atomic
def update_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Member.objects.get(user_id=request.user.id)
        
        user_form = UserForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            login(request, current_user)
            messages.success(request, ("Your Profile has been Updated!"))
            return redirect('office:home')
        return render(request, "authenticate/profile.html", {"u_form":user_form, "p_form":profile_form})
    else:
        messages.success(request, ("Your Profile has been Updated!"))
        return redirect('office:home')

# Create your views here.
