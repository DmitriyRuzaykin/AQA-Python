# 🧪 Автотесты для SauceDemo

1. Клонирование репозитория

git clone https://github.com/DmitriyRuzaykin/AQA-Python.git
cd AQA-Python

2. Запуск через Docker
в терминале:
# 2.1. Сборка Docker образа
docker build -t selenium-tests .

в powershell:
# 2.2. Запустите тесты с сохранением отчета
docker run --rm -v "$(pwd)/allure-results:/app/allure-results" selenium-tests

в powershell:
# 2.3. Просмотр отчёта
allure serve allure-results

3. Локальный запуск (Windows)
в терминале:
# 3.1. Установите зависимости
pip install -r requirements.txt

# 3.2 Запустите тесты
pytest

Тест с Allure отчётом
pytest --alluredir=allure-results

# 3.3. Просмотр отчёта
allure serve allure-results