from factory.product_classes import Dog, Cat


# Using a simple factory method
class SimpleAnimalFactory:
    @staticmethod
    def make_animal(animal_type):
        if animal_type == 'Dog':
            animal = Dog()
        elif animal_type == 'Cat':
            animal = Cat()
        else:
            return None

        return animal


class PetShop:
    def __init__(self, factory):
        self.factory = factory

    def buy_animal(self, animal_type):
        animal = self.factory.make_animal(animal_type)
        if animal:
            animal.makes_sound_to_prove_its_alive()
        else:
            print("No animal")


simple_factory = SimpleAnimalFactory
shop = PetShop(simple_factory)

shop.buy_animal("Dog")
