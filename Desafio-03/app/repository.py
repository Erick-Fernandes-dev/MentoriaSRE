from typing import List, Optional
from .domain import Task, TaskCreate

class TaskRepository:
    def __init__(self):
        # Simulando um banco de dados em memória
        self._db: dict[int, Task] = {}
        self._current_id: int = 1
    
    def save(self, task: Task) -> Task:
        task.id = self._current_id
        self._db[self._current_id] = task
        self._current_id += 1
        return task

    def get_all(self) -> List[Task]:
        return list(self._db.values())

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self._db.get(task_id)
