import random
import pygame


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

# @@@@@@@@@@@@플레이어 효과음@@@@@@@@@@@
    def attack_hit(self):
        pygame.mixer.Sound("bgm/attack_normal.wav").play()

    def magic_hit(self):
        pygame.mixer.Sound("bgm/attack_magic.wav").play()

    def play_sound_effect(self, effect_file_path):
        pygame.mixer.Sound(effect_file_path).play()

        # 일반공격
    def normal_attack(self, target):
        attack_damage = random.randint(
            int(self.normal_damage*0.8), int(self.normal_damage*1.3))
        print(f"{self.name}의 별로 안아픈 공격 ! ")
        target.current_hp -= attack_damage
        print(f"{target.name}에게 {attack_damage}의 피해를 입혔다 ! ")
        target.current_hp = max(target.current_hp, 0)
        if target.current_hp == 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False

# 무기 장착 함수

    def equip_weapon(self, weapon):
        if self.weapon is None:
            self.weapon = weapon
            self.max_hp += weapon.hp
            self.max_mp += weapon.mp
            self.strength += weapon.strength
            self.dexterity += weapon.dexterity
            self.intelligence += weapon.intelligence
            print(f"{self.name}(당신)은/는 {self.weapon.name}을 장착하였습니다")
            self.update_status()
        else:
            while True:
                print(
                    f"{self.name}(당신)은/는 {self.weapon.name}을 장착 중입니다, 교체하시겠습니까? (Y/N)")
                answer = input()
                if answer.upper() == "Y":
                    self.weapon = weapon
                    self.max_hp += weapon.hp
                    self.max_mp += weapon.mp
                    self.strength += weapon.strength
                    self.dexterity += weapon.dexterity
                    self.intelligence += weapon.intelligence
                    print(f"{self.name}(당신)은/는 {weapon.name}을 장착하였습니다!")
                    self.update_status()
                    break
                elif answer.upper() == "N":
                    print(f"{self.name}(당신)은/는 {weapon.name}을 장착하지 않았습니다!")
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 선택해주세요.")

# 방어구 장착 함수
    def equip_armor(self, armor):
        if self.armor is None:
            self.armor = armor
            self.max_hp += armor.hp
            self.max_mp += armor.mp
            self.strength += armor.strength
            self.dexterity += armor.dexterity
            self.intelligence += armor.intelligence
            print(f"{self.name}(당신)은/는 {self.armor.name}을 장착하였습니다")
            self.update_status()
        else:
            while True:
                print(
                    f"{self.name}(당신)은/는 {self.armor.name}을 장착 중입니다, 교체하시겠습니까? (Y/N)")
                answer = input()
                if answer.upper() == "Y":
                    self.armor = armor
                    self.max_hp += armor.hp
                    self.max_mp += armor.mp
                    self.strength += armor.strength
                    self.dexterity += armor.dexterity
                    self.intelligence += armor.intelligence
                    print(f"{self.name}(당신)은/는 {armor.name}을 장착하였습니다!")
                    self.update_status()
                    break
                elif answer.upper() == "N":
                    print(f"{self.name}(당신)은/는 {armor.name}을 장착하지 않았습니다!")
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 선택해주세요.")

<<<<<<< HEAD

# 포션 사용 함수


    def use_hp_potion(self):
        self.current_hp = min(
            round(self.current_hp + self.max_hp*0.5), self.max_hp)
        print(f"{self.name}(당신)이 체력 포션을 사용했습니다!  hp:{self.current_hp}/{self.max_hp}  mp:{self.current_mp}/{self.max_mp}")

    def use_mp_potion(self):
        self.current_mp = min(
            round(self.current_mp + self.max_mp*0.5), self.max_mp)
        print(f"{self.name}(당신)이 마력 포션을 사용했습니다!  hp:{self.current_hp}/{self.max_hp}  mp:{self.current_mp}/{self.max_mp}")


# 여기까지


