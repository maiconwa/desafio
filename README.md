# desafio

API para cadastro e consulta de número de cartão completo:

<h4>Setup do ambiente</h4>

<ol>

<li>Criar um arquivo .env:</li>

![alt text](image/add_env.png)

<li>Criar uma pasta de ambiente virtual do python com python -m venv venv no windows ou python3 -m venv venv no linux:</li>

![alt text](image/create_venv.png)

<li>Ativar o ambiente virtual no cmd venv\Scripts\activate.bat, no powershell venv\Scripts\Activate.ps1 ou no linux source myvenv/bin/activate</li>

![alt text](image/activate_venv.png)

<li>Dentro da pasta desafio é preciso instalar as dependencias do arquivo requirements.txt usando o terminal com o comando pip install -r .\requirements.txt</li>

![alt text](image/pip_install1.png)

![alt text](image/pip_install2.png)

<li>copiar os dados do arquivo .envexample ou criar uma nova SECRET_KEY para o django e adicionar ao arquivo .env:</li>

<strong>envexample</strong>

![alt text](image/add_envexample.png)

<strong>criar uma nova SECRET_KEY</strong>
Com ambiente virtual ativado digite: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

![alt text](image/new_secret.png)

<strong>dados copiados para o arquivo .env</strong>

![alt text](image/env_config.png)

<li>Determinar o banco de dados a ser usado no arquivo settings.py em DATABASES. Por padrão para testes o django vem com sqlite configurado.</li>

<strong>exemplo sqlite</strong>

![alt text](image/sqlite_config.png)

<strong>exemplo PostgreSql</strong>

![alt text](image/postgre_config.png)

<li>Com o ambiente virtual ativo é necessario executar as migrações.</li>

<strong>Para criar as migrações digite: python .\manage.py makemigrations<strong>

![alt text](image/makemigrations.png)

<strong>Para migrar: python .\manage.py migrate<strong>

![alt text](image/migrate.png)

<li>Agora é preciso adicionar o primeiro usuário do sistema:</li>

<strong>Ainda no terminal com o ambiente virutual ativo digite: python manage.py createsuperuser<strong>

![alt text](image/migrate.png)

<strong>Ainda no terminal com o ambiente virtual ativo digite: python manage.py createsuperuser<strong>

![alt text](image/superuser.png)

<ol>