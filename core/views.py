from django.views.generic import TemplateView
from .models import Servico, Funcionario, Features

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        servicos = Servico.objects.order_by('?')
        funcionarios = Funcionario.objects.order_by('?')
        features = Features.objects.all()

        meio = len(features) // 2

        context['servicos'] = servicos
        context['funcionarios'] = funcionarios
        context['features_left'] = features[:meio]
        context['features_right'] = features[meio:]

        return context
