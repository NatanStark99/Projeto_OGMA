from django.shortcuts import render, redirect
from .forms import QuestionarioForm
from .models import Resposta, Pergunta
import pandas as pd
from django.views.decorators.csrf import csrf_exempt  # Apenas se desativar CSRF


from django.shortcuts import render, redirect
from .forms import QuestionarioForm
from .models import Pergunta, Resposta


def questionario_view(request):
    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            # Processa dados pessoais
            dados_pessoais = {
                'nome': form.cleaned_data['nome'],
                'cargo': form.cleaned_data['cargo'],
                'empresa': form.cleaned_data['empresa'],
                'departamento': form.cleaned_data['departamento']
            }

            # Processa respostas (q1 a q10)
            perguntas = Pergunta.objects.all().order_by('id')
            for i, pergunta in enumerate(perguntas, start=1):
                resposta_valor = form.cleaned_data[f'q{i}']

                Resposta.objects.create(
                    pergunta=pergunta,
                    valor=resposta_valor,
                    coordenada_x=calcular_x(pergunta, resposta_valor),
                    coordenada_y=calcular_y(pergunta, resposta_valor),
                    dados_pessoais=dados_pessoais
                )

            return redirect('obrigado')
    else:
        form = QuestionarioForm()

    return render(request, 'questionario/formulario.html', {'form': form})


def obrigado_view(request):
    return render(request, 'questionario/obrigado.html')


def analise_view(request):
    # Converter dados para DataFrame
    respostas = Resposta.objects.all().values()
    df = pd.DataFrame.from_records(respostas)

    # Análise básica (exemplo)
    analise = {
        'total_respostas': len(df),
        'media_por_quadrante': df.groupby('pergunta__quadrante')['valor'].mean().to_dict(),
    }

    return render(request, 'analise/dashboard.html', {'analise': analise})
