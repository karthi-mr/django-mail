from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader


def index(request) -> HttpResponse: # type: ignore
    html_message = loader.render_to_string(
        'email_sender_app/message.html',
        {
            # TODO: Enter the recipient name
            'name': 'mkarthim2212',
            # TODO:  Update with your own body
            'body': 'This email is to verify whether we can send email in Django from Gmail account.',
            # TODO: Update the signature
            'sign': 'Sender',
        })
    send_mail(
        'Congratulations!',
        'You are lucky to receive this mail.',
        'me.officeuse@gmail.com',  # TODO: Update this with your mail id
        ['mkarthim2212@gmail.com'],  # TODO: Update this with the recipients mail id
        html_message=html_message,
        fail_silently=False,
    )

    return HttpResponse("Mail Sent!!")