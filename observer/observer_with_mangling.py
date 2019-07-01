"""Data mangling is not related to the Observer pattern, nor do I promote the technique in Python, but this is a
good opportunity to show a use case.
"""


# Observable
class Speaker:
    def __init__(self):
        self.listeners = []
        self.__announcement = ""

    def __str__(self):
        return f"Speaker announces  {self.announcement}"

    def add(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)
        else:
            print(f'Failed to add: {listener}')

    def notify(self):
        [o.notify(self) for o in self.listeners]

    @property
    def announcement(self):
        return self.__announcement

    @announcement.setter
    def announcement(self, new_value):
        self.__announcement = new_value
        self.notify()


# Observers
class Listener1:
    def __init__(self):
        self.history = []

    def notify(self, speaker):
        self.history.append(speaker.announcement)


class Listener2:
    def __init__(self):
        self.history = []

    def notify(self, speaker):
        self.history.append(speaker.announcement)


class Listener3:
    def __init__(self):
        self.history = []

    def notify(self, speaker):
        self.history.append(speaker.announcement)

# Following the pattern:

# Instantiate the PUBLISHER, also known as the OBSERVABLE, also know as the SUBJECT
announcer = Speaker()

# Instantiate the SUBSCRIBER, also know as the OBSERVER
listener1 = Listener1()
listener2 = Listener2()
listener3 = Listener3()

# Register the SUBSCRIBERS with the PUBLISHER
announcer.add(listener1)
announcer.add(listener2)
announcer.add(listener3)

announcer.announcement = "On your knees BOY!!"
announcer.announcement = "Suck my shin!!"

print(listener1.history)
print(listener2.history)
print(listener3.history)
