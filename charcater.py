import random
import sys
import os
# 캐릭터 클래스 스탯당 공격력추가 , 레벨업, 레벨업마다 스탯증가 구현 필요


class Character:
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        self.name = name
        self.max_hp = hp
        self.current_hp = self.max_hp
        self.max_mp = mp
        self.current_mp = self.max_mp
        self.level = 1
        self.max_exp = 100
        self.current_exp = 0    # 처음 경험치는 0으로 시작해서 몬스터를 잡을때마다 올라야함
        # 잉여경험치 = 현재경험치 - 최대경험치 / 현재 경험치 초기화 후에 +잉여경험치
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.normal_damage = self.strength*1.5 + self.dexterity + \
            self.intelligence*0.5  # 일반데미지는 힘3:민첩2:지능1 비율로 영향
        self.alive = True
        self.weapon = None
        self.armor = None

    def normal_attack(self, target):
        attack_damage = random.randint(
            int(self.normal_damage*0.8), int(self.normal_damage*1.3))
        print(f"{self.name}의 별로 안아픈 공격 ! ")
        target.current_hp -= attack_damage
        print(f"{target.name}에게 {attack_damage}의 피해를 입혔다 ! ")
        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False

    # def skill_attack(self, target):
    #     self.current_mp -= 10
    #     if self.current_mp - 10 < 0:
    #         print("마나가 부족합니다")
    #         return
    #     skill_damage = random.randint(
    #         int(self.skill_damage*1.3), int((self.skill_damage*2.0)))
    #     target.current_hp -= skill_damage
    #     print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
    #     if target.current_hp <= 0:
    #         print(f"{target.name}이 쓰러졌다 !")
    #         self.alive = False

    # 캐릭터 상태
    def update_status(self):
        print(f"{self.name}의 현재 상태: HP {self.current_hp} / {self.max_hp}, MP {self.current_mp} / {self.max_mp}, 경험치:{self.current_exp} / {self.max_exp} 레벨 :{self.level} lv / 힘 : {self.strength} / 민첩 : {self.dexterity} / 지능 : {self.intelligence}")

    # 아이템 획득 작성 칸 get_item
    # 아이템 종류 및 능력치는 찬호님이 고쳐주시겠죠??
    @staticmethod
    def get_item():
        items = [Weapon("무기", 10), Armor("갑옷", 20),
                 Potion("포션", 30), Junk("꽝!")]
        item = random.choice(items)
        return item

    # 무기 장착 함수
    def equip_weapon(self, weapon):
        if self.weapon is None:
            self.wepon = weapon
            self.max_hp += weapon.hp
            self.max_mp += weapon.mp
            self.strength += weapon.strength
            self.dexterity += weapon.dexterity
            self.intelligence += weapon.intelligence
            print(f"{self.name}은 {self.weapon.name}을 장착하였습니다")
            self.update_status()
        else:
            while True:
                answer = input(
                    f"{self.name}은 {self.weapon.name}을 장착 중입니다, 교체하시겠습니까? (Y/N)")
                if answer.upper() == "Y":
                    self.wepon = weapon
                    self.max_hp += weapon.hp
                    self.max_mp += weapon.mp
                    self.strength += weapon.strength
                    self.dexterity += weapon.dexterity
                    self.intelligence += weapon.intelligence
                    print(f"{self.name}은 {weapon.name}을 장착하였습니다!")
                    self.update_status()
                    break
                elif answer.upper() == "N":
                    print(f"{self.name}은 {weapon.name}을 장착하지 않았습니다!")
                    break
                else:
                    print("Y/N 으로 입력해주세요.")


