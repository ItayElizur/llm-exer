from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    priority: str = "medium"


class TaskManager:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, priority: str = "medium") -> Task:
        """Add a new task and return it."""
        task = Task(id=self._next_id, title=title, priority=priority)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_pending_tasks(self) -> List[Task]:
        """Return all incomplete tasks."""
        return [task for task in self._tasks if not task.completed]

    def mark_completed(self, task_id: int) -> bool:
        """Mark a task as completed. Returns True if successful."""
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                return True
        return False
