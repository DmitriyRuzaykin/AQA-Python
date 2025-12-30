# Автотесты для SauceDemo

# 1. Подготовка к запуску

1.1. Клонирование репозитория

```git clone https://github.com/DmitriyRuzaykin/AQA-Python.git```

2.2. Переход в директорию AQA-Python

```cd AQA-Python```

# 2. Запуск через Docker

2.1. Сборка Docker образа

в терминале:

```docker build -t selenium-tests .```

2.2. Запустите тесты с сохранением отчета

в powershell:

```docker run --rm -v "$(pwd)/allure-results:/app/allure-results" selenium-tests```

2.3. Просмотр отчёта

в powershell:

```allure serve allure-results```

# 3. Локальный запуск (Windows)

3.1. Создание виртуального окружения

```python3 -m venv venv```

3.2. Активация виртуального окружения

```venv/Scripts/activate```

3.3. Установите зависимости 

```pip install -r requirements.txt```

3.4 Запустите тесты

```pytest```

Либо тест с Allure отчётом

```pytest --alluredir=allure-results```

3.5. Просмотр отчёта

```allure serve allure-results```