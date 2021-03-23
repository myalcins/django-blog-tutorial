from django.shortcuts import redirect, render
from blog.forms import ContactForm
from blog.models import Contact


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form,
        }
        return render(request, 'pages/contact.html', context=context)