import random


class Transformers:
    def __init__(self, name: str, modes: str, health: int, armor: int, age: int):
        self.name = name
        self.modes = modes
        self.health = health
        self.armor = armor
        self.age = age

    def get_damaged(self, damage: int) -> float:
        self.health -= damage * self.armor / 100

    def health_info(self):
        return self.health


class Autobot(Transformers):
    type_race = 'autobot'
    phrase_list = ['insidious decepticon!', 'I am the best!', 'on guard for good!', 'Ill kill you!',
                   'you can do better']

    def get_info(self):
        return f"This is {self.name} \ntype: {self.type_race} \nmode: {self.modes} \nheath: {self.health} \narmor: {self.armor} \nage: {self.age}"

    def get_phrase(self):
        return random.choice(self.phrase_list)


class Decepticon(Autobot):
    type_race = 'decepticon'
    phrase_list = ['haha, you are too weak', 'try again', 'oh shit!', 'kill me baby', 'Ill kill you!']


optimus_prime = Autobot('Optimus_Prime', 'truck', 200, 20, 1152)
megatron = Decepticon('Megatron', 'Gun', 195, 15, 953)

side = input('Enter side d/a (Deception/Autobot')

while True:
    if side == 'd':
        bot = megatron
        break
    elif side == 'a':
        bot = optimus_prime
        break
    else:
        print('oh no no, please enter d or a')

print(bot.get_info())
print()

while bot.health > 0:
    damage_bot = int(input('Hit me!'))
    bot.get_damaged(damage_bot)
    print(bot.health_info())
    print(bot.get_phrase())

print('You Win!')
