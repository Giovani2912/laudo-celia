from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.tipo_viagem import tipos_de_classes

class PassagemForms(forms.Form):
    nome_proprietário = forms.CharField(label='Nome do Proprietário', max_length=100)
    cpf_proprietario = forms.CharField(label='CPF do proprietário', max_length=15)
    rua = forms.CharField(label='Rua', max_length=100)
    bairro = forms.CharField(label='Bairro', max_length=100)
    numero = forms.IntegerField(label='Número')
    entrada = forms.CharField(label='Descreva a entrada', max_length=500, required=False)
    sala = forms.CharField(label='Descreva a sala', max_length=500, required=False)
    copa = forms.CharField(label='Descreva a copa', max_length=500, required=False)
    cozinha = forms.CharField(label='Descreva a cozinha', max_length=500, required=False)
    corredor_interno = forms.CharField(label='Descreva o corredor interno', max_length=500, required=False)
    wc_social = forms.CharField(label='Descreva o WC social', max_length=500, required=False)
    dormitorio_um = forms.CharField(label='Descreva o primeiro dormitório', max_length=500, required=False)
    dormitorio_dois = forms.CharField(label='Descreva o segundo dormitório', max_length=500,required=False)
    dormitorio_tres = forms.CharField(label='Descreva o terceiro dormitório', max_length=500, required=False)
    dormitorio_quatro = forms.CharField(label='Descreva o quarto dormitório', max_length=500, required=False)
    suite = forms.CharField(label='Descreva a suíte', max_length=500, required=False)
    wc_suite = forms.CharField(label='Descreva o WC da suíte', max_length=500, required=False)
    corredor_externo = forms.CharField(label='Descreva o corredor externo', max_length=500, required=False)
    piso_superior = forms.CharField(label='Descreva o piso superior', max_length=500, required=False)
    observacoes = forms.CharField(
        label='Observações',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    nome_locatario = forms.CharField(label='Nome do locatário', max_length=100)
    cpf_locatario = forms.CharField(label='CPF do locatário', max_length=15)
    nome_fiador = forms.CharField(label='Nome do fiador', max_length=100)
    cpf_fiador = forms.CharField(label='CPF do fiador', max_length=15)
    


    

    