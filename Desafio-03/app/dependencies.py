from .repository import TaskRepository
from .use_cases import TaskService

# Instanciamos o repositório como um "Singleton" (única instância) para manter os dados em memória
task_repository = TaskRepository()

def get_task_service() -> TaskService:
    # Criamos a instância do caso de uso, injetando o repositório
    return TaskService(repository=task_repository)