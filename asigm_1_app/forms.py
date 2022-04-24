from django import forms
from asigm_1_app.models import Person

# ke thua tu class Peron trong model
class user_From(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'address', 'mobile_number']

# tao 1 cai form moi tu Form
class userForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    address = forms.CharField(max_length=100)
    mobile_number = forms.CharField()