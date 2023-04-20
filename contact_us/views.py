from django.shortcuts import render
from django.contrib import messages
from .models import Contact

# Create your views here.
# Create your views here.
def contact_us(request):
   return render(request, "contact_us/contact_us.html", {})


def submit(request):
    if(request.POST):
        current_user = request.user
        contact_data = request.POST.dict()
        name = contact_data.get("name")
        email = contact_data.get("email")
        subject = contact_data.get("subject")
        message = contact_data.get("message")
        print(name, email, subject, message)

        
        contact_instance = Contact.objects.create( customer_id = current_user, name=name, email = email, subject = subject, message = message)
        contact_instance.save()

        messages.success(request, 'your message has been received')
        return render(request, "contact_us/contact_us.html", {})
    else:
        messages.error(request, 'there was an error in your message')
        return render(request, "contact_us/contact_us.html", {})

