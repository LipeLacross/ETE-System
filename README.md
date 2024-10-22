## 🌐 [English Version of README](README_EN.md)

# ETE-System

Este projeto é uma aplicação web desenvolvida em Django. Ela possui várias funcionalidades como gerenciamento de ativos, controle de filtros, dashboard analítico, entre outros módulos voltados para uma gestão eficiente de recursos e estatísticas aleatórias.

## 🔨 Funcionalidades do Projeto

- Gerenciamento de ativos, incluindo a criação, edição e visualização.
- Controle e monitoramento de filtros específicos de aeradores.
- Análise e visualização de dados em dashboards interativos.
- Controle histórico e gerenciamento de informações no sistema.
- Autenticação de usuários e controle de permissões.

### Exemplo Visual do Projeto

![chrome-capture-2024-10-21](https://github.com/user-attachments/assets/55317e7c-837e-4d84-8cca-2320c2b2f1d9)

## ✔️ Técnicas e Tecnologias Utilizadas

- **Django**: Framework para desenvolvimento web em Python.
- **HTML/CSS**: Estrutura e estilização das páginas.
- **Tailwind CSS**: Framework CSS utilitário para estilização rápida e responsiva.
- **Banco de Dados SQLite**: Utilizado para persistência de dados localmente durante o desenvolvimento.
- **Bootstrap**: Estilização e componentes reutilizáveis para criar layouts responsivos (opcional).
- **JavaScript**: Para interatividade e manipulação do DOM.

## 📁 Estrutura do Projeto

- **core/**: Contém a lógica principal do projeto.
    - **migrations/**: Arquivos de migração para configurar e atualizar o banco de dados.
    - **models.py**: Definição dos modelos de dados.
    - **admin.py**: Configuração do painel administrativo.
    - **templates/**: Contém os templates HTML utilizados pelas views.
        - **baseLogin.html**: Template base para a página de login.
        - **dashboard/**: Templates específicos para os dashboards de análise, ativos, controle e outros módulos.
    - **views.py**: Contém as funções de visualização que renderizam os templates HTML.
    - **urls.py**: Definição das rotas do aplicativo.

- **puddle/**: Configurações gerais do projeto.
    - **settings.py**: Configurações do Django, como banco de dados, aplicativos instalados e middlewares.
    - **urls.py**: Definição das rotas principais do projeto.
    - **wsgi.py e asgi.py**: Configurações para a execução do projeto.

- **db.sqlite3**: Banco de dados SQLite utilizado durante o desenvolvimento.

- **requirements.txt**: Lista de dependências necessárias para rodar o projeto.

## 🚠 Abrir e rodar o projeto

Para iniciar o projeto localmente, siga os passos abaixo:

1. **Certifique-se de que o Python está instalado**:
    - O [Python](https://www.python.org/) é necessário para rodar o projeto. Você pode verificar se já o tem instalado com:

   ```bash
   python --version
   ```

    - Se não estiver instalado, baixe e instale a versão mais recente.

2. **Clone o Repositório**:
    - Copie a URL do repositório e execute o comando abaixo no terminal:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

3. **Instale as dependências**:
    - Navegue até o diretório do projeto clonado e instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**:
    - Execute as migrações para configurar o banco de dados:

   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário**:
    - Para acessar o painel administrativo, crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor**:
    - Para iniciar o servidor local, utilize o comando:

   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação**:
    - Abra o navegador e acesse `http://127.0.0.1:8000/` para visualizar a aplicação rodando.

## 🌐 Deploy

Para fazer o deploy do projeto, você pode utilizar plataformas como [Heroku](https://www.heroku.com/), [DigitalOcean](https://www.digitalocean.com/), ou [AWS](https://aws.amazon.com/). Certifique-se de configurar as variáveis de ambiente corretamente e definir o banco de dados de produção, como PostgreSQL ou MySQL.
