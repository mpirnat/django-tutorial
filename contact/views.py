from django.shortcuts import render
from django.core.mail import send_mail

from contact.forms import ContactForm


def contact_form(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        send_mail(form.cleaned_data['subject'], form.cleaned_data['message'],
                form.cleaned_data['sender'], ['codesmash@example.com'])

    return render(request, 'contact/form.html', {
        'form': form,
    })
