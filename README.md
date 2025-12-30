# Автотесты для SauceDemo

У вас должны быть установлены: 

Docker Desktop - для запуска через контейнер

Java 8+ - для работы Allure отчётов

Python 3.10+ - для локального запуска

Allure Commandline - для просмотра отчетов

# 1. Подготовка к запуску

1.1. Клонирование репозитория

```git clone https://github.com/DmitriyRuzaykin/AQA-Python.git```

2.2. Переход в директорию проекта

```cd AQA-Python```

# 2. Запуск через Docker

2.1. Сборка Docker образа

в терминале:

```docker build -t selenium-tests .```

2.2. Запустите тесты с сохранением отчета

Для PowerShell (Windows):

```docker run --rm -v "$(pwd)/allure-results:/app/allure-results" selenium-tests```

2.3. Просмотр отчёта

в powershell:

```allure serve allure-results```

# 3. Локальный запуск (Windows)

3.1. Создание виртуального окружения

```python3 -m venv venv```

3.2. Активация виртуального окружения

в терминале:

```venv/Scripts/activate```

3.3. Установка зависимостей 

```pip install -r requirements.txt```

3.4 Запустите тесты

Простой запуск

```pytest```

С Allure отчётом

```pytest --alluredir=allure-results```

3.5. Просмотр отчёта

```allure serve allure-results```