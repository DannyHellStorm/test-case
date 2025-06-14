# 📡 API Testing: Dating App Challenge

Этот проект содержит автоматические тесты для проверки API приложения знакомств (https://hr-challenge.dev.tapyou.com).

## 🧪 Что тестируется

- Получение списка пользователей по полу (`/users?gender=male|female|any`)
- Получение информации о пользователе по ID (`/user/{id}`)
- Пограничные случаи, ошибки и нестандартные ситуации
- Формат даты регистрации
- Задержки при получении пользователей с чётным ID

## 📁 Структура проекта

tests/
├── test_users_api.py # Основные API тесты
requirements.txt # Зависимости проекта
allure-results/ # Результаты тестов (в .gitignore)

## 🚀 Как запустить

1. ✅ Установите зависимости:

```bash
pip install -r requirements.txt

2. ✅ Запустите тесты:

```bash
pytest tests/ --alluredir=allure-results

3. ✅ (по желанию) Сгенерируйте Allure-отчёт:

```bash
allure serve allure-results

## ✅ Используемые технологии:
pytest — фреймворк для запуска тестов
requests — HTTP-клиент для работы с API
allure — генерация отчётов
re — проверка формата даты (регулярные выражения)