=======
>>>>>>> ba5f3d9970a42b1e117c832024b885260280760d
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
        self.skill_name = "파이참"

    def skill_attack(self, target):
        self.current_mp -= 10
        skill_damage = random.randint(
            int(self.skill_damage*1.3), int((self.skill_damage*2.0)))
        # 스킬을 쓸때마다 스킬 데미지가 힘에 비례해서 증가(버그가 아니고 기능)
        skill_damage += int(self.strength * 0.5)
        target.current_hp -= skill_damage
        print(f"{self.name}의 {self.skill_name}! ")
        print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
        target.current_hp = max(target.current_hp, 0)
        if target.current_hp == 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False

    # 캐릭터 상태
    def update_status(self):
        print(f"{self.name}(당신)의 현재 상태: HP {self.current_hp} / {self.max_hp}, MP {self.current_mp} / {self.max_mp}, 직업: 전사, 경험치:{self.current_exp} / {self.max_exp}, 레벨: {self.level} lv / 힘: {self.strength} / 민첩: {self.dexterity} / 지능: {self.intelligence}")


# 궁수 클래스
class Archer(Character):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        super().__init__(name, hp, mp, strength, dexterity, intelligence)
        self.max_hp = round(self.max_hp*1.5)   # 궁수 클래스는 체력 1.5배 / 마력 1배
        self.current_hp = round(self.current_hp*1.5)
        self.skill_damage = self.normal_damage + \
            self.dexterity*3  # 스킬데미지는 일반데미지 + 직업 특화스탯에 영향을 받음
        self.skill_name = "폭탄화살"

    def skill_attack(self, target):
        self.current_mp -= 10
        skill_damage = random.randint(
            int(self.skill_damage*1.3), int((self.skill_damage*2.0)))
        target.current_hp -= skill_damage
        print(f"{self.name}의 {self.skill_name}! ")
        print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
        target.current_hp = max(target.current_hp, 0)
        if target.current_hp == 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False

    # 캐릭터 상태
    def update_status(self):
        print(f"{self.name}(당신)의 현재 상태: HP {self.current_hp} / {self.max_hp}, MP {self.current_mp} / {self.max_mp}, 직업: 궁수, 경험치:{self.current_exp} / {self.max_exp}, 레벨: {self.level} lv / 힘: {self.strength} / 민첩: {self.dexterity} / 지능: {self.intelligence}")


# 마법사 클래스
class Magician(Character):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        super().__init__(name, hp, mp, strength, dexterity, intelligence)
        self.max_mp = self.max_mp*2  # 마법사 클래스는 체력 1배 / 마력 2배
        self.current_mp = self.current_mp*2
        self.skill_damage = self.normal_damage + \
            self.intelligence*5  # 스킬데미지는 일반데미지 + 직업 특화스탯에 영향을 받음
        self.skill_name = "py썬더"

    def skill_attack(self, target):
        self.current_mp -= 15
        skill_damage = random.randint(
            int(self.skill_damage*1.3), int((self.skill_damage*2.0)))
        target.current_hp -= skill_damage
        print(f"{self.name}의 {self.skill_name}! ")
        print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
        target.current_hp = max(target.current_hp, 0)
        if target.current_hp == 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False

    # 캐릭터 상태
    def update_status(self):
        print(f"{self.name}(당신)의 현재 상태: HP {self.current_hp} / {self.max_hp}, MP {self.current_mp} / {self.max_mp}, 직업: 마법사, \n경험치: {self.current_exp} / {self.max_exp}, 레벨: {self.level} lv / 힘: {self.strength} / 민첩: {self.dexterity} / 지능: {self.intelligence}")


# 몬스터 클래스
class Monster:
    def __init__(self, name, hp, mp, normal_damage, skill_damage, level, exp):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.max_mp = mp
        self.current_mp = mp
        self.normal_damage = normal_damage
        # self.skill_damage = skill_damage
        self.alive = True
        self.level = level
        self.exp = exp

    def normal_attack(self, target):
        attack_damage = random.randint(
            int(self.normal_damage*0.8), int(self.normal_damage*1.3))
        print(f"{self.name}의 별로 안아픈 공격 ! ")
        target.current_hp -= attack_damage
        print(f"{target.name}에게 {attack_damage}의 피해를 입혔다 ! ")
        target.current_hp = max(target.current_hp, 0)
        if target.current_hp == 0:
            print(f"{target.name}이 쓰러졌다 !")
            target.alive = False

    def update_status(self):
        print(f"[{self.name}] 현재 상태: HP {self.current_hp}/{self.max_hp}, MP {self.current_mp}/{self.max_mp} 레벨: {self.level} lv")


class Potion():
    def __init__(self, name, hp=0, mp=0, strength=0, dexterity=0, intelligence=0):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence


