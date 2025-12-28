from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

from core.views import ContatoForm

class IndexViewTestCas(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Jone Oliveira',
            'email': 'jone_olv@gmail.com',
            'assunto': 'Um assunto',
            'mensagem': 'Testando mensagem'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Jone Oliveira',
            'email': '',
            'assunto': 'Meu assunto',
            'mensagem': '',
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)