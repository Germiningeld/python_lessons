class User():
    def __init__(self, id:int, name:str):
        self._id = id
        self._name = name
        self._role = 'user'

    def print_info(self):
        print(f'ID: {self._id}, Name: {self._name}, Role: {self._role}')

    def get_id(self):
        return self._id

class Admin(User):
    def __init__(self, id:int, name:str):
        super().__init__(id, name)
        self._role = 'admin'

    def add_user(self, user_list:list, id:int, name:str):
        user = User(id, name)
        user_list.append(user)

    def remove_user(self, user_list:list, id:int):
        pass
        remove_user = None
        for user in user_list:
            if user.get_id() == id:
                remove_user = user
                break
            else:
                continue

        if remove_user:
            user_list.remove(remove_user)


# Создаем список пользователей
users = []

# Создаем пользоватеря и админа
user = User(1, 'Alex')
admin = Admin(2, 'Bill')

# Добавляем в список новых пользователей через методы класса Admin
admin.add_user(users, 3, 'Ted')
admin.add_user(users, 4, 'Nik')

# Удаляем из списка пользователя с id 3
admin.remove_user(users, 3)


# Выводим данные пользоватеря и админа
user.print_info()
admin.print_info()

# Выводим пользователей из списка users
for user in users:
    user.print_info()