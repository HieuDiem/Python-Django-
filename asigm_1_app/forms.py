from django import forms
from asigm_1_app.models import Person

class user_From(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'address', 'mobile_number']