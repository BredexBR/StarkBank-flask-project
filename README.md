# StarkBank-flask-project
Foi necessário baixar a ferramenta [ngrok](https://ngrok.com/), como também o flask. Para instalar flask **dentro de seu repositório** faça:
> $ pip install flask

O código da chave privada esta como variável de ambiente. Então é necessário você gerar sua chave privada e adicionar ao código pelo terminal:
>  $ PRIVATE_KEY = "SUA-CHAVE-PRIVADA"

Para roda o projeto inicie o ngrok dentro de sua pasta
> $ ngrok/ngrok.exe http 5000

E para executar o projeto basta inserir no terminal:
> $ python setup.py
