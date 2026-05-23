from django.urls import path
from core.views import login, logout, home, cadastrar_link, listar_links, atualizar_link, remover_link

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('', home, name='home'),
    
    path('links/', listar_links, name='listar_links'),
    path('links/cadastrar/', cadastrar_link, name='cadastrar_link'),
    path('links/editar/<int:id>/', atualizar_link, name='atualizar_link'),
    path('links/excluir/<int:id>/', remover_link, name='remover_link'),
]