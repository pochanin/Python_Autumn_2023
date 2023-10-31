class Person:
    def __init__(self, full_name):
        self.full_name = full_name

    def __str__(self):
        return self.full_name[::-1].replace(' ', ' ')

p = Person('Иванов Михаил Федорович')
print(p)