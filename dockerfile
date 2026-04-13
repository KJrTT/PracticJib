FROM python:3.11-slim

WORKDIR /app

# Копируем все файлы
COPY *.py ./

# Создаём директорию для данных с правильными правами
RUN mkdir -p /app/data && \
    chmod 777 /app/data

# Запускаем от root (для простоты)
CMD ["python", "/app/main.py"]