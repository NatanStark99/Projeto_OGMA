from django.contrib import admin
from django.urls import path
from questionario import views as questionario_views
from analise import views as analise_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', questionario_views.questionario_view, name='questionario'),
    path('obrigado/', questionario_views.obrigado_view, name='obrigado'),
    path('analise/', analise_views.analise_view, name='analise'),
]