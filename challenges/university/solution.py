class University:
    def __init__(self):
        self.departments = set()

    def add_department(self, department):
        self.departments.add(department)

    def remove_department(self, department):
        self.departments.discard(department)

    def get_departments(self):
        return self.departments
