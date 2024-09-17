from datetime import datetime


class Task:
    def __init__(self, tasks:dict = {}):
        self.tasks = tasks

    def add_task(self, description:str, deadline:datetime, completed:bool, id:int|None = None):
        if len(self.tasks) > 0:
            id = max(self.tasks.keys()) + 1
        else:
            id = 0
        self.tasks[id] = {}
        self.tasks[id]['description'] = description
        self.tasks[id]['deadline'] = deadline
        self.tasks[id]['completed'] = completed

    def completed_task(self, id:int):
        try:
            self.tasks[id]['completed'] = not self.tasks[id]['completed']
        except:
            print(f'Задача с id = {id} не найдена.')

    def current_tasks(self):
        for key, value in self.tasks.items():
            if value['completed'] == False:
                print(key, value)

# Инициализация объекта
tasks = Task()
print('Вывод данных после инициализации объекта')
print(tasks.tasks)
print()


# Добавление элементов
tasks.add_task(description='Описание', deadline='2020-10-17 00:00:00', completed=False)
tasks.add_task(description='Описание2', deadline='2020-10-15 00:00:00', completed=True)
print('Вывод данных после добавления элементов')
print(tasks.tasks)
print()

# Изменение значения атрибута completed
tasks.completed_task(0)
tasks.completed_task(1)
tasks.completed_task(2)


# Вывод словаря tasks
print('Вывод данных после изменение значения атрибута completed')
print(tasks.tasks)
print()

# Вывод активных элементов
print('Вывод активных задач')
tasks.current_tasks()