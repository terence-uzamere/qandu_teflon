from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
  template_name = 'home.html'

class ContactCreateView(CreateView):
  model = ContactForm
  template_name = "contact/contact_form.html"
  fields = ['title', 'first_name', 'last_name', 'email_Address', 'message']
  success_url = reverse_lazy('success')

class About_Me(TemplateView):
  template_name = "about_me.html"

class Success(TemplateView):
  template_name = "success.html"



