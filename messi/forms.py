from django import forms


from .models import contact_admin

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact_admin
        fields = ['iname', 'iprice', 'imessage' , 'iimage']