from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        # matches that is contact class in models.py
        rota_id = request.POST['rota_id']
        rota = request.POST['rota']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        # realtor_email = request.POST['# realtor_email']



        contact = Contact(rota=rota, rota_id=rota_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        #send email - needs to be set up in settings.py
        #send_mail()
        #    'enter subject text'
        #   'enter body text (?include message)'
        #    'enter from email address'
        #    [' enter list of email address, (use variables from above'],
        #    fail_silently=False


        messages.success(request, 'Your contact form has been submitted, we will get back to you soon.')
        return redirect('/rotas/+rota_id')


        return
