from django import forms
from .models import Pergunta


class QuestionarioForm(forms.Form):
    # Campos fixos para dados pessoais
    nome = forms.CharField(label='Nome Completo', widget=forms.TextInput(attrs={
                           'placeholder': 'Digite seu nome completo', 'class': 'form-control'}), max_length=100, required=True)
    cargo = forms.ChoiceField(
        label='Cargo',
        choices=[
            ('', 'Selecione seu cargo'),
            ('developer', 'Developer'),
            ('coordenador_eventos', 'Coordenador de Eventos'),
            ('analista', 'Analista'),
            ('gerente', 'Gerente'),
            ('supervisor', 'Supervisor'),
            ('consultor', 'Consultor'),
            ('especialista', 'Especialista'),
            ('diretor', 'Diretor'),
            ('outro', 'Outro'),
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}))

    empresa = forms.ChoiceField(
        label='Empresa',
        choices=[
            ('', 'Selecione a empresa'),
            ('empresa_a', 'Globalis'),
            ('empresa_b', 'Ad turismo'),
            ('empresa_c', 'FF36'),
            ('empresa_d', 'Ahoba'),
            ('outra', 'Outra'),
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    departamento = forms.CharField(
        label='Departamento', max_length=100, required=True, widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome completo', 'class': 'form-control'}))

    # Campos dinâmicos para as perguntas
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        perguntas = Pergunta.objects.all().order_by('id')

        # Mapeia os IDs das perguntas para q1, q2, etc.
        for i, pergunta in enumerate(perguntas, start=1):
            self.fields[f'q{i}'] = forms.ChoiceField(
                label=pergunta.texto,
                choices=[
                    ('1', 'Opção 1'),
                    ('2', 'Opção 2'),
                    ('3', 'Opção 3'),
                    ('4', 'Opção 4'),
                    ('5', 'Opção 5'),
                ],
                widget=forms.RadioSelect,
                required=True
            )