class DamagePotion(Potion):
    def __init__(self, name):
        super().__init__(name)

    def use(self, player):
        print(f"{player.name}이(가) {self.name}을(를) 사용합니다.")
        player.strength += 5
        player.dexterity += 5
        player.intelligence += 5
        print(f"{player.name}의 모든 스탯이 5 증가합니다.")


class DefencePotion(Potion):
    def __init__(self, name):
        super().__init__(name)

    def use(self, player):
        print(f"{player.name}이(가) {self.name}을(를) 사용합니다.")
        player.max_hp += 50
        player.current_hp += 50
        print(f"{player.name}의 최대 HP가 50 증가합니다.")


class HpPotion(Potion):
    def __init__(self, name):
        super().__init__(name)

    def use(self, player):
        print(f"{player.name}이(가) {self.name}을(를) 사용합니다.")
        player.current_hp = min(
            round(player.current_hp + player.max_hp*0.5), player.max_hp)
        print(f"{player.name}의 HP가 절반 회복됩니다.")


class MpPotion(Potion):
    def __init__(self, name):
        super().__init__(name)

    def use(self, player):
        print(f"{player.name}이(가) {self.name}을(를) 사용합니다.")
        player.current_mp = min(
            round(player.current_mp + player.max_mp*0.5), player.max_mp)
        print(f"{player.name}의 MP가 절반 회복됩니다.")

        # 경진님 아이템 클래스 끝


# armor 클래스가 상속받을 수 있게 들어가야 함
class WeaponInfo:
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    # 무기 정보 출력 함수
    def show_item(self):
        print(f"{self.name}  옵션 HP: {self.hp}  MP: {self.mp}  힘: {self.strength}  민첩: {self.dexterity}  지능: {self.intelligence}")


class ArmorInfo(WeaponInfo):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        super().__init__(name, hp, mp, strength, dexterity, intelligence)

    def show_item(self):
        super().show_item()
    # wepon클래스와 구조가 같아 상속받아 사용


damage_potion = DamagePotion("공격력 물약")
defence_potion = DefencePotion("방어력 물약")
hp_potion = HpPotion("HP 물약")
mp_potion = MpPotion("MP 물약")

potions = [damage_potion, defence_potion, hp_potion, mp_potion]

############################      찬호님  아이템 인스턴스          #########################
# 여기서 부터 인스턴스로 가져가야 함(아이템 인스턴스)
# 스테이터스 틀 만들어지면 아이템 능력치 부여


warrior_weapon_list = {
    # 전사 무기
    # name, hp, mp, strength, dexterity, intelligence 순서
    'wood_clup': WeaponInfo('wood_clup', 10, 0, 5, 0, 0),
    'great_clup': WeaponInfo('great_clup', 30, 0, 5, 5, 0),
    'battle_axe': WeaponInfo('battle_axe', 30, 20, 10, 5, 0),
    'claymore': WeaponInfo('claymore', 30, 25, 20, 5, 0),
    'great_sword': WeaponInfo('great_sword', 30, 25, 20, 10, 0),
    'flashing_light_stick': WeaponInfo('flashing_light_stick', 50, 50, 40, 20, 30)
}

archer_weapon_list = {
    # 궁수 무기
    # name, hp, mp, strength, dexterity, intelligence 순서
    'short_bow': WeaponInfo('short_bow', 10, 0, 5, 5, 0),
    'long_bow': WeaponInfo('long_bow', 10, 5, 5, 10, 15),
    'composite_bow': WeaponInfo('composite_bow', 15, 10, 5, 15, 10),
    'oriental_bow': WeaponInfo('oriental_bow', 15, 10, 10, 20, 5),
    'is_this_a_real_bow': WeaponInfo('is_this_a_real_bow', 30, 20, 15, 30, 0),
    'fire_breathing_staff': WeaponInfo('fire_breathing_staff', 50, 30, 30, 40, 30)
}

magician_weapon_list = {
    # 마법사 무기
    # name, hp, mp, strength, dexterity, intelligence 순서
    'wand': WeaponInfo('wand', 5, 20, 0, 0, 10),
    'wood_staff': WeaponInfo('wood_staff', 5, 25, 0, 5, 10),
    'Grimoire_of_Eyes_in_a_Triangle': WeaponInfo('Grimoire_of_Eyes_in_a_Triangle', 3, 3, 3, 3, 33),
    'needlessly_large_rod': WeaponInfo('needlessly_large_rod', 20, 60, 0, 0, 20),
    'elder_wand': WeaponInfo('elder_wand', 20, 50, 5, 0, 30),
    'middle_eastern_magic_wand': WeaponInfo('middle_eastern_magic_wand', 50, 50, 5, 5, 30)
}

