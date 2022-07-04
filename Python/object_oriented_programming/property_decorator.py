# property decorator: access a calculeted value as a field


class WorkingStudent:
    def __init__(self, name, school, salary) -> None:
        self.name = name
        self.school = school
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5

    # A setter: function to recalculate and set a field
    @weekly_salary.setter
    def weekly_salary(self, value):
        self.salary = value/37.5



rolf = WorkingStudent("Rolf", "MIT", 15.50)
# Execute the setter
rolf.weekly_salary = 3000 