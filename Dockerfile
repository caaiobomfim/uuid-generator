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