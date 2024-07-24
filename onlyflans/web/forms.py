from django import forms
from django.forms import ModelForm
from .models import ContactForm

class ContactFormForm(forms.Form):#Esto es el formulario creado a partir del modelo ContactForm
    #Según archivo guía, no se declara el atributo contact_form_uuid
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

class ContactFormModelForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']


        