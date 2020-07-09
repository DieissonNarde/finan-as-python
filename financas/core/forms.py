from django import forms
from .models import Transacao, Grupo

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ( 'tipo', 'descricao', 'valor', 'data', 'status')

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ('nome', 'membros')