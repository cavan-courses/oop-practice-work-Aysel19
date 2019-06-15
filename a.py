from random import randint

class GameObject:
    # Canli
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack(self, who):
        print('%s attacked %s' % (self.name, who.name))
        who.health -= self.attack


class Player(GameObject):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.score = 0


class Enemy(GameObject):
    pass


class FightArea:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        while True:
            secret = randint(1, 2)

            choice = input('1 or 2 >>> ')

            if int(choice) == secret:
                self.enemy.health -= self.player.attack
                print('Player attacked enemy by %d' % self.player.attack)
                print('Enemy has %d HP' % self.enemy.health)
            else:
                enemy_choice = randint(1, 2)


                if enemy_choice == secret:
                    self.player.health -= self.enemy.attack
                    print('Enemy attacked player by %d' % self.enemy.attack)
                    print('Player has %d HP' % self.player.health)
                else:
                    print('(facepalm)')

            if player.health <= 0:
                print('%s wins' % self.enemy.name)
                break
            elif enemy.health <= 0:
                print('%s wins' % self.player.name)
                self.player.score += 1
                break


print(Player.__mro__)

player = Player('Vagif', 100, 40)
enemy = Enemy('Putin', 100, 60)

area = FightArea(player, enemy)
area.start_battle()
