from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import LinkModel

class LinkCRUDTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='aluno', 
            email='rafael.silva100@cps.sp.gov.br', 
            password='fatec'
        )
        
        self.link = LinkModel.objects.create(
            titulo="Site da Faculdade", 
            link="https://www.fatec.sp.gov.br", 
            observacao="Link Oficial"
        )

    def test_acesso_negado_para_deslogados(self):
        response = self.client.get(reverse('listar_links'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))

    def test_listar_links_logado(self):
        self.client.login(username='aluno', password='fatec')
        response = self.client.get(reverse('listar_links'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_links.html')
        self.assertContains(response, "Site da Faculdade") 

    def test_cadastrar_link_post(self):
        self.client.login(username='aluno', password='fatec')
        
        dados_novo_link = {
            'titulo': 'Repositório GitHub',
            'link': 'https://github.com',
            'observacao': 'Meus códigos'
        }
        
        response = self.client.post(reverse('cadastrar_link'), dados_novo_link)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('listar_links'))
        
        self.assertTrue(LinkModel.objects.filter(titulo='Repositório GitHub').exists())

    def test_atualizar_link_post(self):
        self.client.login(username='aluno', password='fatec')
        
        dados_atualizados = {
            'titulo': 'Site da FATEC Araras', 
            'link': 'https://www.fatec.sp.gov.br',
            'observacao': 'Novo campus'
        }
        
        response = self.client.post(reverse('atualizar_link', args=[self.link.id]), dados_atualizados)
        self.assertEqual(response.status_code, 302) 
        
        self.link.refresh_from_db()
        self.assertEqual(self.link.titulo, 'Site da FATEC Araras')

    def test_remover_link_post(self):
        self.client.login(username='aluno', password='fatec')
        
        self.assertTrue(LinkModel.objects.filter(id=self.link.id).exists())
        
        response = self.client.post(reverse('remover_link', args=[self.link.id]))
        self.assertEqual(response.status_code, 302)
        
        self.assertFalse(LinkModel.objects.filter(id=self.link.id).exists())