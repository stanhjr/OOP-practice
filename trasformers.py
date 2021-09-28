import random


class Transformer:
    def __init__(self, name: str, modes: str, health: int, armor: int):
        self.name = name
        self.modes = modes
        self.health = health
        self.armor = armor


    def get_damaged(self, damage: int) -> int:
        self.health -= int(damage * self.armor / 50)

    def health_info(self):
        return self.health

    def health_print(self):
        print('Health level = ', self.health)


class Autobot(Transformer):
    type_race = 'autobot'
    phrase_list = ['insidious decepticon!', 'I am the best!', 'on guard for good!', 'Ill kill you!',
                   'you can do better']

    def get_info(self):
        return f"Im {self.name} \ntype: {self.type_race} \nmode: {self.modes} \nheath: {self.health} \narmor: {self.armor}"

    def get_phrase(self):
        return random.choice(self.phrase_list)

    def print_phrase(self):
        print(random.choice(self.phrase_list))


class Decepticon(Autobot):
    type_race = 'decepticon'
    phrase_list = ['haha, you are too weak', 'try again', 'oh shit!', 'kill me baby', 'Ill kill you!']


optimus_prime = Autobot('Optimus_Prime', 'truck', 200, 20)
megatron = Decepticon('Megatron', 'Gun', 195, 15)

side = input('Enter side d/a (Decepticon/Autobot)')

while True:
    if side == 'a':
        bot = megatron
        break
    elif side == 'd':
        bot = optimus_prime
        break
    else:
        print('oh no no, please enter d or a')
        side = input('Enter side d/a (Deception/Autobot')

print()
print(bot.get_info())
print()

while bot.health > 0:
    damage_bot = int(input('Hit me!'))
    bot.get_damaged(damage_bot)
    if bot.health < -20:
        print("OVERKILL!")
        break

    bot.health_print()
    bot.print_phrase()

print('\nCongrarulation, You Win!')
