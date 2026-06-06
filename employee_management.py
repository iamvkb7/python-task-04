class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working")


class Manager(Employee):
    def manage(self):
        print(f"{self.name} is managing the team")


manager = Manager("Sameer")

manager.work()
manager.manage()
