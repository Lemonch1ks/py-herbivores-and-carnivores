class Animal:
    hidden = False
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name},"
                f" Health: {self.health},"
                f" Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        elif not self.hidden:
            self.hidden = True


class Carnivore(Animal):

    @staticmethod
    def bite(obj: Animal) -> None:
        if isinstance(obj, Herbivore):
            if not obj.hidden:
                obj.health -= 50
                if obj.health <= 0:
                    Animal.alive.remove(obj)
