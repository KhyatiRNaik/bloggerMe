from django.shortcuts import render, redirect
from .forms import UserSignUpForm, UpdateUserForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Created account for {username}!')
            return redirect('login')

    else:
        form = UserSignUpForm()
    return render(request, 'users/signUp.html', {'form': form})

@login_required 
def profile(request):
    if request.POST:
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('profile')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }

    return render(request, 'users/profile.html', context)