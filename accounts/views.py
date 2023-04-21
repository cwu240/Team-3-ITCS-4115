from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from django.contrib import messages

def profile_page(request):
    return render(request, "registration/profile_page.html", {})

def submit(request):
    if(request.POST):
        current_user = request.user
        profile_data = request.POST.dict()
        gender = profile_data.get("gender")
        first_name = profile_data.get("first_name")
        last_name = profile_data.get("last_name")
        phone_number = profile_data.get("phone_number")
        email = profile_data.get("email")
        dob = profile_data.get("birthdate")
        print(dob)

        print(gender, first_name, last_name, phone_number, email)

        current_user.gender = gender
        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.phone_number = phone_number
        current_user.email = email
        current_user.dob = dob

        current_user.save()
        
        messages.success(request, 'profile update success')
        return render(request, "registration/profile_page.html", {})
    else:
        messages.error(request, 'profile update failure')
        return render(request, "registration/profile_page.html", {})


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"