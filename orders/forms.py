from django import forms
# from localflavor.us.forms import USZipCodeField
from .models import Order

class OrderCreateForm(forms.ModelForm):
    # postal_code = USZipCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'postal_code', 'city']
    