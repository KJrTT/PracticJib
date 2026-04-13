# To-Do List Manager

Консольное приложение для управления списком задач с поддержкой Docker.

## Возможности

- Добавление задач с названием, описанием и приоритетом
- Просмотр всех задач (активные/выполненные)
- Отметка задач как выполненных
- Редактирование задач
- Удаление задач
- Фильтрация по статусу и приоритету
- Автосохранение в JSON файл
- Полная поддержка Docker и Docker Compose

## Запуск через Docker

### Предварительные требования

- Docker (>= 20.10)
- Docker Compose (>= 2.0) - опционально

### Способ : Docker

```bash
  docker-compose run --rm todo-app
```
## Инструменты качества кода

В проекте настроены автоматические проверки кода для поддержания единого стиля и выявления потенциальных проблем.

### Используемые инструменты

| Инструмент | Назначение |
|------------|------------|
| Black | Автоматическое форматирование кода |
| Ruff | Линтер для проверки качества кода |
| Pre-commit | Запуск проверок перед каждым коммитом |

### Установка

```bash
pip install black ruff pre-commit
```
### Форматирование кода (Black)

```bash
# Отформатировать все файлы
black *.py

# Проверить форматирование без изменений
black --check *.py

# Показать
black --diff *.py
```

### Линтер (Ruff)

```bash
# Проверить код
ruff check *.py

# Автоматически исправить ошибки
ruff check --fix *.py

# Показать информацию об ошибках
ruff check --verbose *.py
```

### Pre-commit хуки

```bash
# Установить хуки в репозиторий
pre-commit install

# Запустить проверки на всех файлах вручную
pre-commit run --all-files

# Запустить проверки на конкретных файлах
pre-commit run --files main.py storage.py
```


<img width="678" height="167" alt="image" src="https://github.com/user-attachments/assets/c8e65ea6-234f-4456-aeb4-6bff73607518" />
<img width="972" height="159" alt="image" src="https://github.com/user-attachments/assets/5858bd0f-0c76-4aa1-a579-8da9bab429a1" />
<img width="1902" height="363" alt="image" src="https://github.com/user-attachments/assets/510a0793-4c18-4dc9-a76d-2687dacd62c7" />
<img width="1849" height="383" alt="image" src="https://github.com/user-attachments/assets/074f1141-5d9d-49aa-b40a-ca25decd9aed" />
<img width="610" height="227" alt="image" src="https://github.com/user-attachments/assets/a0997ae6-d0f6-4760-b23f-ba969c4c3c52" />
<img width="867" height="672" alt="image" src="https://github.com/user-attachments/assets/38b4ac6a-a942-4aaa-9485-90d908c3a50e" />