# 방어구 장착 함수

    def equip_armor(self, armor):
        if self.armor is None:
            self.armor = armor
            self.max_hp += armor.hp
            self.max_mp += armor.mp
            self.strength += armor.strength
            self.dexterity += armor.dexterity
            self.intelligence += armor.intelligence
            print(f"{self.name}은 {self.armor.name}을 장착하였습니다")
            self.update_status()
        else:
            while True:
                answer = input(
                    f"{self.name}은 {self.armor.name}을 장착 중입니다, 교체하시겠습니까? (Y/N)")
                if answer.upper() == "Y":
                    self.armor = armor
                    self.max_hp += armor.hp
                    self.max_mp += armor.mp
                    self.strength += armor.strength
                    self.dexterity += armor.dexterity
                    self.intelligence += armor.intelligence
                    print(f"{self.name}은 {armor.name}을 장착하였습니다!")
                    self.update_status()
                    break
                elif answer.upper() == "N":
                    print(f"{self.name}은 {armor.name}을 장착하지 않았습니다!")
                    break
                else:
                    print("Y/N 으로 입력해주세요.")


# 포션 사용 함수

    def use_potion(self, potion):
        self.hp += potion.hp_recovery
        self.mp += potion.mp_recovery
        print(f"{self.name}이 {potion.name}을 사용했습니다!")
        self.update_status()


# 전사 클래스
class Warrior(Character):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        super().__init__(name, hp, mp, strength, dexterity, intelligence)
        self.max_hp = self.max_hp*2
        self.current_hp = self.current_hp*2  # 전사 클래스는 체력 2배 / 마력 0.5배
        self.max_mp = round(self.max_mp*0.5)
        self.current_mp = round(self.current_mp*0.5)
        self.skill_damage = self.normal_damage + \
            self.strength*3  # 스킬데미지는 일반데미지 + 직업 특화스탯에 영향을 받음
        self.warrior_skill_name = "파이참"
        # self.normal_damage = normal_damage + strength * 0.3

    def skill_attack(self, target):
        self.current_mp -= 20
        if self.current_mp - 20 < 0:
            print("마나가 부족합니다")
            return
        skill_damage = random.randint(
            int(self.skill_damage*1.3), int((self.skill_damage*2.0)))
        # 스킬을 쓸때마다 스킬 데미지가 힘에 비례해서 증가(버그가 아니고 기능)
        skill_damage += int(self.strength * 0.5)
        target.current_hp -= skill_damage
        print(f"{self.name}의 {self.warrior_skill_name}! ")
        print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False


# 궁수 클래스
class Archer(Character):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        super().__init__(name, hp, mp, strength, dexterity, intelligence)
        self.max_hp = round(self.max_hp*1.5)   # 궁수 클래스는 체력 1.5배 / 마력 1배
        self.current_hp = round(self.current_hp*1.5)
        self.skill_damage = self.normal_damage + \
            self.dexterity*3  # 스킬데미지는 일반데미지 + 직업 특화스탯에 영향을 받음
        self.archer_skill_name = "폭탄화살"

    def skill_attack(self, target):
        self.current_mp -= 15
        if self.current_mp - 15 < 0:
            print("마나가 부족합니다")
            return
        skill_damage = random.randint(
            int(self.skill_damage*1.3), int((self.skill_damage*2.0)))
        target.current_hp -= skill_damage
        print(f"{self.name}의 {self.archer_skill_name}! ")
        print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False


# 마법사 클래스
class Magician(Character):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        super().__init__(name, hp, mp, strength, dexterity, intelligence)
        self.max_mp = self.max_mp*2  # 마법사 클래스는 체력 1배 / 마력 2배
        self.current_mp = self.current_mp*2
        self.skill_damage = self.normal_damage + \
            self.intelligence*5  # 스킬데미지는 일반데미지 + 직업 특화스탯에 영향을 받음
        self.magician_skill_name = "py썬더"

    def skill_attack(self, target):
        self.current_mp -= 30
        if self.current_mp - 30 < 0:
            print("마나가 부족합니다")
            return
        skill_damage = random.randint(
            int(self.skill_damage*1.3), int((self.skill_damage*2.0)))
        target.current_hp -= skill_damage
        print(f"{self.name}의 {self.magician_skill_name}! ")
        print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False


