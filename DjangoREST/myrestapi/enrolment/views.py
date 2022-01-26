# enrolment/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'registration/signup.html'

from django.views import generic
from .forms import SignUpForm

class SignUpView(generic.CreateView):
    """
    Allows the User to Create a New Account
    """
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('signup')

#class SignUpView(generic.CreateView):
    """
    Allows the User to Create a New Account
    """
 #   form_class = SignUpForm
 #  template_name = "registration/admission.html"
 #   success_url = reverse_lazy('apply')

#test starts here
from .models import Application
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application
from django.views.generic import UpdateView


def application_form(request):
    if not request.user.is_authenticated:
        return redirect("accounts/login")
    hide = Application.objects.filter(user=request.user)
    if request.method=="POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            application.user = request.user
            application.save()
            return render(request, "application_form.html")
    else:
        form=ApplicationForm()
    return render(request, "application_form.html", { 'form':form,'hide':hide})

def edit_application(request):
    if not request.user.is_authenticated:
        return redirect("accounts/login")
    try:
        application = request.user.application
    except Application.DoesNotExist:
        application = Application(user=request.user)
    if request.method=="POST":
        form = ApplicationForm(data=request.POST, files=request.FILES, instance=application)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "edit_application.html", {'alert':alert})
    else:
        form=ApplicationForm(instance=application)
    return render(request, "edit_application.html", {'form':form})

def status(request):
    if not request.user.is_authenticated:
        return redirect("accounts/login")
    application = Application.objects.get(user=request.user) 
    return render(request, "status.html", {'application':application})



def handle_admin(request):
    if not request.user.is_superuser:
        return redirect("accounts/login")
    users = User.objects.all().count
    approve = Application.objects.filter(Application_Status='Approved').count
    reject = Application.objects.filter(Application_Status='Rejected').count
    pending = Application.objects.filter(Application_Status='Pending').count
    return render(request, "handle_admin.html", {'approve':approve, 'reject':reject, 'pending':pending, 'users':users})

def users(request):
    if not request.user.is_superuser:
        return redirect("accounts/login")
    allUsers = Application.objects.all()
    return render(request, "users.html", {'allUsers':allUsers})

def student_application(request, myid):
    if not request.user.is_superuser:
        return redirect("accounts/login")
    application = Application.objects.filter(id=myid)
    return render(request, "student_application.html", {'application':application[0]})

class UpdatePostView(UpdateView):
    model = Application
    template_name = 'application_status.html'
    fields = ('Application_Status', 'message',)

def approved_applications(request):
    if not request.user.is_superuser:
        return redirect("accounts/login")
    approved = Application.objects.filter(Application_Status="Approved")
    return render(request, "approved_applications.html", {'approved':approved})

def pending_applications(request):
    if not request.user.is_superuser:
        return redirect("accounts/login")
    pending = Application.objects.filter(Application_Status="Pending")
    return render(request, "pending_applications.html", {'pending':pending})

def rejected_applications(request):
    if not request.user.is_superuser:
        return redirect("accounts/login")
    rejected = Application.objects.filter(Application_Status="Rejected")
    return render(request, "rejected_applications.html", {'rejected':rejected})