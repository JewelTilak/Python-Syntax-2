class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__password = "Jewel@0191"

    def get_password(self):
        return self.__password

person = Person("Alice", 30)
print(person.name)
print(person._age)          
print(person.__password)
print(person.get_password())
