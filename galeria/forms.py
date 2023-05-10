from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from galeria.models import Comment

class Perfilform(UserCreationForm):
    email = forms.EmailField(max_length=70)

    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AvaliacaoForm(forms.Form):
    estrelas = forms.ChoiceField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas')])

