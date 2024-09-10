# trabalho-topicos-especiais-1
Trabalho Python

# Processo de instalação das bibliotecas

## Criando o ambiente virtual
Antes de instalar as extensões é importante criar seu ambiente virtual, para criá-lo precisa rodar o comando abaixo no terminal
```shell
py -3 -m venv .venv
```
Após a pasta .venv ser criada, será necessário habilita-lá com o seguinte comando
```shell
.venv\Scripts\activate
```

## Instalando as bibliotecas
Após a criação do ambiente virtual, é essencial instalar as bibliotecas do flask.

Começando pelo flask, sendo usado para a criação da aplicação no geral
```shell
pip install flask
```
Após o flask, instale o flask-SqlAchemy, para utilização e administração do Banco de Dados
```shell
pip install -U Flask-SQLAlchemy
```
flask-login faz a parte de administração de login na aplicação
```shell
pip install flask-login
```
E por ultimo, Flask-WTF, fazendo a parte de criação de formulários
```shell
pip install -U Flask-WTF
```

# Rodando a aplicação web
Após ter instalado todas as bibliotecas, utilize o comando abaixo para rodar a aplicação

```shell
flask --app main run
```


# Resumo dos comandos 
```shell
py -3 -m venv .venv

.venv\Scripts\activate

pip install flask

pip install flask-login

pip install -U Flask-SQLAlchemy

pip install -U Flask-WTF

flask --app main run
```


