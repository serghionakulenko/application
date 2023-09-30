class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print(f"{self.username} has no tasks yet.")
        else:
            print(f"Tasks for {self.username}:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def update_task(self, index, updated_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = updated_task
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            print(f"Deleted task: {deleted_task}")
        else:
            print("Invalid task index.")

class TaskManager:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        print(f"User {username} registered successfully.")

    def login_user(self, username, password):
        user = next((u for u in self.users if u.username == username), None)
        if user and user.password == password:
            return user
        else:
            print("Invalid username or password.")
            return None

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            task_manager.register_user(username, password)
        elif choice == "2":
           
