# api-cadastro-veiculos
API Restfull para cadastros de veiculos e ativacao com autenticacao


# Descrição do projeto para estudo

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
  - O candidato deverá fornecer uma documentação clara e completa da API, descrevendo todos os endpoints, parâmetros, respostas e exemplos de uso.
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
   - criar o projetor em docker
   - usar fastapi, usar sqlite
   - documentar 
   - criar o swagger
   - usar o uvicorn
