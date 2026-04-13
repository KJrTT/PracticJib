import json
import os

from task_manager import TaskManager


class Storage:
    """Класс для сохранения и загрузки задач"""

    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename

    def save(self, manager: TaskManager) -> bool:
        """Сохраняет задачи в файл"""
        try:
            data = manager.to_dict()
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            return False

    def load(self) -> TaskManager | None:
        """Загружает задачи из файла"""
        if not os.path.exists(self.filename):
            return TaskManager()

        try:
            with open(self.filename, encoding="utf-8") as f:
                data = json.load(f)
            return TaskManager.from_dict(data)
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")
            return TaskManager()

    def backup(self) -> bool:
        """Создает резервную копию файла задач"""
        if not os.path.exists(self.filename):
            return False

        backup_filename = f"{self.filename}.backup"
        try:
            with open(self.filename, encoding="utf-8") as source:
                with open(backup_filename, "w", encoding="utf-8") as target:
                    target.write(source.read())
            return True
        except Exception as e:
            print(f"Ошибка при создании резервной копии: {e}")
            return False
