from django import forms
from .models import Order
from localflavor.pl.forms import PLPostalCodeField
from django.utils.translation import gettext_lazy as _


class OrderCreateForm(forms.ModelForm):
    postal_code = PLPostalCodeField(label=_("Kod pocztowy"))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']