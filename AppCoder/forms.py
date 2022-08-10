from django import forms


class SociosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    NumeroDeSocio= forms.IntegerField()    