#docker build . -t posting_vk
FROM python:alpine
 #создаем директорию
WORKDIR /app
 #копируем все в директорию
COPY . /app
#устанавливаем зависимости
RUN pip install -r requirements.txt


CMD [ "python3", "main.py" ]
