from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ServiceRequestForm
from .models import ServiceRequest, UserAccount

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Please enter a correct username and password."
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')

def home(request):
    return render(request, 'Gas_Services/home.html')

@login_required
def account_info(request):
    account_info = UserAccount.objects.get(user=request.user)
    return render(request, 'Gas_Services/account_info.html', {'account_info': account_info})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_request', request_id=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'Gas_Services/submit_request.html', {'form': form})

@login_required
def track_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id, customer=request.user)
    return render(request, 'Gas_Services/track_request.html', {'service_request': service_request})
