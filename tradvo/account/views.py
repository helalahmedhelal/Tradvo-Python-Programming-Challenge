from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, UpdatedUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    
    if request.method =='POST':
        form = CreateUserForm(request.POST)  # Correctly pass POST data
        if form.is_valid():
           form.save()
           messages.success(request, 'Registration successful!')
           return redirect('interface')  
        else:
            messages.error(request, 'Please correct the error below.')  # Error message
    else:
        form = CreateUserForm()
    
    context={'form':form}    
    return render(request,'account/registration/register.html',context)


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('interface')  
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    context= {'form': form}
    
    return render(request, 'account/login.html',context)


@login_required(login_url='login')
def logoutview(request):
    
    logout(request)
    
    return redirect('interface')


@login_required(login_url='login')
def profile(request):
    
    if request.method == 'POST':
        
        user_form=UpdatedUserForm(request.POST, instance=request.user)
        
        if user_form.is_valid():
            
            user_form.save()
            
            return redirect('interface')
        
    user_form = UpdatedUserForm(instance= request.user)
    
    context={'user_form':user_form}
    
    return render(request,'account/profile/profile.html',context)    