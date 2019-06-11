import types


class Vessel:
    def __init__(self, func=None):
        if func:
            self.status = "In vessel"
            self.start_vessel = types.MethodType(func, self)
            self.class_name = f'{self.__class__.__name__} and function {func.__name__}'
        else:
            self.class_name = self.__class__.__name__

    def start_vessel(self):
        """This is a strategy"""

        print("Default vessel")
        print("Going nowhere cos I don't know what type of vessel this is!!")
        print(f'Initiated from class {self.class_name}\n')


def start_car(self):
    print("Car vessel")
    print("Slowly takes off on to the road")
    print(self.status)
    print(f'Initiated from class {self.class_name}\n')


def start_aeroplane(self):
    print("Aeroplane vessel")
    print("Takes off down a runway and up into the air")
    print(self.status)
    print(f'Initiated from class {self.class_name}\n')


def start_boat(self):
    print("Boat vessel")
    print("Goes slowly down the river")
    print(self.status)
    print(f'Initiated from class {self.class_name}\n')


default = Vessel()
default.start_vessel()

car = Vessel(start_car)
car.start_vessel()

aeroplane = Vessel(start_aeroplane)
aeroplane.start_vessel()

boat = Vessel(start_boat)
boat.start_vessel()
