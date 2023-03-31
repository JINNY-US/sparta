import random


class Player:
    def __init__(self, name, hp, mp, power):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.power = power
        self.items = []

    def normal_attack(self, monster):
        damage = random.randint(self.power - 2, self.power + 2)
        monster.hp -= damage
        print(f"{self.name}이(가) {monster.name}에게 일반공격으로 {damage}의 데미지를 입혔습니다.")

    def magic_attack(self, monster):
        if self.mp >= 3:
            self.mp -= 3
            damage = random.randint(self.power, self.power + 5)
            monster.hp -= damage
            print(f"{self.name}이(가) {monster.name}에게 마법공격으로 {damage}의 데미지를 입혔습니다.")
        else:
            print(f"{self.name}의 MP가 부족합니다.")

    @staticmethod
    def get_item():
        items = [Weapon("무기", 10), Armor("갑옷", 20),
                 Potion("포션", 30), Junk("꽝!")]
        item = random.choice(items)
        return item

    def show_status(self):
        print(f"{self.name}의 현재 상태: HP {self.hp}, MP {self.mp}")
        # print("보유 아이템:")
        # for item in self.items:
        #     print(f"- {item.name} ({item.kind})")


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def normal_attack(self, player):
        damage = random.randint(self.power - 1, self.power + 1)
        player.hp -= damage
        print(f"{self.name}이(가) {player.name}에게 일반공격으로 {damage}의 데미지를 입혔습니다.")

    def drop_item(self):
        items = [
            Item("무기"),
            Item("갑옷"),
            Item("포션"),
            Item("꽝"),
        ]
        item = random.choice(items)
        item_name = item.name
        print(f"{self.name}을(를) 물리쳤습니다! {item.name}을(를) 얻었습니다.")
        return item_name


class Item:
    def __init__(self, name, hp=0, mp=0, power=0):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.power = power

    # def use(self, player):
    #     print(f"{player.name}이(가) {self.name}을(를) 사용합니다.")
    #     # print(f"{self.name}: HP {self.hp}, MP {self.mp}, power {self.power}")


class Weapon(Item):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def use(self, player):
        print(f"{player.name}이(가) {self.name}을(를) 장착합니다.")
        player.power += self.power


class Armor(Item):
    def __init__(self, name, hp):
        super().__init__(name)
        self.hp = hp

    def use(self, player):
        print(f"{player.name}이(가) {self.name}을(를) 장착합니다.")
        player.hp += self.hp


class Potion(Item):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

    def use(self, player):
        print(f"{player.name}이(가) {self.name}을(를) 사용합니다.")
        player.hp += self.amount
        player.mp += self.amount
        print(f"{player.name}의 HP와 MP가 {self.amount}만큼 회복됩니다.")


class Junk(Item):
    def __init__(self, name):
        super().__init__(name)

    def use(self, player):
        print(f"{player.name}이(가) {self.name}을(를) 사용합니다.")
        print(f"하지만 효과가 없습니다...{self.name}은 쓸모가 없습니다...버리시길..")


player_name = input("플레이어의 이름을 입력하세요: ")
player = Player(player_name, 50, 20, 10)
monster = Monster("슬라임", 30, 8)

print(f"{player.name} vs {monster.name} 전투를 시작합니다!")

while player.hp > 0 and monster.hp > 0:
    print("="*20)
    print(f"{player.name}: HP {player.hp}, MP {player.mp}")
    print(f"{monster.name}: HP {monster.hp}")
    print("="*20)

    choice = input("어떤 공격을 하시겠습니까? (1. 일반공격 / 2. 마법공격) ")
    if choice == "1":
        player.normal_attack(monster)
    elif choice == "2":
        player.magic_attack(monster)
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")
        continue

    if monster.hp <= 0:
        print(f"{player.name}이(가) {monster.name}을(를) 물리쳤습니다!")
        item_name = monster.drop_item()

        use_item = input("아이템을 자동으로 사용합니다.")
        # if item_name == "무기":
        #     Weapon.use(Item, player)
        # elif item_name == "갑옷":
        #     Armor.use(Item, player)
        # elif item_name == "포션":
        #     Potion.use(Item, player)
        # else:
        #     Junk.use(Item, player)

        # item = Item(item_name)
        # item.use(player)
        next_battle = input("다음 전투로 넘어가시겠습니까? (1. 예 / 2. 아니오) ")
        if next_battle == "1":
            monster = Monster("슬라임", 30, 8)
            continue
        else:
            break

    monster.normal_attack(player)
    if player.hp <= 0:
        print(f"{monster.name}이(가) {player.name}을(를) 물리쳤습니다...")
        break
