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

# Funcionamento do programa

Antes de tudo, o usuário deverá rodar os códigos acima.

Logo após, o usuário deverá abrir o endereço que está aparecendo no terminal.

Assim que clicar, irá abrir uma página index no navegador, com as opções de se registrar e logar.

O usuário deve criar uma conta com um login e senha, após isso, com as mesmas informações, conseguirá se logar no site, assim indo para a página do dashboard.

No dashboard, irá ter as opções de criar, editar e excluir uma task. Tanto quando for criar quanto editar, irá ter opções de colocar o nome, uma descrição, indicar se está pendente, em andamento ou concluída.
Quando for editar, também, terá a opção de compartilhar a task para outro usuário, colocando o nome dele no ultimo campo da página de editar.
