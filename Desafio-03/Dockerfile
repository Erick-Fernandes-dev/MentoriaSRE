# Usa uma imagem oficial e leve do python
FROM python:3.11-slim

# Define o diretório de trabalho DENTRO do container
WORKDIR /code

# Copia apenas o arquivo de requisitos primeiro (aproveita o cache do docker)
COPY requirements.txt .

# Instala as dependências de sua API
RUN pip install --no-cache-dir -r requirements.txt

# Agora, copia a sua pasta 'app' local para dentro de uma 'app' no container
COPY ./app ./app

# Expõe a porta que a API vai rodar
EXPOSE 8008

# Inicia o Uvicorn, apontando para o arquivo main.py dentro da pasta do projeto
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8008"]