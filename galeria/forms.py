from django import forms
from galeria.classe_galeria import tipo_de_classes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GaleriaForms(forms.Form):
    classe_galeria = forms.ChoiceField(label='Qual sua avaliacao para esse filme', choices=tipo_de_classes)
    informacoes = forms.CharField(label='Informacoes extras', max_length=200, widget=forms.Textarea, required=False)

class Perfilform(UserCreationForm):
    email = forms.EmailField(max_length=70)

    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']
