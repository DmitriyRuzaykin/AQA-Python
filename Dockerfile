FROM python:3.10-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Переменные окружения
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Рабочая директория
WORKDIR /app

# Копируем проект
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запуск тестов
CMD ["pytest", "--alluredir=allure-results"]