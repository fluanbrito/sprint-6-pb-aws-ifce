<!--
title: 'AWS Simple HTTP Endpoint example in Python'
description: 'This template demonstrates how to make a simple HTTP API with Python running on AWS Lambda and API Gateway using the Serverless Framework.'
layout: Doc
framework: v3
platform: AWS
language: python
authorLink: 'https://github.com/serverless'
authorName: 'Serverless, inc.'
authorAvatar: 'https://avatars1.githubusercontent.com/u/13742415?s=200&v=4'
-->
![Logo_CompassoUOL_Positivo](https://user-images.githubusercontent.com/94761781/212589731-3d9e9380-e9ea-4ea2-9f52-fc6595f8d3f0.png)
# 📑 Avaliação Sprint 4 - Programa de Bolsas Compass UOL / AWS e IFCE

<hr>
<p align="center">
  
<img src="https://img.shields.io/static/v1?label=STATUS&message=FINALIZADO&color=RED&style=for-the-badge" />
</p>

<br>

## 📌 Tópicos 

- [📝 Descrição do projeto](#-descrição-do-projeto)

- [🧑‍💻👩‍💻 Ferramentas e Tecnologias](#-ferramentas-e-tecnologias)

- [🖥️ Código](#%EF%B8%8F-código)

- [📤 Deploy - serviço Elastic Beanstalck](#-deploy---serviço-elastic-beanstalck)

- [♾️ Equipe](#%EF%B8%8F-equipe)

- [📌 Considerações finais](#-considerações-finais)

<br>

## 📝 Descrição do projeto 

<p align="justify">
 Projeto em desenvolvimento se refere à 
avaliação da quarta sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

Trata-se do consumo de do processo criativo de uma aplicação nodeJs (express) que irá consumir duas APIs distintas e efetue o deploy na AWS Elastic Beanstalk.

**Especificações:**
- A aplicação terá basicamente duas rotas que irão retornar informações vindas de APIs externas formatadas de acordo com a especifícação a seguir.

<br>
<hr>

## 🧑‍💻👩‍💻 Ferramentas e Tecnologias 

<br>
<a href="https://nodejs.org/en/" target="_blank"> 
<img src="https://cdn.iconscout.com/icon/free/png-256/node-js-1174925.png" alt="androidStudio" width="40" title="Nodejs" height="40"/> </a> <a href="https://aws.amazon.com/pt/" target="_blank"> <img src="https://static-00.iconduck.com/assets.00/aws-icon-512x512-hniukvcn.png" title="AWS" alt="java" width="40" height="40"/> </a> 
<a href="https://aws.amazon.com/pt/elasticbeanstalk/" target="_blank"> <img src="https://pragmaticintegrator.files.wordpress.com/2016/08/aws_simple_icons_networking_amazonroute53-svg.png" alt="firebase" width="40" height="40" title="AWS Elastic Beanstalk"/> </a>

<br>

🚩[API Piadas](https://api.chucknorris.io/jokes/random)
🚩[API Atividades]( https://www.boredapi.com/api/activity)

<hr>
<br>

## 🖥️ Código

 1- comandos no terminal para instalação e dependências

O seguinte comando cria um pacote, em que os arquivos do projeto serão armazenados

  ```npm init -y```

2- Para instalar as dependências do seu projeto, vamos começar com o Express, que é um framework para Node.js que fornece recursos mínimos para construção de servidores web: Instale o Express:

```npm install --save express```


Para praticidade nos teste instale ainda o Nodemon que vai reiniciar automaticamente o aplicativo do Node 
sempre que detectar qualquer alteração.
```npm install --save nodemon```

3- acompanhe como deverá ficar após a criação dos arquivos subsequentes a imagem

```estrutura **src**```
![01](https://user-images.githubusercontent.com/94761781/212593640-7523887b-88f2-42bf-a107-84e72a8178fd.png)


Arquivo app.js
```
const express = require("express");
const app = express();
//const path = require("path");
const PORT = "8080";

app.use(express.static(__dirname + "/src"));

// rota principal
app.get("/", function (req, res) {
  res.status(200).send("<h1>Este é o app do Grupo 4 🐊</h1>");
});

app.use("/api", require("./apis/atividades_api")); // rota: get /api/atividades

app.use("/api", require("./apis/chucknorris_api")); // rota: get /api/piadas

app.listen(PORT, function () {
  console.log(`Ouvindo a porta ${PORT}`);
});

```

dentro de "apis" criamos o arquivo atividades_api.js
```
const express = require("express");
const router  = express.Router();
const request = require("request");
const activity = require("../format/atividades.js")

router.get("/atividades", (req, res) => {
  request("https://www.boredapi.com/api/activity", (error, response, body) => {
    if(error) {
      console.log(error);
    } else {
      // converte o retorno da API para JSON
      const data = JSON.parse(body);
      // exibe na tela o JSON formatado
      res.status(200).send(activity.returnActivity(data.activity, data.type, data.participants, data.accessibility));
    }
  });
});

module.exports = router;
```


Também dentro de "apis" é criado o arquivo chucknorris_api.js
```
const express = require("express");
const router = express.Router();
const request = require("request");
const format = require("../format/chucknorris.js")
const guid = require("../format/atividades.js")

router.get("/piadas", (req, res) => {
  // função que consome a API
  request(
    "https://api.chucknorris.io/jokes/random",
    (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        // converte o retorno da API para JSON
        data = JSON.parse(body)
        // exibe o JSON formatado na tela
        res.status(200).send(format.contentFormat(format.dataFormat(data.updated_at), format.dataFormat(data.created_at), data.icon_url, guid.createGUID(), format.chuckUpper(data.value), data.url));
      }
    }
  );
})
module.exports = router;

```

Agora em uma outra pasta dentro de src, criamos a pasta "format" criamos o arquivo atividades.js:
```
function createGUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
    });
}

function returnActivity(activity, type, participants, acessibility){
    const act = `{
    "id": "${createGUID()}",
    "atividade": "${activity}",
    "tipo": "${type}",
    "participantes": "${participants}",
    "acessibilidade": "${acessibility * 100}%"
    }`
    return JSON.parse(act);
};

//console.log(returnActivity("a", "esc", 2, 0.2))
module.exports = {returnActivity, createGUID}
```

format/chucknorris.js
```

// formatar a data no formado DD/MM/YYYY
function dataFormat(date){
    newdate = date.slice(0,10).split('-')
    return `${newdate[2]}-${newdate[1]}-${newdate[0]}`
}

// formatação da api no formato solicitado para exibição na tela.
function contentFormat(updated_at, created_at, icon_url, id, joke, reference){
    const template = `{
    "data_atualizacao": "${updated_at}",
    "data_criacao": "${created_at}",
    "icone": "${icon_url}",
    "id": "${id}",
    "piada": "${joke}",
    "referencia": "${reference}"
    }`
    return JSON.parse(template)
}

// função para deixar a palavra "Chuck Norris" em caixa alta.
function chuckUpper(string){
    string_upper = string.replace('Chuck Norris', 'CHUCK NORRIS')
    return string_upper
}

// exportação para uso em outro script
module.exports = {dataFormat, contentFormat, chuckUpper}
```

No terminal da pasta que está o app.js, execute

```
node app.js
```

Abra o navegador e verifique o projeto rodando localmente na porta 8080 temos o resultado:
![000](https://user-images.githubusercontent.com/94761781/212600262-a6b4fb78-5843-4174-81a5-35baf391c840.png)

De forma similar na rota de atividades temos a saída formatada
![00000](https://user-images.githubusercontent.com/94761781/212601459-86c11a79-2352-4e7a-8bb2-585238619398.png)

E, ainda, na rota de piadas:

![00000](https://user-images.githubusercontent.com/94761781/212602195-d4da37f2-2706-44f7-a33c-3ebd6df054d5.png)




## 📤 Deploy - serviço Elastic Beanstalck

Para essa realização foi utilizada a região → `us-east-1` (confira na console se está na região correta antes de proseguir os próximos passos)
- vai está no canto superior direto no seu console:

![deploy-00](https://user-images.githubusercontent.com/94761781/212701374-b5abb41b-77ee-4d60-b4cc-5264f50ce367.png)



1. [Acesse o serviço Elastic Beanstalk no console da AWS.](https://us-east-1.console.aws.amazon.com/elasticbeanstalk/home?region=us-east-1#/welcome)

2. Clique em Create Application

![Step 2 screenshot](https://images.tango.us/workflows/6d444cf6-7a3c-4959-b26c-55383834d79f/steps/05b6785f-52dd-4f8d-8f97-b3cb759de880/169788ea-7c8f-43ff-ad6b-e167074ca7cf.png?crop=focalpoint&fit=crop&fp-x=0.6992&fp-y=0.2949&fp-z=2.9003&w=1200&mark-w=0.2&mark-pad=0&mark64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n&ar=1920%3A902)

3. Na página de criação em "Application Information" digite o nome da aplicação. E para essa aplicação desconsidere o box de ```Aplication tags```

![deploy-01](https://user-images.githubusercontent.com/94761781/212696753-9097dbc2-36f5-455c-8953-59725daa9ef9.png)

4. Em ```Platform```,  selecione NodeJS. Será configurada por padrão em termos de versões o que for necessário. Então basta selecionar Node.js e proceder.

![deploy-02](https://user-images.githubusercontent.com/94761781/212696756-8150c6fe-4d22-432d-bfe1-3b97d4bd6430.png)


5. Selecione na sequência a opção "Upload your code" no box de ```Aplication code```

6. Em ```Source code origin``` defina a origem do código e atribuimos um nome para versão de sua aplicação. E, por conseguinte, selecione o **arquivo .zip** com o projeto Node e clique em "Create application"


![deploy-03](https://user-images.githubusercontent.com/94761781/212696758-4bc58789-24f5-449c-9a6b-84ed8158de90.png)


8. Na sequência, serão exibidos os logs da criação do ambiente.
Observe que vários serviços AWS serão criados (S3, EC2, Security Groups, etc). Pode levar alguns minutos até chegar a finalização.

![deploy-04](https://user-images.githubusercontent.com/94761781/212698335-b0ed1bf1-058d-453f-9afd-05b21b8f79fd.png)


9. Pronto,  na sequência teremos a url exposta para acessar sua aplicação.

No card ```Health``` é possível observar o status da aplicação, se algo estiver incorreto você pode clicar em "Causes" para entender o que causou o erro.

10. Caso seja preciso subir uma atualização do projeto 

Basta clicar em **Upload and deploy** e selecionar o arquivo .zip com o projeto atualizado.

- Vale ressalta a importância de manter uma coêrencia nas versões por exemplo: projeto-node-v1, projeto-node-v2, etc.

![sprint-4](https://user-images.githubusercontent.com/94761781/212698955-2f29b28b-49b8-47f6-a707-c2042362c70a.jpeg)


Mais informações sobre o Elastic Beanstalk podem ser encontradas na [documentação da AWS](https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/Welcome.html)

<br>

## 🚩Acesso ao projeto

Pela URL, acesse: [http://avaliacaosprint4grupo4-env.eba-3cpfyu4p.us-east-1.elasticbeanstalk.com/](http://avaliacaosprint4grupo4-env.eba-3cpfyu4p.us-east-1.elasticbeanstalk.com/)
⚠️link do projeto WEB ficará fora do ar até o dia da avaliação da Sprint para economia de recursos.

<br>
<hr>

## ♾️ Equipe
<br>

- Nicolas Ferreira
- Josiana Silva
- Samara Oliveira
- Jhonatan Gonçalves

<br>
<hr>

## 📌 Considerações finais
<br>
Em resumo, ...




# Serverless Framework Python HTTP API on AWS

This template demonstrates how to make a simple HTTP API with Python running on AWS Lambda and API Gateway using the Serverless Framework.

This template does not include any kind of persistence (database). For more advanced examples, check out the [serverless/examples repository](https://github.com/serverless/examples/)  which includes DynamoDB, Mongo, Fauna and other examples.

## Usage

### Deployment

```
$ serverless deploy
```

After deploying, you should see output similar to:

```bash
Deploying aws-python-http-api-project to stage dev (us-east-1)

✔ Service deployed to stack aws-python-http-api-project-dev (140s)

endpoint: GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/
functions:
  hello: aws-python-http-api-project-dev-hello (2.3 kB)
```

_Note_: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [http event docs](https://www.serverless.com/framework/docs/providers/aws/events/apigateway/).

### Invocation

After successful deployment, you can call the created application via HTTP:

```bash
curl https://xxxxxxx.execute-api.us-east-1.amazonaws.com/
```

Which should result in response similar to the following (removed `input` content for brevity):

```json
{
  "message": "Go Serverless v3.0! Your function executed successfully!",
  "input": {
    ...
  }
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function hello
```

Which should result in response similar to the following:

```
{
  "statusCode": 200,
  "body": "{\n  \"message\": \"Go Serverless v3.0! Your function executed successfully!\",\n  \"input\": \"\"\n}"
}
```

Alternatively, it is also possible to emulate API Gateway and Lambda locally by using `serverless-offline` plugin. In order to do that, execute the following command:

```bash
serverless plugin install -n serverless-offline
```

It will add the `serverless-offline` plugin to `devDependencies` in `package.json` file as well as will add it to `plugins` in `serverless.yml`.

After installation, you can start local emulation with:

```
serverless offline
```

To learn more about the capabilities of `serverless-offline`, please refer to its [GitHub repository](https://github.com/dherault/serverless-offline).

### Bundling dependencies

In case you would like to include 3rd party dependencies, you will need to use a plugin called `serverless-python-requirements`. You can set it up by running the following command:

```bash
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to `plugins` section in your `serverless.yml` file and add it as a `devDependency` to `package.json` file. The `package.json` file will be automatically created if it doesn't exist beforehand. Now you will be able to add your dependencies to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but requires additional configuration) and they will be automatically injected to Lambda package during build process. For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).
