# Мой блог на Django

Простой блог с возможностью создания статей.

**1. Клонировать репозиторий:**
```bash
https://github.com/myclim/my_django_project.git
```

**2. Создать виртуальное окружение (рекомендуется):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

**3. Установить зависимости:**
```bash
pip install -r requirements.txt
```

**4. Применить миграции:**
```bash
python manage.py migrate
```

**5. Создать суперпользователя (чтобы зайти в админку):**
```bash
python manage.py createsuperuser
```

**6. Запустить сервер:**
```bash
python manage.py runserver
```

**7. Открыть в браузере:**
- Блог: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/ (логин/пароль от суперпользователя)

---

## ⚙️ Основные функции

- 📝 Создание/редактирование статей
- 🔐 Регистрация и авторизация (если есть)

---

> 🌟 Это мой первый проект на Django. Буду рад обратной связи!