# 방어구
# name, hp, mp, strength, dexterity, intelligence 순서
warrior_armor_list = {
    # 초반
    'cloth_armor': ArmorInfo('cloth_armor', 20, 5, 5, 0, 0),
    # 중반
    'leather_armor': ArmorInfo('leather_armor', 35, 10, 5, 5, 0),
    'chainmail': ArmorInfo('chainmail', 60, 20, 10, 10, 5),
    # 이벤트
    'thornmail': ArmorInfo('thornmail', 200, 50, 50, 10, 10)
}

archer_armor_list = {
    # 초반
    'hunter_hood': ArmorInfo('hunter_hood', 10, 10, 0, 5, 0),
    # 중반
    'assassin_cloak': ArmorInfo('assassin_cloak', 25, 10, 5, 10, 0),
    'claoak_of_agility': ArmorInfo('claoak_of_agility', 50, 25, 10, 5, 0),
    # 이벤트
    'invisibility_cloak': ArmorInfo('invisibility_cloak', 200, 60, 45, 15, 10)
}

magician_armor_list = {
    # 초반
    'old_robe': ArmorInfo('old_robe', 5, 20, 0, 0, 5),
    # 중반
    'ash_cloak': ArmorInfo('ash_cloak', 15, 20, 0, 10, 10),
    'apprentice_cloak': ArmorInfo('Apprentice Cloak', 30, 40, 0, 0, 20),
    # 이벤트
    'cloak_the_you_shall_not_pass': ArmorInfo(
        'cloak_the_you_shall_not_pass', 100, 100, 20, 20, 50)
}


# # 사용 예시
# hero = player('bob', 300, 300, 200, 200, 200)
# sword = WeaponInfo('sword', 0, 0, 0, 0, 0)
# # name, hp, mp, strength, dexterity, intelligence 순서
# plateArmor = ArmorInfo('plateArmor', 0, 0, 0, 0, 0)
# # name, hp, mp, strength, dexterity, intelligence 순서
# red_potion = potion('red_potion', (hero.max_hp-hero.current_hp), 0)
# blue_potion = potion('blue_potion', 0, (hero.max_mp-hero.current_mp))
# # 인스턴스 생성 -> 클래스지정 -> 속성값 부여

# hero.equip_wepon(sword)
# hero.equip_armor(plateArmor)
# hero.use_potion(red_potion)
# # 인스턴스 생성 -> 사용함수 -> 값
# # 사용자지정 -> 행동지정 -> 사용아이템지정


##############################################    찬호님  아이템 인스턴스 끝 ###############################


###################################  재훈 몬스터  인스턴스 ####################################
# 일반 몬스터 딕셔너리
monster_dict = {"monster1": Monster("들짐승", 50, 0, 10, 0, 1, 130),
                "monster2": Monster("늑대인간", 100, 0, 15, 0, 3, 150),
                "monster3": Monster("고블린", 120, 0, 20, 0, 4, 165),
                "monster4": Monster("거대독거미", 200, 0, 40, 0, 6, 170),
                "monster5": Monster("빨간슬라임", 200, 0, 40, 0, 6, 180),
                "monster6": Monster("케로베로스", 250, 0, 50, 0, 7, 190),
                "monster7": Monster("오우거", 300, 0, 55, 0, 7, 200),
                "monster8": Monster("서큐버스", 440, 0, 70, 0, 8, 215),
                "monster9": Monster("드라큘라", 450, 0, 80, 0, 9, 250),
                }
# 엘리트 몬스터 딕셔너리
strong_monster_dict = {
    "strong_monster1": Monster("군필여고생", 111, 0, 20, 0, 4, 240),
    "strong_monster2": Monster("케로베로스", 333, 0, 50, 0, 10, 310),
    "strong_monster3": Monster("악마", 666, 0, 100, 0, 13, 350)
}
# 보스몬스터 딕셔너리
boss_monster_dict = {
    "boss_monster1": Monster("보스몬스터1", 150, 10, 20, 35, 7, 300),
    "boss_monster2": Monster("보스몬스터2", 300, 10, 35, 50, 10, 450),
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
###################################  재훈 몬스터  인스턴스 끝####################################
