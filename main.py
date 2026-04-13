#!/usr/bin/env python3
"""
To-Do List Application
Консольное приложение для управления списком задач
"""

import sys

from storage import Storage


def print_header():
    """Выводит заголовок приложения"""
    print("\n" + "=" * 50)
    print("         📝  TO-DO LIST MANAGER  📝")
    print("=" * 50)


def print_menu():
    """Выводит главное меню"""
    print("\n📋 МЕНЮ:")
    print("  1. ➕ Добавить задачу")
    print("  2. 📋 Показать все задачи")
    print("  3. ✅ Отметить задачу выполненной")
    print("  4. ✏️  Редактировать задачу")
    print("  5. ❌ Удалить задачу")
    print("  6. 🔍 Фильтровать задачи")
    print("  7. 🗑️  Очистить выполненные задачи")
    print("  8. 💾 Сохранить и выйти")
    print("  9. 🚪 Выйти без сохранения")
    print("-" * 50)


def print_tasks(tasks, show_details=False):
    """Выводит список задач"""
    if not tasks:
        print("  📭 Нет задач")
        return

    for i, task in enumerate(tasks, 1):
        status = "✅" if task.completed else "⭕"
        priority_text = {
            "low": "🟢 Низкий",
            "medium": "🟡 Средний",
            "high": "🔴 Высокий",
        }
        priority_display = priority_text.get(task.priority, "Средний")

        print(f"\n  {i}. {status} #{task.id} - {task.title}")
        print(f"     📊 Приоритет: {priority_display}")

        if show_details and task.description:
            print(f"     📝 Описание: {task.description}")

        if task.completed and task.completed_at:
            from datetime import datetime

            completed_date = datetime.fromisoformat(task.completed_at).strftime(
                "%d.%m.%Y %H:%M"
            )
            print(f"     ✅ Выполнено: {completed_date}")

        from datetime import datetime

        created_date = datetime.fromisoformat(task.created_at).strftime(
            "%d.%m.%Y %H:%M"
        )
        print(f"     📅 Создано: {created_date}")


def add_task_interface(manager):
    """Интерфейс добавления задачи"""
    print("\n✨ ДОБАВЛЕНИЕ НОВОЙ ЗАДАЧИ:")
    title = input("  📌 Название задачи: ").strip()
    if not title:
        print("  ❌ Название не может быть пустым!")
        return

    description = input("  📝 Описание (необязательно): ").strip()

    print("  🎯 Приоритет:")
    print("     1. Низкий")
    print("     2. Средний")
    print("     3. Высокий")
    priority_choice = input("  Выберите (1-3, по умолчанию 2): ").strip()

    priority_map = {"1": "low", "2": "medium", "3": "high"}
    priority = priority_map.get(priority_choice, "medium")

    task = manager.add_task(title, description, priority)
    print(f"  ✅ Задача #{task.id} успешно добавлена!")


def show_all_tasks_interface(manager):
    """Интерфейс показа всех задач"""
    print("\n📋 ВСЕ ЗАДАЧИ:")
    tasks = manager.get_all_tasks()

    if not tasks:
        print("  📭 Список задач пуст")
        return

    # Разделяем на активные и выполненные
    active = [t for t in tasks if not t.completed]
    completed = [t for t in tasks if t.completed]

    if active:
        print("\n  🔥 АКТИВНЫЕ ЗАДАЧИ:")
        print_tasks(active)

    if completed:
        print("\n  ✅ ВЫПОЛНЕННЫЕ ЗАДАЧИ:")
        print_tasks(completed)

    print(
        f"\n  📊 Статистика: Всего: {len(tasks)} | Активных: {len(active)} | Выполнено: {len(completed)}"
    )


def complete_task_interface(manager):
    """Интерфейс отметки задачи выполненной"""
    print("\n✅ ОТМЕТКА ЗАДАЧИ:")
    active_tasks = manager.get_tasks_by_status(completed=False)

    if not active_tasks:
        print("  🎉 Нет активных задач!")
        return

    print("  Активные задачи:")
    for task in active_tasks:
        print(f"    #{task.id} - {task.title}")

    try:
        task_id = int(input("\n  Введите ID задачи для отметки: "))
        if manager.complete_task(task_id):
            print(f"  ✅ Задача #{task_id} отмечена как выполненная!")
        else:
            print(f"  ❌ Задача #{task_id} не найдена или уже выполнена")
    except ValueError:
        print("  ❌ Пожалуйста, введите корректный ID")


