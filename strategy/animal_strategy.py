import time
import types


class Animal(object):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', 'Animal')
        func = kwargs.get('walk')
        if func:
            self.walk = types.MethodType(func, self)

    def walk(self):
        """This is a strategy"""
        raise NotImplementedError(f'{self.__class__.__name__} needs to implement a walk function')


def get_lamb_walk(self):
    print(f'I am a {self.name} and I dance about until I get slaughtered and devoured')


def get_bird_walk(self):
    print(f'I am a {self.name} and I fly')


lamb = Animal(name='lamb', walk=get_lamb_walk)
lamb.walk()

bird = Animal(name='bird', walk=get_bird_walk)
bird.walk()

time.sleep(1)

generic_animal = Animal()
generic_animal.walk()
