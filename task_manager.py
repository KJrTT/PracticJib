import json
from datetime import datetime
from typing import List, Dict, Optional

class Task:
    """Класс, представляющий задачу"""
    
    def __init__(self, title: str, description: str = "", priority: str = "medium"):
        self.id = None
        self.title = title
        self.description = description
        self.priority = priority  # low, medium, high
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.completed_at = None
    
    def to_dict(self) -> Dict:
        """Преобразует задачу в словарь для сохранения"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at,
            'completed_at': self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Создает задачу из словаря"""
        task = cls(data['title'], data.get('description', ''), data.get('priority', 'medium'))
        task.id = data['id']
        task.completed = data['completed']
        task.created_at = data['created_at']
        task.completed_at = data.get('completed_at')
        return task
    
    def complete(self):
        """Отмечает задачу как выполненную"""
        self.completed = True
        self.completed_at = datetime.now().isoformat()
    
    def __str__(self) -> str:
        status = "✓" if self.completed else "○"
        priority_symbols = {"low": "↓", "medium": "→", "high": "↑"}
        priority_symbol = priority_symbols.get(self.priority, "→")
        return f"[{status}] [{priority_symbol}] {self.title}"


class TaskManager:
    """Менеджер для управления списком задач"""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "", priority: str = "medium") -> Task:
        """Добавляет новую задачу"""
        task = Task(title, description, priority)
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def remove_task(self, task_id: int) -> bool:
        """Удаляет задачу по ID"""
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False
    
    def complete_task(self, task_id: int) -> bool:
        """Отмечает задачу как выполненную"""
        for task in self.tasks:
            if task.id == task_id and not task.completed:
                task.complete()
                return True
        return False
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Возвращает задачу по ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def get_all_tasks(self) -> List[Task]:
        """Возвращает все задачи"""
        return self.tasks.copy()
    
    def get_tasks_by_status(self, completed: bool = False) -> List[Task]:
        """Возвращает задачи по статусу выполнения"""
        return [task for task in self.tasks if task.completed == completed]
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        """Возвращает задачи по приоритету"""
        return [task for task in self.tasks if task.priority == priority]
    
    def update_task(self, task_id: int, title: str = None, 
                   description: str = None, priority: str = None) -> bool:
        """Обновляет информацию о задаче"""
        task = self.get_task(task_id)
        if not task:
            return False
        
        if title:
            task.title = title
        if description is not None:
            task.description = description
        if priority:
            task.priority = priority
        
        return True
    
    def clear_completed(self) -> int:
        """Удаляет все выполненные задачи"""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return initial_count - len(self.tasks)
    
    def to_dict(self) -> Dict:
        """Преобразует все задачи в словарь для сохранения"""
        return {
            'next_id': self.next_id,
            'tasks': [task.to_dict() for task in self.tasks]
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        """Восстанавливает менеджер из словаря"""
        manager = cls()
        manager.next_id = data['next_id']
        manager.tasks = [Task.from_dict(task_data) for task_data in data['tasks']]
        return manager