# 몬스터 클레스
class Monster:
    def __init__(self, name, hp, mp, normal_damage, skill_damage, level, exp):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.max_mp = mp
        self.current_mp = mp
        self.normal_damage = normal_damage
        self.skill_damage = skill_damage
        self.alive = True
        self.level = level
        self.exp = exp

    def normal_attack(self, target):
        attack_damage = random.randint(
            int(self.normal_damage*0.8), int(self.normal_damage*1.3))
        print(f"{self.name}의 별로 안아픈 공격 ! ")
        target.current_hp -= attack_damage
        print(f"{target.name}에게 {attack_damage}의 피해를 입혔다 ! ")
        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False

    # def skill_attack(self, target):
    #     if self.current_mp - 10 < 0:
    #         print("마나가 부족합니다")
    #         return
    #     print(f"{self.name}의 뼈저리는 공격 ! ")
    #     skill_damage = random.randint(
    #         int(self.skill_attack * 1.3), int(self.skill_attack * 2.0))
    #     target.current_hp -= skill_damage
    #     self.current_mp -= 10
    #     print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
    #     if target.current_hp <= 0:
    #         print(f"{target.name}이 쓰러졌다 !")
    #         self.alive = False

    def update_status(self):
        print(f"{self.name}의 현재 상태: HP {self.current_hp}/{self.max_hp}, MP {self.current_mp}/{self.max_mp} 레벨 :{self.level} lv")

    # 아이템 드랍 작성 칸 drop_item
    # 아이템 드랍, 4종류의 하위 품목은 따로 만들어야 함  인스턴스 만들어놓고
    # 이것도 찬호님이 고쳐주시겠죠?? 전투부분에서 print랑 함수로 처리하는게 좋을 거 같습니다
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

# 아이템 클래스 작성 칸 class Item(self, player)
# 아이템 클래스에 왜 hp, mp, power가 있냐면,
# 아이템이 저 능력치를 가지고 있으며 능력치만큼 플레이어가 강화되기 때문입니다. 이 부분은 wepon armor class랑 기능이 비슷하네요


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
        print(f"하지만 효과가 없습니다...{self.name}은 쓸모가 없습니다...")


class WeaponInfo:
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
# 더 해줄 능력치 작성
# name, hp, mp, strength, dexterity, intelligence

# 무기 정보 출력 함수
    def show_item(self):
        print(f"{self.name}  옵션 hp:{self.hp}  mp:{self.mp}  strength:{self.strength}  dexterity:{self.dexterity}  intelligence:{self.intelligence}")


class ArmorInfo(WeaponInfo):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        super().__init__(name, hp, mp, strength, dexterity, intelligence)

    def show_item(self):
        super().show_item()
# wepon클래스와 구조가 같아 상속받아 사용


# 포션 생성 클래스
class PotionInfo:
    def __init__(self, name, hp_recovery, mp_recovery):
        self.name = name
        self.hp_recovery = hp_recovery
        self.mp_recovery = mp_recovery


# 포션
red_potion = PotionInfo('red_potion', (you.max_hp-you.current_hp), 0)
blue_potion = PotionInfo('blue_potion', 0, (you.max_mp-you.current_mp))

# 전사 무기
# name, hp, mp, strength, dexterity, intelligence 순서
wood_clup = WeaponInfo('wood_clup', 10, 0, 5, 0, 0)
great_clup = WeaponInfo('great_clup', 30, 0, 5, 5, 0)
battle_axe = WeaponInfo('battle_axe', 30, 20, 10, 5, 0)
claymore = WeaponInfo('claymore', 30, 25, 20, 5, 0)
short_sword = WeaponInfo('short_sword', 10, 0, 10, 0, 0)
great_sword = WeaponInfo('great_sword', 30, 0, 60, 10, 0)
flashing_light_stick = WeaponInfo('flashing_light_stick', 50, 50, 100, 100, 30)

