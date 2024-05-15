from django.shortcuts import render,redirect
from member.models import Contact
from django.http import HttpResponse
from django.conf import settings
import os

def IndexPage(request):
    return render(request,'index.html')

def ContactView(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        contact = Contact.objects.create(name=name,email=email,message=message)
        
        return redirect('index')
    else:
        message = "Sorry! Please enter again your message"
        return render(request,'index.html',{'msg':message})
    
def download_cv(request):
    # Path to the resume file
    cv_path = os.path.join(settings.BASE_DIR,'media/RESUME.pdf')
    
    # Open the file in binary mode
    with open(cv_path,'rb') as f:
        # Prepare the response
        response = HttpResponse(f.read(), content_type='application/pdf')
        # Set the Content-Disposition header to force download
        response['Content-Disposition'] = 'attachment; filename="RESUME.pdf"'
        return response