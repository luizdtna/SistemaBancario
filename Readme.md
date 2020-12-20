###Sistema bancario 

Developed by: Luiz Araujo e Daniela Soares

####Para executar o projeto:


* Crie uma virtual enviroment:
    * linux: python3 -m venv venv
    * windows: py -m venv venv
  
* Inicia a virtual enviroment:
    * linux: source python venv/bin/activate
    * windows: .\env\Scripts\activate
  
* instale as dependências:
    * pip install -r requirements.txt
  
* na raiz do sistema, crie um arquivo e o nomeie de .env , adicione uma SECRET_KEY aleatória e DEBUG=True, exemplo:
    * SECRET_KEY=afjsfknsdlfkncanklc
    * DEBUG=True 

* Execute as migrações:
    * python manage.py migrate
  
* Abra no navegador o seguinte endereço:
  * Tela do gerente (para criar novos clientes): localhost:8000/painel/gestao/ 
  * Tela principal (para logar como um cliente): localhost:8000/