# 궁수 무기
# name, hp, mp, strength, dexterity, intelligence 순서
short_bow = WeaponInfo('short_bow', 10, 10, 20, 5, 10)
long_bow = WeaponInfo('long_bow', 15, 5, 30, 10, 15)
composite_bow = WeaponInfo('composite_bow', 15, 10, 30, 15, 10)
oriental_bow = WeaponInfo('oriental_bow', 20, 20, 30, 30, 30)
is_this_a_real_bow = WeaponInfo('is_this_a_real_bow', 50, 50, 50, 50, 0)
fire_breathing_staff = WeaponInfo('fire_breathing_staff', 5, 5, 100, 0, 30)

# 마법사 무기
# name, hp, mp, strength, dexterity, intelligence 순서
wand = WeaponInfo('wand', 5, 20, 5, 20, 10)
wood_staff = WeaponInfo('wood_staff', 5, 25, 5, 25, 10)
Grimoire_of_Eyes_in_a_Triangle = (
    'Grimoire_of_Eyes_in_a_Triangle', 3, 33, 3, 33, 3)
needlessly_large_rod = ('needlessly_large_rod', 5, 60, 0, 60, 0)
elder_wand = WeaponInfo('elder_wand', 20, 30, 5, 50, 0)
middle_eastern_magic_wand = WeaponInfo(
    'middle_eastern_magic_wand', 50, 50, 100, 100, 20)


# 일반 몬스터 딕셔너리
monster_dict = {"monster1": Monster("들짐승", 50, 0, 10, 0, 1, 100),
                "monster2": Monster("늑대인간", 100, 0, 15, 0, 3, 130),
                "monster3": Monster("고블린", 120, 0, 20, 0, 4, 135),
                "monster4": Monster("거대독거미", 200, 0, 40, 0, 6, 150),
                "monster5": Monster("빨간슬라임", 200, 0, 40, 0, 6, 150),
                "monster6": Monster("케로베로스", 250, 0, 50, 0, 7, 160),
                "monster7": Monster("오우거", 300, 0, 55, 0, 7, 160),
                "monster8": Monster("서큐버스", 440, 0, 70, 0, 8, 185),
                "monster9": Monster("드라큘라", 450, 0, 80, 0, 9, 190),
                }
# 엘리트 몬스터 딕셔너리
strong_monster_dict = {
    "strong_monster1": Monster("군필여고생", 111, 0, 20, 0, 4, 140),
    "strong_monster2": Monster("케로베로스", 333, 0, 50, 0, 10, 190),
    "strong_monster3": Monster("악마", 666, 0, 100, 0, 13, 250)
}
# 보스몬스터 딕셔너리
boss_monster_dict = {
    "boss_monster1": Monster("보스몬스터1", 150, 10, 20, 35, 7, 170),
    "boss_monster2": Monster("보스몬스터2", 300, 10, 35, 50, 10, 200),
    "boss_monster3": Monster("어금니", 999, 20, 120, 150, 99, 999)
}

# 층별 몬스터
floor1 = [monster_dict["monster1"]]
floor2 = [monster_dict["monster1"], monster_dict["monster2"]]
floor3 = [monster_dict["monster1"],
          monster_dict["monster2"], monster_dict["monster3"]]
floor4 = [monster_dict["monster2"], monster_dict["monster3"],
          strong_monster_dict["strong_monster1"]]
floor5 = [boss_monster_dict["boss_monster1"]]
floor6 = [monster_dict["monster4"]]
floor7 = [monster_dict["monster4"], monster_dict["monster5"]]
floor8 = [monster_dict["monster4"],
          monster_dict["monster5"], monster_dict["monster6"]]
floor9 = [monster_dict["monster5"], monster_dict["monster6"],
          strong_monster_dict["strong_monster2"]]
floor10 = [boss_monster_dict["boss_monster2"]]
floor11 = [monster_dict["monster7"]]
floor12 = [monster_dict["monster7"], monster_dict["monster8"]]
floor13 = [monster_dict["monster7"],
           monster_dict["monster8"], monster_dict["monster9"]]
