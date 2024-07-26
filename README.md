# desafio

API para cadastro e consulta de número de cartão completo:

<h4>Setup do ambiente:</h4>

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

envexample
![alt text](image/add_envexample.png)

criar uma nova SECRET_KEY:
Com ambiente virtual ativado digite: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
![alt text](image/new_secret.png)

dados copiados para o arquivo .env:
![alt text](image/env_config.png)

<li>Determinar o banco de dados a ser usado no arquivo settings.py em DATABASES. Por padrão para testes o django vem com sqlite configurado.</li>

Exemplo sqlite:
![alt text](image/sqlite_config.png)

Exemplo PostgreSql:
![alt text](image/postgre_config.png)

<li>Com o ambiente virtual ativo é necessario executar as migrações:</li>

Para criar as migrações digite: python .\manage.py makemigrations
![alt text](image/makemigrations.png)

Para migrar: python .\manage.py migrate
![alt text](image/migrate.png)

<li>Agora é preciso adicionar o primeiro usuário do sistema:</li>

Ainda no terminal com o ambiente virutual ativo digite: python manage.py createsuperuser
![alt text](image/migrate.png)

Ainda no terminal com o ambiente virtual ativo digite: python manage.py createsuperuser
![alt text](image/superuser.png)

</ol>


<h4>Como usar a API:</h4>
São três endpoints:
<ol>
<li>Endpoint /api/token/:</li>
    É utilizado para gerar o token JWT e o refresh.
<li>Endpoint /api/upload/:</li>
    É utilizado para enxiar o arquivo txt.
<li>Endpoint /api/check/:</li>
    É utilizado para enviar o número de um ou mais cartões e receber como resposta um identificador unico.
</ol>
<br>
Observação geral:
Os exemplos abaixo foram criados com o postman. Com exceção do endpoint /api/token/ os demais exigem que o token seja passado no Bearer Token.

<ol>
<li>Endpoint /api/token/ para conseguir um token JWT e o refresh:</li>

Informar o user e a senha:
![alt text](image/token.png)
obs: Aqui foi utilizado o superusuario para o teste.

<li>Endpoint /api/upload/ para envio do arquivo em formato txt:</li>

Informar o token no bearer token em authorization:
![alt text](image/access_upload.png)


Informar no Body a key file e adicionar o arquivo de upload no value:
![alt text](image/upload_body.png)


O postman tem acesso limitado ao sistema para o upload de arquivos no body é necessário alterar as configurações ou colocar os arquivos na pasta files como o exemplo abaixo:
![alt text](image/postman_local.png)

<li>Endpoint /api/check/ para enviar um ou mais cartões e receber um identificador unico:</li>

Assim como na chamada anterior é necessário informar o token no bearer token em authorization:
![alt text](image/check_token.png)


Nesta chamada é possivel informar um ou mais numeros de cartões e a resposta será um identificador unico:
![alt text](image/check_body.png)

Exemplo de body:

[
    {
        "numero_cartao": "4456897999999999"
    },
    {
        "numero_cartao": "4456897912999999"
    }
]

</ol>