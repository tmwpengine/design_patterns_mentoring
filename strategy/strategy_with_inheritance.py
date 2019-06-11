class Vessel:

    def start_vessel(self):
        print("Default vessel")
        print("Going nowhere cos I don't know what type of vessel this is!!")
        print(f'Initiated from class {self.__class__.__name__}\n')


class Car(Vessel):
    def start_vessel(self):
        print("Car vessel")
        print("Slowly takes off on to the road")
        print(f'Initiated from class {self.__class__.__name__}\n')


class Aeroplane(Vessel):
    def start_vessel(self):
        print("Aeroplane vessel")
        print("Takes off down a runway and up into the air")
        print(f'Initiated from class {self.__class__.__name__}\n')


class Boat(Vessel):
    def start_vessel(self):
        print("Boat vessel")
        print("Goes slowly down the river")
        print(f'Initiated from class {self.__class__.__name__}\n')


boat = Boat()
boat.start_vessel()

aeroplane = Aeroplane()
aeroplane.start_vessel()

car = Car()
car.start_vessel()
