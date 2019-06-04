from factory.product_classes import Dog, Cat


def make_animal(animal_type):
    if animal_type == 'Dog':
        animal = Dog()
    elif animal_type == 'Cat':
        animal = Cat()
    else:
        raise Exception(f"No implementation exists for {animal_type}")

    return animal


animal = make_animal('Dog')
animal.makes_sound_to_prove_its_alive()
