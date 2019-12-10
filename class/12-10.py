class Animal():
    def __init__(self, name):
        self.name = name


class dog(Animal):
    def __init__(self, name):
        super().__init__("小狗"+name)


a = dog("123")
print(a.name)
