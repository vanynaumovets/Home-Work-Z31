class Person:
    name = str
    age = int
    sex = str



    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return True
        else: age < 18
        return False
    @classmethod
    def is_sort_by_sex(cls, sex):
        if sex == "man":
            return "Вы мужчина"
        else: sex == "Woman"
        return " вам не повезло"
person1 = Person("Ivan", 25, "man")
print(person1.__dict__)
print(person1.is_sort_by_sex("man"))
person2 = Person("Katya", 12, "Woman")
print(person2.__dict__)
print(person2.is_adult(12))


