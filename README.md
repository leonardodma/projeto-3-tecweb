# Music Identifier
Print da página inicial do site
![plot](https://github.com/leonardodma/projeto-3-tecweb/blob/main/printScreenSite/homeSite.PNG)

Print de uma música exemplo encontrada
![plot](https://github.com/leonardodma/projeto-3-tecweb/blob/main/printScreenSite/musicSite.PNG)

## Integrantes

* Leonardo Duarte Malta de Abreu
* Rafael Seicali Malcervelli

## Projeto

Projeto desenvolvido para o curso de Tecnologias Web do <a href="https://www.insper.edu.br/en/"><b>Insper</b></a>, com a temática livre, mantendo especificações de utilizar alguma tecnologia web, seja voltada para o front ou para o back-end. No caso do projeto, utilizaremos do back-end para realizar requisições com algumas APIs de reconhecimento de voz, autorização da utilização do microfone pela página web e o front-end.

## Sobre

Identifique alguma música de interesse utilizando o microfone do seu navegador! Nosso site permite a identificação do áudio tocado por meio da utilização de uma API chamada AudD (<https://audd.io/>).


## Planejamento 

- [x] Conseguir respostas coerentes da API da AudD (2 dias)
- [x] Conseguir, por meio da aplicação, gravar o áudio do usuário (3 dias)
- [x] Obter url do vídeo do youtube da música pesquisada (2 dias)
- [X] FrontEnd da aplicação (1 semana)
- [X] Correção de erros e Deploy (2 dia)


## URL da aplicação

<https://music-finder-app.herokuapp.com/>


## Executar a aplicação localmente

* Clonar o repositório
* Mudar para a branch de teste local: `$ git chekout testeLocal`
* Na raiz do projeto, executar: 

1) `$ python3 -m venv NOME_DA_PASTA_DO_VENV`, para criar ambiente virtual em python3;

2) `$ . NOME_DA_PASTA_DO_VENV/bin/activate`, para ativar o ambiente virtual;

3) `$ pip install -r requirements.txt`, para instalar pacotes necessários;

4) `$ python manage.py migrate`, para fazer migrações do banco de dados;

5) `$ python manage.py runserver`, para iniciar a aplicação localmente em <http://127.0.0.1:8000/>
