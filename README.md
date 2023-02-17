# Aplicação que receba inputs de 3 rotas em uma página HTML, para um arquivo de audio MP3 via polly, após isso retorne o arquivo de audio para o usuário

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/LogoCompasso-positivo.png/440px-LogoCompasso-positivo.png)](https://compass.uol/pt/home/)

Desenvolver uma plicação em python que obtenha uma página simples HTML responsável por receber os inputs de 3 rotas, capture a frase e converta ela num arquivo de audio via polly, por fim retorne o arquivo.

A apresentação será desenrolada em duas etapas principais, sendo-as:
- Execução (código fonte)
- Deploy. Será apresentado:

### Sumário
- Organização e preparação da aplicação
- Ferramentas
- Comandos

# Organização e preparação da aplicação


Segue a imagem de como ficou a organização dos arquivos.


![estrutura_arquivos_sprint6](https://user-images.githubusercontent.com/119500249/219551929-ee86fe3c-853a-4314-988a-cd4e304dbe4d.png)


## Ferramentas

As principais ferramentas utilizadas no projeto foram:

- [Python](https://www.python.org/) - Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
- [HTML] - O que é HTML e para que serve?
HTML (Linguagem de Marcação de HiperTexto) é o bloco de construção mais básico da web. Define o significado e a estrutura do conteúdo da web. Outras tecnologias além do HTML geralmente são usadas para descrever a aparência/apresentação (CSS) ou a funcionalidade/comportamento (JavaScript) de uma página da web.
- [AWS](https://aws.amazon.com/pt/) - Também conhecido como AWS, é uma plataforma de serviços de computação em nuvem, que formam uma plataforma de computação na nuvem oferecida pela Amazon.com. Os serviços são oferecidos em várias áreas geográficas distribuídas pelo mundo. Dentre teus principais serviços, estão: 1º Computação. 2º Armazenamento. 3º Banco de dados. 4º Redes e entrega de conteúdo. 5º Análises. 6º /Machine learning. 7º Segurança, identidade e conformidade. Dentre muito outros.
- [Serverless](https://aws.amazon.com/pt/serverless/) - As aplicações modernas são desenvolvidas primeiro sem servidor, uma estratégia que prioriza a adoção de serviços sem servidor, para que você possa aumentar a agilidade em toda a pilha de aplicações.


## As rotas

### Rota /v1/tts POST
Esta rota pega o texto de "phrase" e chama a função _getAudioData()_ que por sua vez vai chamar o __client polly__ e criar o áudio com a função 'synthesize_speech', depois adiciona o arquivo no bucket S3 com o tipo mp3. Por fim, retorna um objeto do tipo Data, que contém as informações sobre o áudio (o texto original, o id e a url). De volta ao arquivo v1.py, os dados retornados são usados para dar o retorno em json esperado.


### Rota /v2/tts  POST
Esta rota vai fazer o mesmo que a rota /v1/tts, porém com a adição da inserção dos dados numa tabela do DynamoDB através da função 'putIntoTable()' que recebe um objeto tipo Data.


### Rota /v3/tts  POST
Esta rota diferentemente das demais, vai primeiro consultar o banco de dados e averiguar, através da função 'getFromTable' se já existe algum registro com o mesmo hash, se existir a função retorna um objeto tipo Data, senão retorna None. No caso do retorno ser None, o bloco a ser executado fará basicamente o mesmo que a rota anterior faz.

---
## Autores

* [@Humberto-Sampaio](https://github.com/Humbert010)
* [@Jeef-Moreira](https://github.com/Jeef-Moreira)
* [@Josiana-Silva](https://github.com/JosianaSilva)
* [@Rosemelry-Mendes](https://github.com/Rosemelry)

---
---