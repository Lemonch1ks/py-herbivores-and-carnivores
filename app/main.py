class Animal:
    hidden = False
    alive = []
    def __init__(self, name:str, health: int = 100) -> None:
        self.name = name
        self.health = health
        Animal.alive.append(self)
        ''
    def __repr__(self) -> str:
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"
class Herbivore(Animal):


    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        elif not self.hidden:
            self.hidden = True

class Carnivore(Animal):

    @staticmethod
    def bite(object: Animal) -> None:
        if isinstance(object, Herbivore):
            if not object.hidden:
                object.health -=50
                if object.health <= 0:
                    Animal.alive.remove(object)
