# company-ratings-service
Сервис для сбора отзывов на необходимые организации

## Как запустить локально
1. Из папки integrations делаем запуск контейнера postgres + adminer:
```shell
docker compose up -d
```
2. Добавляем переменные окружения:
```shell
export DATABASE_ENGINE=postgresql
export DATABASE_USER=postgres
export DATABASE_PASSWORD=testpostgres
export DATABASE_HOST=localhost
export DATABASE_PORT=5432
export DATABASE_NAME=db
```
3. Запускаем сервис
