from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ContatoForm
from .models import Servico, Funcionario, Features

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

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

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        print(form.errors)
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)