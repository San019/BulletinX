from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages  # For feedback messages
from .models import Notice
from .forms import NoticeForm

def home(request):
    category = request.GET.get('category', None)
    notices = Notice.objects.all()
    if category:
        notices = notices.filter(category=category)
    categories = [choice[0] for choice in Notice.CATEGORY_CHOICES]
    context = {'notices': notices, 'categories': categories, 'selected_category': category}
    return render(request, 'home.html', context)

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    context = {'notice': notice}
    return render(request, 'notice_detail.html', context)

@login_required
def submit_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            messages.success(request, 'Notice submitted successfully!')
            return redirect('home')
    else:
        form = NoticeForm()
    context = {'form': form}
    return render(request, 'submit_notice.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')  # Changed from '/home' to 'home' (named URL)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/login') 