from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return redirect("signup")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username Already exists.")
            return redirect("signup")
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already exists.")
            return redirect("signup")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created Successfully. Please login")
        return redirect("signin")
    
    return render(request, "signup.html")
        

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "login Success")
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials.")
            return redirect("signin")
        
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "logged out successfully.")
    return redirect("signin")
    







# from .utils import extract_invoice_fields
# def signup_view(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data["password"])
#             user.save()
#             # Auto-login after signup
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = SignupForm()
#     return render(request, "signup.html", {"form": form})
# def login_view(request):
#     error = None
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             error = "Invalid credentials"
#     return render(request, "login.html", {"error": error})
# def logout_view(request):
#     logout(request)
#     return redirect('login')
# @login_required
# def dashboard(request):
#     invoices = Invoice.objects.filter()
#     return render(request, "dashboard.html", {"invoices": invoices})
# @login_required
# def invoice_upload(request):
#     if request.method == "POST":
#         form = InvoiceUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             invoice = form.save()
#             file_path = invoice.file.path
#             extracted = extract_invoice_fields(file_path)
#             # Update the invoice instance with extracted fields.
#             invoice.invoice_date = extracted.get("invoice_date")
#             invoice.invoice_number = extracted.get("invoice_number")
#             invoice.amount = extracted.get("amount")
#             invoice.due_date = extracted.get("due_date")
#             invoice.save()
#             return redirect('dashboard')
#     else:
#         form = InvoiceUploadForm()
#     return render(request, "invoice_upload.html", {"form": form})