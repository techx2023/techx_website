from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail
from techx_project.settings import EMAIL_HOST_USER
from .models import *
from .utils import *




def Erreur404(request, exception):
    return render(request, '404.html')
# This function is used to render the home page
def Index(request):
    # Set title of the page
    title= "Accueil"
    # Get the absolute URI of the current request
    path = request.build_absolute_uri()
    # Create a context dictionary with categories, formations and title
    context = {
        'title':title,
        'path':path
    }
    # Render the home page with the context
    return render(request, 'pages/index.html',context)

# This function is used to render the services page
def OurServices(request):
    # Set title of the page
    title= "Services"
    # Get the absolute URI of the current request
    path = request.build_absolute_uri()
    # Create a context dictionary with categories, formations and title
    context = {
        'title':title,
        'path':path
    }
    # Render the services page with the context
    return render(request, 'pages/services.html',context)

# This function is used to contact the team
def contactUs(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Check if all the required fields are filled
        if (request.POST['email'] and 
            request.POST['fname'] and
            request.POST['subject'] and
            request.POST['message']):
            # Get the data from the request
            email= request.POST['email']
            fname= request.POST['fname']
            subject= request.POST['subject']
            message= request.POST['message']
            # Create a ContactUs object with the data
            contact = Contact.objects.create(email=email,fname=fname, subject=subject, message=message)
            # Save the object
            contact.save()
            # Send the mail
            contact_us_send_mail(subject,fname,message,email)
            # Show success message
            messages.success(request, 'Votre message a été bien transmit à notre équipe. Nous vous revenons d\'ici peu')
            # Redirect to contact page
            return redirect('contactez-nous')
        else:
            # Show error message
            messages.error(request,'formulaire invalid')
            # Redirect to contact page
            return redirect('contactez-nous')
    # Set the title of the page
    title = "Contactez-Nous"
    # Get the absolute URI of the current request
    path = request.build_absolute_uri()
    # Set the context for the page
    context = {
        'title': title,
        'path': path,
    }
    # Render the page
    return render(request, 'pages/contact.html',context)

# This function is used to render the about page
def About(request):
    # Set title of the page
    title= "A propos"
    # Get the absolute URI of the current request
    path = request.build_absolute_uri()
    # Create a context dictionary with categories, formations and title
    context = {
        'title':title,
        'path':path
    }
    # Render the about page with the context
    return render(request, 'pages/about.html', context)

# This function is used to render the realisation page
def Realisation(request):
    # Set title of the page
    title= "A propos"
    # Get the absolute URI of the current request
    path = request.build_absolute_uri()
    # Create a context dictionary with categories, formations and title
    context = {
        'title':title,
        'path':path
    }
    # Render the realisation page with the context
    return render(request, 'pages/realisation.html', context)
