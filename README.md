Система авторизации на Django REST Framework (JWT)

Тестовое задание на позицию Junior Python Developer.

Реализованный функционал:

- JWT-авторизация: Использование access и refresh токенов.
- Custom User Model: Расширенная модель пользователя (email вместо username, дополнительные поля).
- Система ролей (RBAC): Кастомная реализация прав доступа через таблицу Roles (Admin, Client и т.д.).
- Мягкое удаление: При удалении профиля аккаунт деактивируется (`is_active=False`), данные сохраняются.
- Logout: Реализован через механизм `blacklist` для JWT токенов.
- Админ-панель: Удобное управление пользователями и их ролями.

Как запустить проект:

1. Создать виртуальное окружение и активировать его.
2. Установить зависимости: `pip install -r requirements.txt`.
3. Применить миграции: `python manage.py migrate`.
4. Создать суперпользователя: `python manage.py createsuperuser`.
5. Запустить сервер: `python manage.py runserver`.

Технологии:

- Python 3.x
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt

Данные для теста (Admin):

Login: admin@mail.ru
Password: xyu12345
Role: admin (уже назначена в БД)