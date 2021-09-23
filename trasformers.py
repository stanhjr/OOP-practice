class Transformers:
    def __init__(self, name: str, modes: str, health: int, armor: int, age: int):
        self.name = name
        self.modes = modes
        self.health = health
        self.armor = armor
        self.age = age


class Autobot(Transformers):
    type_race = 'autobot'

    def get_info(self):
        return f"This is {self.name} \ntype: {self.type_race} \nmode: {self.modes} \nheath: {self.health} \narmor: {self.armor} \nage: {self.age}"


class Decepticon(Autobot):
    type_race = 'decepticon'


optimus_prime = Autobot('Optimus_Prime', 'truck', 200, 20, 1152)
megatron = Decepticon('Megatron', 'Gun', 195, 15, 953)

print(optimus_prime.get_info())
print()
print(megatron.get_info())
