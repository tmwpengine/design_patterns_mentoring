from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def makes_sound_to_prove_its_alive(self):
        pass


# Concrete classes Dog and Cat
class Dog(Animal):
    def makes_sound_to_prove_its_alive(self):
        print("woof woof")


class Cat(Animal):
    def makes_sound_to_prove_its_alive(self):
        print("meow")