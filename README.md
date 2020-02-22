# logist-api
Async application service. App for logist company.

https://sqlalchemy-migrate.readthedocs.io/en/latest/

Create migrate file

> python logist_db/manage.py script "comment"
> python logist_db/manage.py upgrade
> python logist_db/manage.py downgrade 002


1. Фильтр

1. Добавить удаление для всех сущностей

2. Роутинги определить в классы

3. Сделать классы модели для таблиц бд 

5. настроить unit test

6. валидация данных

7. обработка ошибок (выводить соответствующие response code)