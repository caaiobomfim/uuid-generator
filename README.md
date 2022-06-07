# UUID Generator

O projeto consiste num **container docker** que executa uma imagem **python** (gerada a partir de um **Dockerfile**) e através do **flask** exibe uma aplicação web desenvolvida em **html**, **css** e **bootstrap** que mostra um gerador de **UUID online**.

## Iniciar o Git no Repositório

```shell
users@DESKTOP MINGW64 ~/Documents/github-projects/uuid-generator
$ git init
```

## Criação do Dockerfile

Criação do arquivo **Dockerfile** com a intrução para baixar a imagem oficial **httpd** no **Docker Hub** e copia o projeto para o container posteriormente.

```dockerfile
#Iniciar a imagem base
FROM python:3
#Definir o diretório de trabalho
WORKDIR /uuid-generator
#Copiar o conteúdo do projeto para o diretório de trabalho
ADD . /uuid-generator
#Executar as dependências do projeto
RUN pip install -r requirements.txt
#Definir comando de inicializar container
CMD [ "python", "app.py" ]
```

## HTML

Criação do arquivo **index.html**.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UUID Generator</title>
    <link rel="stylesheet" href="../static/css/main.css">
    <link rel="stylesheet" href="../static/css/bootstrap.min.css">
</head>

<body class="bg-uuid-generator">
    <header>
        <div class="container container-uuid-generator">
            <h1 class="display-4 title-uuid-generator">UUID Generator Application</h1>
            <hr class="my-4 hr-uuid-generator">
            <form action="/" method="post">
                <div class="input-group">
                    <select class="custom-select" id="inputGroupSelect" name="select-uuid">
                        <option selected>Selecionar...</option>
                        <option value="uuid1">UUID 1</option>
                        <option value="uuid4">UUID 4</option>
                    </select>
                    <div class="input-group-append">
                        <input class="btn btn-outline-primary" type="submit" value="Generate" id="gen" />
                    </div>
                </div>
            </form>
            {% for message in get_flashed_messages() %}
            <div class="result-uuid-generator">
                <label for="label-result-uuid-generator"> {{message}} </label>
            </div>
            {% endfor %}
        </div>
    </header>
</body>

</html>
```

## CSS

Criação do arquivo **main.css**.

```css
.bg-uuid-generator {
    background-color: #e9ecef;
}

.title-uuid-generator {
    color: black;
    text-align: center;
    padding-bottom: 2rem;
}

.container-uuid-generator {
    padding-top: 7rem;
}

.hr-uuid-generator {
    background-color: #D6D6D6;
}

.result-uuid-generator {
    text-align: center;
    margin-top: 2rem;
    font-weight: 500;
    font-size: 2rem;
    background-color: #59C9A5;
    padding-top: 0.5rem;
    color: azure;
}
```

## Construção da Imagem Docker

Criação da imagem docker a partir do arquivo **Dockerfile**.

```docker
users@DESKTOP MINGW64 ~/Documents/github-projects/uuid-generator
$ docker build -t docker-uuid-generator .
```

## Criação e Execução do Container

Criação e execução do container na porta 5000 a partir da imagem **docker-uuid-generator**.

```docker
users@DESKTOP MINGW64 ~/Documents/github-projects/uuid-generator
$ docker run -d --name docker-python-flask-uuid-generator-webpage -p 5000:5000 docker-uuid-generator
```

## Aplicação em Execução

Acessando a aplicação web em http://localhost/.

![webproject](./webproject/img/project-exec.JPG "webproject")