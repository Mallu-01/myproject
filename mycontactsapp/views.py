from django.shortcuts import render
from .models import Contact

def index(request):
    all_contacts = Contact.objects.all()
    return render(request, 'mycontactsapp/index.html', {'contacts': all_contacts})

    
