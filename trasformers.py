class Transformers:
    def __init__(self, name: str, modes: str, health: int, armor: int, age: int):
        self.name = name
        self.modes = modes
        self.health = health
        self.armor = armor
        self.age = age

    def get_info(self):
        return f"This is {self.name} \nmode {self.modes} \nheath {self.health} \narmor {self.armor} \nage {self.age}"

class Autobots(Transformers):

    def __init__(self):
        type_race = 'autobot'

optimus_prime = Transformers('Optimus_Prime', 'truck', 200, 20, 1152)

print(optimus_prime.get_info())
