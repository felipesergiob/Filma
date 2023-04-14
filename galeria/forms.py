from django import forms
from galeria.classe_galeria import tipo_de_classes


class GaleriaForms(forms.Form):
    classe_galeria = forms.ChoiceField(label='Qual sua avaliacao para esse filme', choices=tipo_de_classes)
    informacoes = forms.CharField(label='Informacoes extras', max_length=200, widget=forms.Textarea, required=False)