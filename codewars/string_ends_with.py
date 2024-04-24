class Person:

    typ = "Person"
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def print_person(self):
        print(f"age - {self.__age}, name - {self.__name}")


# tom = Person('tom', 77)
# tom.print_person()
# tom.__age = 100
# tom.print_person()
# tom.set_age(100)
# tom.print_person()



# if __name__ == '__main__':
#     print(solution("(])"))