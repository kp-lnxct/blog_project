from django.forms.fields import EmailField
from django.shortcuts import render,redirect 

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdate

from django.contrib.auth.decorators import login_required
# Create your views here.




def admin_form(request):

    if request.method == 'POST':
        print('-------------------------Method is Post')
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('admin_login')
    else:
        print('-------------------------Else part ')
        form = UserCreationForm()

    return render(request, 'users/register.html',{'form':form, 'type':'form'})

def admin_form_class(request):

    if request.method == 'POST':
        print('-------------------------Method is Post')
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('admin_login')
    else:
        print('-------------------------Else part ')
        form = UserRegisterForm()

    return render(request, 'users/register.html',{'form':form, 'type':'class'})

def admin_crispy_form(request):

    if request.method == 'POST':
        print('-------------------------Method is Post')
        form = UserRegisterForm(request.POST)

        if form.is_valid():
    
            username = form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('admin_login')
    else:
        print('-------------------------Else part ')
        form = UserRegisterForm()

    return render(request, 'users/register.html',{'form':form, 'type':'crispy'})


@login_required
def profile(request):
    if request.method == "POST":
            
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, 
                                request.FILES , 
                                instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)

    context = {'uform':u_form, 'pform':p_form}

    return render(request, 'users/profile.html', context)



    