floor14 = [monster_dict["monster8"], monster_dict["monster9"],
           strong_monster_dict["strong_monster3"]]
floor15 = [boss_monster_dict["boss_monster3"]]


print("플레이어 이름 입력 :  ")
character_name = input(" ")

print(f"당신은{character_name}이군요")

# 주사위를 굴리라는 안내멘트
stat_str = random.randint(5, 10)
stat_dex = random.randint(5, 10)
stat_int = random.randint(5, 10)

print(f"힘 : {stat_str}  민첩 : {stat_dex}  지능 : {stat_int}")

print("직업 선택 ? 1: 전사  2: 궁수  3: 마법사")
select_character = input()
if select_character == "1":
    you = Warrior(f"{character_name}", 300, 200, stat_str, stat_dex, stat_int)
    # 이부분이 처음에 스탯을 주사위로 랜덤으로 하려고 했었죠? 네네
    # 그럼 주사위를 굴리고 나서 직업을 선택해야겠죠..네!!
elif select_character == "2":
    you = Archer(f"{character_name}", 300, 200, stat_str, stat_dex, stat_int)
elif select_character == "3":
    you = Magician(f"{character_name}", 300, 200, stat_str, stat_dex, stat_int)
else:
    print("잘못된 입력입니다. 다시 선택해주세요.")
    you = None

# 현재 층
floor = 1
while floor <= 15:
    # 현재 층의 몬스터 리스트 가져오기
    monster_list = classes.eval(f"floor{floor}")

    print(f"\n{floor}층에 입장했습니다. 이곳에서는 {len(monster_list)}마리의 몬스터와 전투합니다.")

    # 14층에 대한 이벤트 작성 칸...나중에 입력할게요 넵

    for i, thismonster in enumerate(monster_list):
        print(f"\n{i+1}번째 몬스터와의 전투가 시작됩니다.")
        # 플레이어와 몬스터의 상태 업데이트 출력하기
        thismonster.update_status()
        you.update_status()

        # 플레이어의 행동 받기
        action = input("다음 중 알맞는 정답을 고르시오. 1: 일반 공격 2: 스킬 공격 3:(없음)")

        # 플레이어의 행동에 따라 몬스터 공격이나 포션 사용하기
        if action == "1":
            you.normal_attack(thismonster)
        elif action == "2":
            you.skill_attack(thismonster)
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
            continue

        # 몬스터가 살아있는 경우 몬스터가 플레이어를 공격하기
        if thismonster.alive:
            thismonster.normal_attack(you)

        # 플레이어가 죽은 경우 게임 종료하기
        if not you.alive:
            print("당신은 죽었습니다. 게임 오버")
            sys.exit()

        # 몬스터가 죽은 경우 경험치와 레벨업 처리하기
        if not thismonster.alive:
            print(f"{thismonster.name}을(를) 처치하여 {thismonster.exp}의 경험치를 얻었습니다.")
            you.current_exp += thismonster.exp
            if you.current_exp >= you.max_exp:
                you.level += 1
                you.current_exp = you.current_exp - you.max_exp
                you.max_exp += 100
                print(f"축하합니다! {you.level} 레벨이 되었습니다.")
                print("능력치를 선택해 주세요.")
                print("1: 힘, 2: 민첩성, 3: 지능")
                stat_choice = input()
                if stat_choice == "1":
                    you.strength += 1
                elif stat_choice == "2":
                    you.dexterity += 1
                elif stat_choice == "3":
                    you.intelligence += 1
                else:
                    print("잘못된 입력입니다. 능력치 상승 없이 진행합니다.")
# print(f"장비를 획득했습니다! {wood_clup.name}")
# 장비 인스턴스 넣고 이 부분에서 wood_clup.show_item()으로 정보 보여준 다음에
# player.equip_wepon(wood_clup)으로 장착 함수 돌릴 수 있을까요
    print(f"\n{floor}층을 클리어하셨습니다!")
    floor += 1
