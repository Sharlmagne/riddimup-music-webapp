from django.shortcuts import render, redirect
from .forms import UserRegisterForm, TrackUploadForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Track



# Registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
        else:
            messages.warning(request, f'Invalid Entry')     
            
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Profile Page
@login_required
def profile(request):
    current_user = request.user
    context = {
        'tracks': Track.objects.filter(author=current_user),
    }
    return render(request, 'users/profile.html/', context)

# Account Page
@login_required
def account(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile updated')
            return redirect('account')
        else:
            messages.warning(request, f'Invalid Entry')    

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
            'u_form': u_form,
            'p_form': p_form
        }
        
    return render(request, 'users/account.html', context)   

# Upload tracks
@login_required
def upload(request):
    
    if request.method == 'POST': 
        form = TrackUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            track = form.cleaned_data.get('track_title')
            artist = form.cleaned_data.get('artist_name') 
            messages.success(request, f'{track} by "{artist}" was successfully uploaded')
            return redirect('profile')
        else:
            messages.warning(request, f'Invalid Entry') 
             
    else:
        form = TrackUploadForm()           
    return render(request, 'users/upload.html', {'form': form})    




