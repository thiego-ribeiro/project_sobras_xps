# 🧱 Sistema de Sobras — Projeto Django

Este projeto foi desenvolvido em **Python/Django** e utiliza **SQLite3** como banco de dados.  
O objetivo é permitir o **cadastro e gerenciamento de sobras de materiais**, incluindo upload de imagens, através de uma interface web simples e eficiente.

---

## 🚀 Pré-requisitos

Antes de tudo, verifique se o **Python** está instalado no seu computador.

### 🔍 Verificar instalação

Abra o terminal (Prompt de Comando, PowerShell ou Git Bash) e execute:

python --version

Se aparecer algo como `Python 3.x.x`, o Python já está instalado.  
Caso contrário, baixe o instalador oficial em: https://www.python.org/downloads/

Durante a instalação, **marque a opção “Add Python to PATH”**.

---

## ⚙️ Clonando o projeto

1. Acesse o repositório no GitHub.  
2. Clique no botão verde **“Code”** e copie o link HTTPS.  
3. No terminal, vá até a pasta onde deseja salvar o projeto e execute:

git clone https://github.com/thiego-ribeiro/sobras_project.git
cd sobras_project

---

## 🧩 Criando o ambiente virtual

Crie um ambiente virtual para isolar as dependências do projeto:

python -m venv venv

Ative o ambiente virtual:

**Windows:**

venv\Scripts\activate

**Linux/Mac:**

source venv/bin/activate

Você saberá que o ambiente está ativo quando aparecer `(venv)` antes do caminho no terminal.

---

## 📦 Instalando as dependências

Com o ambiente virtual ativo, instale as bibliotecas necessárias para o projeto:

pip install django pillow

Se existir um arquivo `requirements.txt`, você pode instalar tudo de uma vez com:

pip install -r requirements.txt

> 💡 **Observação:** O pacote **Pillow** é essencial para o funcionamento dos campos de imagem (`ImageField`) no Django.  
> Se você receber o erro `Cannot use ImageField because Pillow is not installed`, rode novamente: pip install pillow com o ambiente virtual ativado.

---

## 🗃️ Configurando o banco de dados (SQLite3)

O projeto utiliza **SQLite3**, que já vem embutido no Python — portanto, **não é preciso instalar nada adicional**.

Para criar e atualizar o banco de dados, execute:

python manage.py makemigrations
python manage.py migrate

Esses comandos geram as tabelas no arquivo `db.sqlite3` de acordo com os modelos definidos em `models.py`.

---

## 👩‍💻 Criando um superusuário (opcional)

Para acessar o painel administrativo do Django, crie um superusuário:

python manage.py createsuperuser

Siga as instruções para definir **nome de usuário**, **e-mail** e **senha**.  
Depois, acesse o painel administrativo em: http://127.0.0.1:8000/admin

---

## ▶️ Executando o servidor

Para iniciar o servidor de desenvolvimento, use:

python manage.py runserver

O sistema estará disponível em: http://127.0.0.1:8000/

---

## 🖼️ Upload de Imagens

Este projeto utiliza campos `ImageField`, portanto o pacote **Pillow** é obrigatório.  
Se ocorrer o erro:

Cannot use ImageField because Pillow is not installed

Execute novamente:

pip install pillow

Certifique-se de que o ambiente virtual está ativado antes de rodar os comandos do Django.

---

## 🧾 Gerando o arquivo requirements.txt (opcional)

Se você quiser registrar todas as dependências do projeto, execute:

pip freeze > requirements.txt

Isso cria (ou atualiza) o arquivo `requirements.txt` contendo todas as bibliotecas instaladas, facilitando para que outras pessoas possam reproduzir o ambiente.

---

## 🧹 Limpando e recriando o banco de dados (opcional)

Caso queira recomeçar o banco de dados do zero ⚠️ **Atenção:** Isso apaga todos os dados existentes!

**Windows:**

del db.sqlite3
python manage.py migrate --run-syncdb

**Linux/Mac:**

rm db.sqlite3
python manage.py migrate --run-syncdb

---

## 📁 Estrutura básica do projeto

sobras_project/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── materiais/                # Aplicativo principal do sistema
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── static/                   # Arquivos estáticos (CSS, JS, imagens)
│   └── style.css
│
└── sobras_project/           # Configurações principais do Django
    ├── settings.py
    ├── urls.py
    └── wsgi.py

---

## 💡 Dicas úteis

- Se o comando `python` não funcionar, tente:

py manage.py runserver

- Sempre **ative o ambiente virtual** antes de instalar pacotes ou rodar o servidor.

- Para listar todas as migrations aplicadas:

python manage.py showmigrations

- Para verificar se o projeto tem problemas de configuração:

python manage.py check

- Se aparecer erro de módulo não encontrado:

pip install -r requirements.txt

---

## 👨‍💻 Autor

**Thiego Ribeiro**  
Estudante de **Análise e Desenvolvimento de Sistemas (ADS)**  
Autodidata em programação e entusiasta de projetos open-source.

GitHub: https://github.com/thiego-ribeiro
