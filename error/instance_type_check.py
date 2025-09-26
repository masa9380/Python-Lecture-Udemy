class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name} is walking!')


class Dog(Animal):
    def bark(self):
        print(f'{self.name} is barking!')


def walk_with_me(animal: Animal) -> None:
    # if type(animal) is Animal:    # このように記述すると、継承をした際に不都合がでる。そのため、isinstanceを用いて判別する
    # if isinstance(animal, Animal):    # もっというと、データの型よりも.walkというattributeを持っているかどうかが重要
    method = getattr(animal, "walk", None)
    if callable(method):
        animal.walk()
    else:
        raise TypeError(f'{type(animal).__name__}は散歩(walk)できません')


if __name__ == '__main__':
    pochi = Dog('Pochi')
    walk_with_me(pochi)
    print(dir(pochi))