from django.shortcuts import render

def analise_view(request):
    return render(request, 'analise/dashboard.html', {})