<p align="center">
  <img src="http://www.ideiadofuturo.com.br/img/logo_ideia.png" width="120" title="ideia"  alt="ideia">
</p>



# api-cadastro-veiculos
API Restfull para cadastros de veiculos e ativacao com autenticacao


## Descrição do projeto para estudo

 1.	Criação da API RESTful: 
  -	caso de estudo: criar uma API RESTful que permita a listagem de veículos.
  -	A API deve ter os seguintes endpoints: 
   - GET /veiculos: Retorna a lista de veículos.
   - POST /veiculos: Cria um novo veículo.
   - GET /veiculos/: Retorna os detalhes de um veículo específico.
   - PUT /veiculos/: Atualiza o status de um veículo para "CONNECTADO" ou "DESCONECTADO".
   - DELETE /veiculos/: Exclui um veículo.

 2.	Autenticação e Autorização: 
  - implementar um mecanismo de autenticação e autorização para a API. -> criar Bearer token -> user/senha
  - Apenas usuários autenticados e autorizados devem ter acesso aos endpoints.

 3.	Documentação da API: 
  - deve ter documentação clara e completa da API, descrevendo todos os endpoints, parâmetros, respostas e exemplos de uso.
  - A documentação deve ser acessível e compreensível para outros desenvolvedores.
   - usar Swagger

 4.	Testes Unitários: 
  - O candidato deverá escrever testes unitários para garantir a qualidade e o correto funcionamento da API.
  - Os testes devem cobrir os principais cenários de uso e verificar se os endpoints estão retornando as respostas esperadas.
   - criar teste com unittest

 5.	Execução local do serviço: 
 - documentar instruções claras para executar o projeto localmente e testar os endpoints.
 - O serviço deve ser executado de forma a expor os endpoints localmente para que possa realizar as operações de CRUD. -> automatize com make

 - dicas:
   - usar bd local: sqlite
   - criar o projeto em docker
   - usar fastapi, usar sqlite
   - documentar 
   - criar o swagger
   - usar o uvicorn


## Depêndencias

 - python 3.11
 - Para mais informações de requisitos e configurações iniciais podem ser verificados no arquivo [setup.py](setup.py)

## Desenvolvimento

Para facilitar o uso deste projeto, foi utilizado o Makefile.

 - para acesso ao help do make basta usar o comando abaixo
	- ```bash
		make help
		```

### instruções para iniciar o ambiente de dev manualmente na sua máquina

 - realize o clone do projeto
	- ```bash
		git clone https://github.com/eniodefarias/api-cadastro-veiculos.git
		```
 - entre no dir do projeto
	- ```bash
		cd api-cadastro-veiculos
		```

#### Método 1: executando o python localmente



 - criar o ambiente virtual:
	- ```bash
		python3 -m venv .venv
		```

 - ativar o ambiente virtual:
	- ```bash
		source .venv/bin/activate
		source ~/.bashrc
		```

 - instale os pacotes necessário para o setup:
	- ```bash
		make setup
		```

 - execute o app:
	- ```bash
		make api
		```
 
 - abra a url do swagger com a documetação da api
    - [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

#### Método 2: usando docker
 - tenha o docker instalado em sua máquina

 - realize a buida da imagem
	- ```bash
		make build
		```

 - execute o conteiner do projeto
	- ```bash
		make run 
		```
 - abra a url do swagger com a documetação da api
    - [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

***

## documentação das Rotas dos endpoints

### GET: /healthcheck
  - rota que informa se a app está online


### POST: /token
  - rota para obter o token de autenticação

### GET: /protected
  - rota para confirmar a autenticação do token se é válido

### POST: /register
 - rota para adicionar um novo usuário

### /veiculos

#### GET: /veiculos
 - mostra todos os veiculos cadastrados

#### POST: /veiculos 
  - cria um novo veiculo

#### GET: /veiculos /<id>
  - mostra os dados do veiculo indicado no <id>

#### PUT: /veiculos/<id>
  - serve para alterar o status do veiculo

#### DELETE: /veiculos/<id>
  - deleta um veiculo veiculo
  
******

# melhoria para o futuro

 - criar teste unitarios
 - criar metodo de alteração de dados do usuário
 - criar uma tabela de cliente para associar aos veiculos
 - criar um frontend basico

  

<p align="center">
  <img src="http://www.ideiadofuturo.com.br/img/logo_ideia.png" width="120" title="ideia"  alt="ideia">
</p>