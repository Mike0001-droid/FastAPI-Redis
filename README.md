# FastAPI-Redis
FastAPI приложение для демонстрации работы с NoSQL Redis
![GitHub top language](https://img.shields.io/github/languages/top/Mike0001-droid/FastAPI-Redis)
## Цель задания 
# Разработать микросервис для хранения и управления связками "телефон-адрес"
Такой сервис может использоваться для кеширования часто запрашиваемой информации
Задача позволяет оценить понимание REST API, работу с Redis как быстрым хранилищем данных, 
и умение проектировать простые, но правильные решения.
<!--Установка-->
## Установка 

1. Клонирование репозитория 

```git clone https://github.com/Mike0001-droid/FastAPI-Redis```

2. Создайте файл .env, шаблон указан в корне проекта

```REDIS_HOST="localhost"```
```REDIS_PORT=6379```
```REDIS_PASSWORD="password"```
```APPLICATION_TITLE="FastAPI Project"```
```APPLICATION_DEBUG=False```

3. Далее запустите docker-compose

```docker-compose up```

4. Перейдите по адресу 
```http://127.0.0.1:8000/docs```

## Стек
1. Fastapi
2. Pydantic
3. Phonenumbers
4. Gunicorn
5. Uvicorn
6. Pydantic-settings
7. Pydantic-extra-types
8. Redis
