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
export AUTH_SECRET=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
export AUTH_ALGORITHM=HS256
export AUTH_RESET_SECRET=testtest
export AUTH_VERIFICATION_SECRET=testtest
```
3. Запускаем сервис