def edit_task_interface(manager):
    """Интерфейс редактирования задачи"""
    print("\n✏️ РЕДАКТИРОВАНИЕ ЗАДАЧИ:")
    tasks = manager.get_all_tasks()

    if not tasks:
        print("  📭 Нет задач для редактирования")
        return

    print("  Все задачи:")
    for task in tasks:
        status = "✓" if task.completed else "○"
        print(f"    #{task.id} [{status}] - {task.title}")

    try:
        task_id = int(input("\n  Введите ID задачи для редактирования: "))
        task = manager.get_task(task_id)

        if not task:
            print(f"  ❌ Задача #{task_id} не найдена")
            return

        print(f"\n  Текущее название: {task.title}")
        new_title = input(
            "  Новое название (оставьте пустым для без изменений): "
        ).strip()

        print(f"  Текущее описание: {task.description or '(пусто)'}")
        new_description = input(
            "  Новое описание (оставьте пустым для без изменений): "
        ).strip()

        print(
            "  Текущий приоритет:",
            {"low": "Низкий", "medium": "Средний", "high": "Высокий"}[task.priority],
        )
        print("  Новый приоритет:")
        print("     1. Низкий")
        print("     2. Средний")
        print("     3. Высокий")
        print("     0. Без изменений")
        priority_choice = input("  Выберите (0-3): ").strip()

        priority_map = {"1": "low", "2": "medium", "3": "high", "0": None}
        new_priority = priority_map.get(priority_choice)

        if manager.update_task(
            task_id, new_title or None, new_description or None, new_priority
        ):
            print(f"  ✅ Задача #{task_id} успешно обновлена!")
        else:
            print("  ❌ Ошибка при обновлении задачи")

    except ValueError:
        print("  ❌ Пожалуйста, введите корректный ID")


def delete_task_interface(manager):
    """Интерфейс удаления задачи"""
    print("\n❌ УДАЛЕНИЕ ЗАДАЧИ:")
    tasks = manager.get_all_tasks()

    if not tasks:
        print("  📭 Нет задач для удаления")
        return

    print("  Все задачи:")
    for task in tasks:
        status = "✓" if task.completed else "○"
        print(f"    #{task.id} [{status}] - {task.title}")

    try:
        task_id = int(input("\n  Введите ID задачи для удаления: "))
        confirm = input(
            f"  Вы уверены, что хотите удалить задачу #{task_id}? (y/n): "
        ).lower()

        if confirm == "y":
            if manager.remove_task(task_id):
                print(f"  ✅ Задача #{task_id} удалена!")
            else:
                print(f"  ❌ Задача #{task_id} не найдена")
        else:
            print("  🚫 Удаление отменено")
    except ValueError:
        print("  ❌ Пожалуйста, введите корректный ID")


def filter_tasks_interface(manager):
    """Интерфейс фильтрации задач"""
    print("\n🔍 ФИЛЬТРАЦИЯ ЗАДАЧ:")
    print("  1. Показать только активные")
    print("  2. Показать только выполненные")
    print("  3. По приоритету (низкий)")
    print("  4. По приоритету (средний)")
    print("  5. По приоритету (высокий)")

    choice = input("  Выберите опцию (1-5): ").strip()

    filter_map = {
        "1": ("status", False),
        "2": ("status", True),
        "3": ("priority", "low"),
        "4": ("priority", "medium"),
        "5": ("priority", "high"),
    }

    if choice not in filter_map:
        print("  ❌ Неверный выбор")
        return

    filter_type, value = filter_map[choice]

    if filter_type == "status":
        tasks = manager.get_tasks_by_status(value)
        status_text = "активные" if not value else "выполненные"
        print(f"\n  📋 {status_text.upper()} ЗАДАЧИ:")
    else:
        tasks = manager.get_tasks_by_priority(value)
        priority_text = {"low": "НИЗКИЙ", "medium": "СРЕДНИЙ", "high": "ВЫСОКИЙ"}
        print(f"\n  📋 ЗАДАЧИ С ПРИОРИТЕТОМ {priority_text[value]}:")

    print_tasks(tasks, show_details=True)

    if not tasks:
        print("  📭 Нет задач по указанному фильтру")


def main():
    """Главная функция приложения"""
    storage = Storage()
    manager = storage.load()

    print_header()
    print("💡 Добро пожаловать в менеджер задач!")

    while True:
        print_menu()
        choice = input("\n👉 Ваш выбор: ").strip()

        if choice == "1":
            add_task_interface(manager)
        elif choice == "2":
            show_all_tasks_interface(manager)
        elif choice == "3":
            complete_task_interface(manager)
        elif choice == "4":
            edit_task_interface(manager)
        elif choice == "5":
            delete_task_interface(manager)
        elif choice == "6":
            filter_tasks_interface(manager)
        elif choice == "7":
            count = manager.clear_completed()
            print(f"  🗑️ Удалено {count} выполненных задач")
        elif choice == "8":
            if storage.save(manager):
                print("  💾 Задачи сохранены. До свидания! 👋")
            else:
                print("  ❌ Ошибка при сохранении!")
            break
        elif choice == "9":
            print("  🚪 Выход без сохранения. До свидания! 👋")
            break
        else:
            print("  ❌ Неверный выбор! Пожалуйста, выберите опцию от 1 до 9")

        input("\n📌 Нажмите Enter для продолжения...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана пользователем. До свидания!")
        sys.exit(0)
