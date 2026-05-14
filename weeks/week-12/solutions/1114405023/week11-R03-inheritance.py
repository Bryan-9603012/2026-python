class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} 發出聲音"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"

class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵～"

class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def speak(self):
        base = super().speak()
        return f"{base}（導盲犬，主人：{self.owner}）"

d = Dog("小黑")
c = Cat("咪咪")
g = GuideDog("阿金", "王伯伯")

for animal in [d, c, g]:
    print(animal.speak())

print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(d, Cat))

print(issubclass(Dog, Animal))
print(issubclass(Cat, Dog))

def make_sounds(animals: list):
    for a in animals:
        print(a.speak())

make_sounds([d, c, g])
