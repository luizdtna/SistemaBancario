###Sistema bancario 


####Para executar o projeto:

* Crie uma virtual enviroment:
    * linux: python3 -m venv venv
    * windows: py -m venv env
    
* instale as dependências:
    * pip install -r requirements.txt
  
* na raiz do sistema, crie um arquivo e o nomeie de .env , adicione uma SECRET_KEY aleatória e DEBUG=True, exemplo:
    * SECRET_KEY=afjsfknsdlfkncanklc
    * DEBUG=True 

* Execute as migrações:
    * python manage.py migrate
  
* Abra no navegador o seguinte endereço:
  * Tela principal: localhost:8000/
  * Tela do gerente: localhost:8000/gestao/