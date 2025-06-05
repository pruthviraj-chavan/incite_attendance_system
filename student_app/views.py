from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.utils import timezone  # Import timezone here
from datetime import datetime, time


# Home Page
def home(request):
    return render(request, 'home.html')

# Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = StudentProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                course=form.cleaned_data['course']
            )
            FeeStatus.objects.create(student=profile)
            # Use auth_login instead of login
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            # Redirect admins to admin dashboard
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')  # Regular users go to student dashboard

        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Profile Edit
@login_required
def profile(request):
    profile = StudentProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

# Dashboard
@login_required
def dashboard(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)

    today = timezone.now().date()
    today_start = timezone.make_aware(datetime.combine(today, time()))
    today_end = timezone.make_aware(datetime.combine(today, time(23, 59, 59)))

    attendance = AttendanceRequest.objects.filter(
        student=profile,
        date_requested__range=(today_start, today_end)
    ).first()

    if not attendance:
        attendance = AttendanceRequest.objects.create(
            student=profile,
            status='Pending'
        )

    fee_status, fee_created = FeeStatus.objects.get_or_create(student=profile)

    return render(request, 'dashboard.html', {
        'attendance': attendance,
        'fee_status': fee_status
    })

# Request Attendance
@login_required
def request_attendance(request):
    profile = StudentProfile.objects.get(user=request.user)
    AttendanceRequest.objects.get_or_create(
        student=profile,
        date_requested=timezone.now().date()
    )
    return redirect('dashboard')

# Admin Dashboard
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')  # Redirect non-admin users
    requests = AttendanceRequest.objects.all()
    fees = FeeStatus.objects.all()
    return render(request, 'admin_dashboard.html', {
        'requests': requests,
        'fees': fees
    })

# Approve Attendance
@login_required
def approve_attendance(request, request_id):
    req = AttendanceRequest.objects.get(id=request_id)
    req.status = 'Approved'
    req.save()
    return redirect('admin_dashboard')

# Reject Attendance
@login_required
def reject_attendance(request, request_id):
    req = AttendanceRequest.objects.get(id=request_id)
    req.status = 'Rejected'
    req.save()
    return redirect('admin_dashboard')

# Update Fee Status
@login_required
def update_fee_status(request, fee_id):
    fee = FeeStatus.objects.get(id=fee_id)
    if request.method == 'POST':
        fee.status = request.POST.get('status')
        fee.last_payment_date = request.POST.get('last_payment_date')
        fee.remarks = request.POST.get('remarks')
        fee.save()
        return redirect('admin_dashboard')
    return render(request, 'update_fee.html', {'fee': fee})

@login_required
def courses_page(request):
    return render(request, 'courses.html')

@login_required
def ai_tools_page(request):
    return render(request, 'ai_tools.html')

@login_required
def resources_page(request):
    # Example list of downloadable files
    resources = [
        {'name': 'Math Notes', 'file': 'math_notes.pdf'},
        {'name': 'Physics Question Paper', 'file': 'physics_qp.pdf'},
        {'name': 'Python Basics', 'file': 'python_basics.pdf'},
    ]
    return render(request, 'resources.html', {'resources': resources})