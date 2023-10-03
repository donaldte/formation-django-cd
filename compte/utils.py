from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage




def send_email_with_html(context, template_name, email_subject, from_email, to_email):
    
    message = render_to_string(template_name, context)
                
    emailsent = EmailMessage(
        email_subject,
        message, 
        from_email,
        to_email,
    )
                
    emailsent.fail_silently = True 
    emailsent.send()