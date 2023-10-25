## Generic single-database configuration.

Использование миграций:
- Для генерации новой миграции:
```shell
alembic revision --autogenerate -m "Название миграции"
```
- Для апгрейда до последней миграции:
```shell
alembic upgrade head
```

