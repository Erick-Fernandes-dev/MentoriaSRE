from .domain import Task, TaskCreate
from .repository import TaskRepository

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository
    
    def create_task(self, task_data: TaskCreate) -> Task:
        # Regra de negócio: O título da tarefa não pode ter menos de 3 caracteres
        if len(task_data.title) < 3:
            raise ValueError("O título da tarefa deve ter pelo menos 3 caracteres.")
        
        new_task = Task(
            title=task_data.title,
            description=task_data.description,
        )

        return self.repository.save(new_task)

    def list_tasks(self) -> list[Task]:
        return self.repository.get_all()
        