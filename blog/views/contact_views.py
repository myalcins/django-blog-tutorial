from django.shortcuts import redirect, render
from blog.forms import ContactForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages


class ContactFormView(FormView):
    template_name = 'pages/form.html'
    form_class = ContactForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message sended succesfully.")
        return redirect(self.success_url)
    
