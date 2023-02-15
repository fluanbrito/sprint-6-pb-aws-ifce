![Logo_CompassoUOL_Positivo](https://user-images.githubusercontent.com/94761781/212589731-3d9e9380-e9ea-4ea2-9f52-fc6595f8d3f0.png)
# 📑 Avaliação Sprint 6 - Programa de Bolsas Compass.uol / AWS e IFCE

<hr>
<p align="center">
  
<img src="https://img.shields.io/static/v1?label=STATUS&message=construindo&color=RED&style=for-the-badge" />
</p>


## 📌 Tópicos 

- [📝 Descrição do projeto](#-descrição-do-projeto)

- [🧑‍💻👩‍💻 Ferramentas e Tecnologias](#-ferramentas-e-tecnologias)

- [🖥️ Código](#%EF%B8%8F-código)

- [📤 Deploy - serviço Elastic Beanstalck](#-deploy)

- [♾️ Equipe](#%EF%B8%8F-equipe)

- [📌 Considerações finais e dificuldades](#-considerações-finais-e-dificuldades)

<br>

## 📝 Descrição do projeto 
Criação de uma página html que captura uma frase qualquer inserida pelo usuário e transformará essa frase em um audio em mp3 via polly.

<p align="justify">
<hr>

## 🧑‍💻👩‍💻 Ferramentas e Tecnologias 

<br>
<a href="https://aws.amazon.com/pt/polly/" target="_blank"> 
<img src="https://imgs.search.brave.com/Q8TsMuqn0Ggx-ePHHX5cbZ6wcQkAb6tpaR6EZoOMe8o/rs:fit:200:200:1/g:ce/aHR0cHM6Ly9rYWxs/aW9wZS1wcm9qZWN0/LmdpdGh1Yi5pby9p/bWFnZXMvcG9sbHlf/dHRzLnBuZw" alt="androidStudio" width="40" title="Polly" height="40"/> </a> <a href="https://aws.amazon.com/pt/api-gateway/ target="_blank"> <img src="https://imgs.search.brave.com/-mAOrY3RTIz9jBKsHpv8wvpy2cOF7CV6YtfUxnUN9Bo/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9jZG4u/ZnJlZWJpZXN1cHBs/eS5jb20vbG9nb3Mv/bGFyZ2UvMngvYXdz/LWFwaS1nYXRld2F5/LWxvZ28tcG5nLXRy/YW5zcGFyZW50LnBu/Zw" title="API GATEWAY" alt="java" width="40" height="40"/> </a> 
<a href="https://aws.amazon.com/pt/lambda/" target="_blank"> <img src="https://imgs.search.brave.com/u5UqI1qsoHqoY1QGcfWS7WU9jmaGEgxhwqlYZbJ9Eoo/rs:fit:725:750:1/g:ce/aHR0cHM6Ly9pMS53/cC5jb20vYmxvZy5j/b250YWN0c3Vubnku/Y29tL3dwLWNvbnRl/bnQvdXBsb2Fkcy8y/MDE5LzExL2F3c19s/YW1iZGFfbG9nby5w/bmc_c3NsPTE" alt="firebase" width="40" height="40" title="AWS Lambda"/> </a><a href="https://aws.amazon.com/pt/dynamodb/" target="_blank"> <img src="https://imgs.search.brave.com/84pQUKFRPnJD0Fcoc-rwRZMAGrjIWdFHC9C1lX02LFc/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9jZG4u/ZnJlZWJpZXN1cHBs/eS5jb20vbG9nb3Mv/bGFyZ2UvMngvYXdz/LWR5bmFtb2RiLWxv/Z28tcG5nLXRyYW5z/cGFyZW50LnBuZw" alt="firebase" width="40" height="40" title="AWS DYnanmo DB"/> </a> <a href="https://aws.amazon.com/pt/s3/" target="_blank"> <img src="https://imgs.search.brave.com/uKMT5jd0yYlnw-jAFoeBgq4XT-Shdlgto1NoX2NHSUs/rs:fit:1057:1200:1/g:ce/aHR0cHM6Ly9icmFu/ZHNsb2dvcy5jb20v/d3AtY29udGVudC91/cGxvYWRzL2ltYWdl/cy9sYXJnZS9hd3Mt/czMtbG9nby5wbmc" alt="firebase" width="40" height="40" title="AWS S3"/> </a><a href="https://www.serverless.com/" target="_blank"> <img src="https://imgs.search.brave.com/D8PnoWnRnNIFBk7YnDttFF4TrmsEhr3LWU-ernO7WUU/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9zMy11/cy13ZXN0LTIuYW1h/em9uYXdzLmNvbS9h/c3NldHMuc2l0ZS5z/ZXJ2ZXJsZXNzLmNv/bS9sb2dvcy9zZXJ2/ZXJsZXNzLXNxdWFy/ZS1pY29uLXRleHQu/cG5n" alt="firebase" width="40" height="40" title="Serveless"/> </a>

<br>

<hr>

## 🖥️ Código - Execução (Código Fonte)

**Configurações Iniciais**:

Passo a passo para iniciar o projeto:

1. Instale o framework serverless em seu computador. Mais informações [aqui](https://www.serverless.com/framework/docs/getting-started)
```json
npm install -g serverless
```

2. Gere suas credenciais (AWS Acess Key e AWS Secret) na console AWS pelo IAM. Mais informações [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

3. Em seguida insira as credenciais e execute o comando conforme exemplo:

```json
serverless config credentials --provider aws --key XXXXXXX --secret XXXXXXX
  ```

Também é possivel configurar via [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) executando o comando:

```json
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: ENTER
  ```

4. Efetuar o deploy da solução na sua conta aws execute (acesse a pasta `api-tts`):
```
$ serverless deploy
```
Um retorno parecido com isTo:

```bash
Deploying api-tts to stage dev (us-east-1)

Service deployed to stack api-tts-dev (85s)

endpoints:
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v1
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v2
functions:
  health: api-tts-dev-health (2.1 kB)
  v1Description: api-tts-dev-v1Description (2.1 kB)
  v2Description: api-tts-dev-v2Description (2.1 kB)
```


## Atividade -> Parte 1 

### Página HTML

Conforme especificações da avaliação, foi criada uma página HTML para o usuário fornecesse uma frase qualquer e a mesma passasse pelo processo das rotas da API de foma a ser convertida em audio mp3 utilizando o serviço Amazon Polly e o resultado fosse retornado ao usuário. 

```







### Rota V1 -> Post /v1/tts

Para o desenvolvimento da primeira parte do projeto 

Deverá ser criada a rota `/v1/tts` que receberá um post no formato abaixo:

```json
  {
    "phrase": "converta esse texto para áudio"
  }
```
- Essa frase recebida deverá ser transformada em áudio via AWS Polly
- Deverá ser armazenada em um S3 (Que deverá ser público, apenas para a nossa avaliação)
- A resposta da chamada da API deverá constar o endereço do audio gerado no S3

Resposta a ser entregue:

```json
  {
    "received_phrase": "converta esse texto para áudio",
    "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
    "created_audio": "02-02-2023 17:00:00"
  }
```

Dessa maneira essa será a arquitetura a ser impantada:

![post-v1-tts](./assets/post-v1-tts.png)


Exemplos de referência:
  - https://github.com/SC5/serverless-blog-to-podcast (JS) 
  - https://github.com/hussainanjar/polly-lambda (Python)

## Atividade -> Parte 2 
### Rota V2 -> Post /v2/tts

Deverá ser criada a rota `/v2/tts` que receberá um post no formato abaixo:

```json
  {
    "phrase": "converta esse texto para áudio e salve uma referencia no dynamoDB"
  }
```
- Deverá ser criada uma lógica para que essa frase recebida seja um id unico (um hash).
- Esse hash será o principal atributo em nosso dynamo db
Exemplo: "Teste 123" será sempre o id "123456"
- Com essa frase recebida deverá ser transformada em áudio via AWS Polly
- Deverá ser armazenada em um S3 (Que deverá ser público, apenas para a nossa avaliação)
- Deverá ser salva uma referencia no dynamoBD com as seguintes informações: id, frase e url do s3
- A resposta da chamada da API deverá constar o endereço do audio gerado no S3

Resposta a ser entregue:

```json
  {
    "received_phrase": "converta esse texto para áudio",
    "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
    "created_audio": "02-02-2023 17:00:00",
    "unique_id": "123456"
    
  }
```

Dessa maneira essa será a arquitetura a ser impantada:

![post-v2-tts](./assets/post-v2-tts.png)


Exemplos de referência com inserção no dynamoDb:
  -  https://github.com/serverless/examples/tree/v3/aws-python-http-api-with-dynamodb (Python)


## Atividade -> Parte 3 
### Rota V3 -> Post /v3/tts

Deverá ser criada a rota `/v3/tts` que receberá um post no formato abaixo:

```json
  {
    "phrase": "converta esse texto para áudio e salve uma referencia no dynamoDB. Caso a referencia já exista me devolva a URL com audio já gerado"
  }
```
- Deverá utilizar a lógica do hash para verificar se a frase já foi gerada anteriormente.
- Caso o hash já exista no dynamo entregue o retorno conforme abaixo.
- Caso não exista faça a geração do audio, grave no s3 e grave as referencias no dynamo conforme Parte 2


Resposta a ser entregue:

```json
  {
    "received_phrase": "converta esse texto para áudio",
    "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
    "created_audio": "02-02-2023 17:00:00",
    "unique_id": "123456"
  }
```

Dessa maneira essa será a arquitetura a ser impantada:

![post-v3-tts](./assets/post-v3-tts.png)

***

## Observações retorno esperado

- os campos de entrada e saida deverão estar nos formatos e com os nomes apresentados.
- status code para sucesso da requisição será `200`
- status code para erros deverá ser `500`




## 📤 Deploy

<br>

## 🚩Acesso ao projeto

<hr>

## ♾️ Equipe
<br>

- [Mylena Soares](https://github.com/mylensoares)
- [Samara Alcantara](https://github.com/SamaraAlcantara)
- [Julio Cesar](https://github.com/JC-Rodrigues)
- [Jhonatan Gonçalves](https://github.com/jhonatangoncalvespereira)

<br>
<hr>

## 📌 Considerações finais e dificuldades
<br>
No desenvolvimento do projeto uma dos principais impedimentos encontrados estavam nas permissões nas funções da AWS, particurlarmente no serviço Polly.






Avaliação da sexta sprint do programa de bolsas Compass.uol para formação em machine learning para AWS.

