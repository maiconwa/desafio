# Desafio

API para cadastro e consulta de número de cartão completo:

<h4>Preparação do ambiente:</h4>

<ol>

<li>Criar um arquivo .env:</li>

![alt text](image/add_env.png)

<li>Para criar o ambiente virtual do python digite no terminal:</li>
<br>
Windows

    python -m venv venv

Linux & Mac

    python3 -m venv venv

![alt text](image/create_venv.png)

<li>Ative o ambiente virtual:</li>
<br>
Windows:

    # In cmd.exe
    venv\Scripts\activate.bat
    # In PowerShell
    venv\Scripts\Activate.ps1

Linux and MacOS:

    $ source myvenv/bin/activate

![alt text](image/activate_venv.png)

<li>Dentro da pasta desafio é preciso instalar as dependencias do arquivo requirements.txt usando o terminal com o comando:</li>
    
    pip install -r .\requirements.txt

![alt text](image/pip_install1.png)

![alt text](image/pip_install2.png)

Observação: No VS code após instalar as dependencias as vezes é necessário fechar o terminal e o editor de código para que as dependencias sejam reconhecidas. 

<li>Copiar os dados do arquivo .envexample ou criar uma nova SECRET_KEY para o django e adicionar ao arquivo .env:</li>

Envexample:

![alt text](image/add_envexample.png)

Criar uma nova SECRET_KEY:

    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    
![alt text](image/new_secret.png)

Dados copiados para o arquivo .env:

![alt text](image/env_config.png)

<li>Determinar o banco de dados a ser usado no arquivo settings.py em DATABASES. Por padrão para testes o django vem com sqlite configurado.</li>

Exemplo sqlite:

![alt text](image/sqlite_config.png)

Exemplo PostgreSql:

![alt text](image/postgre_config.png)

<li>Com o ambiente virtual ativo é necessario executar as migrações:</li>

Para criar as migrações digite: 

    python .\manage.py makemigrations
    
![alt text](image/makemigrations.png)

Para migrar:

    python .\manage.py migrate
    
![alt text](image/migrate.png)

<li>Com o ambiente virtual ativo é necessário criar o primeiro usuário do django digite:</li>

    python manage.py createsuperuser
    
![alt text](image/superuser.png)

<li>Para iniciar o django com o ambiente virtual ativo digite no terminal:</li>


    python manage.py runserver

<br>

</ol>

<h4>Como usar os endpoints:</h4>

<ol>
    
<li>/api/token/: É utilizado para gerar o token JWT e o refresh.</li>
        
<br>

<li>/api/upload/: É utilizado para enviar o arquivo txt.</li>
    
<br>
    
<li>/api/check/: É utilizado para enviar o número de um ou mais cartões e receber como resposta um identificador unico.</li>
    
<br>
    
</ol>

<strong>IMPORTANTE: Os dados de todas as requisições são salvos em um arquivo de log na pasta logs com o nome de arquivo django.log</strong>

<br>

Observação geral:

<br>

Os exemplos abaixo foram criados com o postman. Com exceção do endpoint /api/token/ os demais exigem que o token seja passado no Bearer Token.

<br>

<ol>
    
<li>Endpoint /api/token/ para conseguir um token JWT e o refresh:</li>


Informar o user e a senha:

![alt text](image/token.png)
obs: Aqui foi utilizado o superusuario para o teste.

<li>Endpoint /api/upload/ para envio do arquivo em formato txt:</li>
<br>
Informar o token no bearer token em authorization:

![alt text](image/access_upload.png)


Informar no Body a key file e adicionar o arquivo de upload no value:

![alt text](image/upload_body.png)


O postman tem acesso limitado ao sistema para o upload de arquivos no body é necessário alterar as configurações ou colocar os arquivos na pasta files como o exemplo abaixo:

![alt text](image/postman_local.png)

<li>Endpoint /api/check/ para enviar um ou mais cartões e receber um identificador unico:</li>
<br>
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

Os dados são salvos no banco de dados, sendo que destes o cartão é criptografado para maior segurança:

Exemplo dados salvos PostgreSql:

![alt text](image/postgresql_data.png)

Exemplo dados salvos SqLite:

![alt text](image/sqlite_data.png)


Agradeço a atenção
