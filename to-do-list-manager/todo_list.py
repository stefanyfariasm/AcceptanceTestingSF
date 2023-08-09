class Task:
    def __init__(self, title, description, status="Pending"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(f"- {task.title} - {task.status}")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "Completed"
                break

    def clear_tasks(self):
        self.tasks = []
        
        
    def set_task_priority(self, task_index, priority):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].priority = priority
            
            
