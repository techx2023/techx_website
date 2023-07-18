from django.template.loader import render_to_string
from django.core.mail import send_mail

# This function is used to send an email to team when user want contact team
def contact_us_send_mail(subject,fname,message,email):
    # Create a context for the email by rendering the HTML template with the given parameters 
    context = render_to_string("mails/contactus.html", {
                'subject': subject,
                'fname': fname,
                'message': message,
                'email': email
            })
     # Send the mail to the specified email address
    send_mail(subject, context, '',['ernestdossa.9@gmail.com'])