# Observable/Publish/Subject
class Speaker:
    def __init__(self):
        self.listeners = []
        self.announcement = ""

    def __str__(self):
        return f"Speaker announces  {self.announcement}"

    def add(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)
        else:
            print(f'Failed to add: {listener}')

    def notify(self):
        [listener.notify(self) for listener in self.listeners]

    def announce(self, announcement):
        self.announcement = announcement
        self.notify()


# Observers
class Listener1:
    def __init__(self):
        self.history = []

    def notify(self, speaker):
        self.history.append(speaker.announcement)
        print(f"{type(self).__name__} has heard Speaker announce '{speaker.announcement}'")


class Listener2:
    def __init__(self):
        self.history = []

    def notify(self, speaker):
        self.history.append(speaker.announcement)
        print(f"{type(self).__name__} has heard Speaker announce '{speaker.announcement}'")


class Listener3:
    def __init__(self):
        self.history = []

    def notify(self, speaker):
        self.history.append(speaker.announcement)
        print(f"{type(self).__name__} has heard Speaker announce '{speaker.announcement}'")

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

# The PUBLISHER announces something and all SUBSCRIBERS know about it
announcer.announce("All hail the new flesh")
announcer.announce("You're suffering will be legendary... EVEN IN HELL!!")

print(listener1.history)
