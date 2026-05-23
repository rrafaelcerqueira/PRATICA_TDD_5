# Prática TDD 5 - LinkPedia

Desafio técnico para os alunos da disciplina "Desenvolvimento Web 3" - FATEC.

Este projeto consiste numa aplicação web em Django para gestão de links (LinkPedia), desenvolvida com foco em Test-Driven Development (TDD) e cobertura de testes acima de 90%.

---

## 🛠️ Como executar o projeto

### No ambiente Windows:

```console
git clone [https://github.com/rrafaelcerqueira/Pratica_TDD_5.git](https://github.com/rrafaelcerqueira/Pratica_TDD_5.git)
cd Pratica_TDD_5/
python -m venv venv
cd venv/scripts
activate.bat
cd ../..
pip install -r requirements.txt
cd linkpedia/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py createsuperuser
python manage.py runserver
```

### No ambiente Linux:

```console
git clone [https://github.com/rrafaelcerqueira/Pratica_TDD_5.git](https://github.com/rrafaelcerqueira/Pratica_TDD_5.git)
cd Pratica_TDD_5/
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd linkpedia/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py createsuperuser
python manage.py runserver
```

---

### Credenciais padrão para teste inicial:

* Username: aluno
* E-mail: seu e-mail institucional
* Password: fatec

---

### 🏁 Estado do Projeto

#### Sprint 1 - Concluída ✅
A expectativa inicial do projeto foi o desenvolvimento do sistema de autenticação.

O login somente ocorre com o e-mail institucional @cps.sp.gov.br.

Proteção de rotas básicas e funcionalidade de Logout implementadas.

---

#### Sprint 2 - Concluída ✅
O foco da segunda sprint foi desenvolver um cadastro de links com as operações de CRUD, totalmente protegido e testado.

Com base no modelo LinkModel estabelecido, as seguintes funcionalidades foram implementadas e validadas:

✅ Criar formulário para o modelo LinkModel utilizando ModelForms.
✅ Cadastrar Link (Create)
✅ Listar Links (Read)
✅ Atualizar Link (Update)
✅ Remover Link (Delete)
✅ Proteção de Rotas: Todas as funcionalidades do CRUD estão protegidas pelo decorador @login_required, garantindo acesso exclusivo a utilizadores autenticados.

---

### 🎨 Melhoria de Interface (UI/UX)
Além dos requisitos técnicos, a interface da aplicação foi totalmente redesenhada. O design base do Bootstrap foi aprimorado com técnicas de Glassmorphism, transições suaves, sombras modernas e um painel de ações intuitivo, oferecendo uma experiência de utilizador (UX) de nível premium.

---

### 🧪 Cobertura de Testes (TDD)

![Teste](/linkpedia/Testes.png)
