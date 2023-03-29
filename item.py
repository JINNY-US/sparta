import random


class Character:
    def __init__(self, name, hp, mp, power, magic_power, luck):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.magic_power = magic_power
        self.luck = luck

# 게임 내 캐릭터가 공유하는 스텟(임의)
# name
# he
# mp
# power
# magic_power
# attack
# magic_attack
# luck

    def dice(self):
        pass
    # dice 함수는 모든 액션에 사용됨
    # Character(player, monster)의 luck에 의해 출력되는 값의 범위를 다르게 함
    # ex)if self.luck >= 30:
    #       return random.randrange(4,7)
    #    elif self.luck >= 15:
    #       return radom.randrange(3,7)
    #    else:
    #       return radom.randrange(1,5)
    # 공격 타입(attack, magic_attack)을 강제함 4이상일 경우 magic_attack 사용가능
    # damage 주사위의 수+power 만큼 추가(다른 기능 생각 중)

    def nomal_attack(self, target):
        pass
    # damage는 주사위의 수 + power의 값
    # damage = self.dice() + self.power
    # targe.hp -= damage

    def magic_attack(self, target):
        pass
    # mp가 소모되어야 하기 때문에 if문 사용
    #   if self.mp >= 10:
    #       damage = self.dice() + self.magic_power
    #       self.mp -= 10
    #       target.hp -= damage
    #   else:
    #       print(f"{self.name}의 mp가 부족합니다")

    def attack_style(self, target):
        pass
    # self.dice의 값을 가져와 공격스타일에 조건을 줌
    # self.dice의 값이 4 이상이면 magic_attack와 nomal_attack 둘 다 사용가능
    # self.dice의 값이 3 이상이면 namal_attack만 사용가능
    # player의 경우에는 input값을 사용해야 하지만 monster는 자동적으로 선택하는 기능이 필요
    # 두 가지로 구현하여 각각 class에 넣어줘야 함 이건 예시
    # dice_vla = self.dice()

    # if dice_val >= 4:
    #   style_choice = input("공격 방법을 선택하세요! 일반공격: 1 | 마법 공격: 2")
    #   if style_choice == "1":
    #       self.nomal_attack(target)
    #   elif style_choice == "2":
    #       self.magic_attack(target)
    #   else:
    #       print('잘못된 선택입니다 일반공격: 1 | 마법공격: 2')
    # else:
    #   self.nomal_attack(target) < 4 미만일 때 자동적으로 nomal_attack

    def show_status(self):
        pass
    # 전투 시 이름, 남은 hp /총 hp, 남은 mp /총 mp를 보여줌
    # print(f"{self.name}  hp:{self.hp}/{self.max_hp} mp:{self.mp}/{self.max_mp}")
# ///////////////////////////////

    # 기능 구현 (사용했던 코드 재활용/다듬어야 함)
    # 캐릭터 생성 및 스텟 찍는 코드
    # print('캐락터를 생성합니다')
    # character_name = str(input(" "))
    # print('캐릭터의 스텟을 설정합니다')
    # player = Character(character_name, 100, 100, 30, 30, 10) <=생성 시 이름 + 기초 포인트
    # print('hp:100  mp:100 nomal_power(pw):30  magic_power(mpw):30 luck:10  남은 포인트:20')
    # point = 20
    # while point > 0:
    #     new_status = str(input(" "))
    #     if new_status == 'hp':
    #         player.hp += 1
    #         point -= 1
    #         print(f"hp + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    #         continue
    #     elif new_status == 'mp':
    #         player.mp += 1
    #         point -= 1
    #         print(f"mp + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    #     elif new_status == 'pw':
    #         player.nomal_power += 1
    #         point -= 1
    #         print(f"nomal_power + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    #     elif new_status == 'mpw':
    #         player.magic_power += 1
    #         point -= 1
    #         print(f"magic_power + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    # #     elif new_status == 'luck':
    #         player.luck += 1
    #         point -= 1
    #         print(f"luck + 1  남은 point:{point}")
    #         print(f"""
    #         hp:{player.hp}  mp:{player.mp}
    #         nomal_power:{player.nomal_power} magic_power:{player.magic_power} luck:{play.luck}
    #         """)
    #     else:
    #         break
    # print(f"{character_name}님의 스테이터스는 hp:{hp}  mp:{mp} power:{power} magig_power:{magic_power}  luck:{luck} 입니다")


class player(Character):
    pass
# 아이템을 장착할 공간 필요
#   def __init__(self, name, hp, mp, power, magic_power, luck)
#       super().__init__(name, hp, mp, power, magic_power, luck)
#       self.wepon = None
#       self.armor = None

# 무기 장착 함수
#   def equip_wepon(self, wepon):
#       if self.wepon is None:
#            self.wepon = wepon
#            self.power += wepon.power
#            self.magic_power += wepon.magic_power
#            self.hp += wepon.hp
#            self.mp += wepon.mp
#            self.luck += wepon.luck
#            print(f"{self.name}은 {self.wepon.name}을 장착하였습니다")
#            self.show_status()
#       else:
#           answer = input(f"{self.name}은 {self.wepon.name}을 장착 중입니다, 교체하시겠습니까? (Y/N)")
#           if answer.upper() =="Y":   <-upper()은 값을 모두 대문자로 받기위해 사용
#               self.wepon = wepon
#               self.power += wepon.power
#               self.magic_power += wepon.magic_power
#               self.hp += wepon.hp
#               self.mp += wepon.mp
#               self.luck += wepon.luck
#               print(f"{self.name}은 {wepon.name}을 장착하였습니다!")
#               self.show_status()
#           else:
#               print(f"{self.name}은 {wepon.name}을 장착하지 않았습니다!")


# 방어구 장착 함수
#   def equip_armor(self, armor):
#       if self.armor is None:
#            self.armor = armor
#            self.power += armor.power
#            self.magic_power += armor.magic_power
#            self.hp += armor.hp
#            self.mp += armor.mp
#            self.luck += armor.luck
#            print(f"{self.name}은 {self.armor.name}을 장착하였습니다")
#            self.show_status()
#       else:
#           answer = input(f"{self.name}은 {self.armor.name}을 장착 중입니다, 교체하시겠습니까? (Y/N)")
#           if answer.upper() =="Y":   <-upper()은 값을 모두 대문자로 받기위해 사용
#               self.armor = armor
#               self.power += armor.power
#               self.magic_power += armor.magic_power
#               self.hp += armor.hp
#               self.mp += armor.mp
#               self.luck += armor.luck
#               print(f"{self.name}은 {armor.name}을 장착하였습니다!")
#               self.show_status()
#           else:
#               print(f"{self.name}은 {armor.name}을 장착하지 않았습니다!")
# 포션 사용 함수
#   def use_potion(self, potion)
#       self.hp += potion.hp_recovery
#       self.mp += potion.mp_recovery


class wepon:
    pass
#   def __init__(self, name, hp, mp, power, magic_power, luck):
#       self.name = name
#       self.hp = hp
#       self.mp = mp
#       self.power = power
#       self.magic_power = magic_power
#       self.luck = luck
# 더 해줄 능력치 작성
# name, hp, mp, power, magic_power, luck

# 무기 정보 출력 함수
#   def show_item(self):
#       print(f"{self.name}  옵션 hp:{self.hp}  mp:{self.mp}  power:{self.power}  magic_power:{self.magic_power}  luck:{self.luck}")


class armor(wepon):
    pass
#   def __init__(self, name, hp, mp, power, magic_power, luck):
#       super().__init__(name, hp, mp, power, magic_power, luck)

#   def show_item(self):
#       super().show_item()
# wepon클래스와 구조가 같아 상속받아 사용

# 포션 관련 클래스


class potion:
    pass
#   def __init__(self, name, hp_recovery, mp_recovery):
#       self.name = name
#       self.hp_recovery = hp_recovery
#       self.mp_recovery = mp_recovery


# 사용 예시
hero = player('bob', 300, 300, 200, 200, 200)
sword = wepon('sword', 0, 0, 30, 10, 5)
plateArmor = armor('plateArmor', 30, 10, 10, 10, 10)
redpotion = potion('redpotion', (hero.max_hp-hero.hp), 0)
bluepotion = potion('bluepotion', 0, (hero.max_mp-hero.mp))

hero.equip_wepon(sword)
hero.equip_armor(plateArmor)
hero.use_potion(redpotion)

# 전사 무기
wood_clup = wepon('wood_clup', 10, 0, 30, 0, 0)
great_clup = wepon('great_clup', 20, 0, 50, 5, 0)
battle_axe = wepon('battle_axe', 20, 0, 50, 5, 0)
claymore = wepon('claymore', 30, 0, 50, 5, 0)
short_sword = wepon('short_sword', 10, 0, 10, 0, 0)
great_sword = wepon('great_sword', 30, 0, 60, 10, 0)
flashing_light_stick = wepon('flashing_light_stick', 50, 50, 100, 100, 30)
# 궁수 무기
short_bow = wepon('short_bow', 10, 10, 20, 5, 10)
long_bow = wepon('long_bow', 15, 5, 30, 10, 15)
composite_bow = wepon('composite_bow', 15, 10, 30, 15, 10)
oriental_bow = wepon('oriental_bow', 20, 20, 30, 30, 30)
is_this_a_real_bow = wepon('is_this_a_real_bow', 50, 50, 50, 50, 0)
fire_breathing_staff = wepon('fire_breathing_staff', 5, 5, 100, 0, 30)
# 마법사 무기
wand = wepon('wand', 5, 20, 5, 20, 10)
wood_staff = wepon('wood_staff', 5, 25, 5, 25, 10)
Grimoire_of_Eyes_in_a_Triangle = (
    'Grimoire_of_Eyes_in_a_Triangle', 3, 33, 3, 33, 3)
needlessly_large_rod = ('needlessly_large_rod', 5, 60, 0, 60, 0)
elder_wand = wepon('elder_wand', 20, 30, 5, 50, 0)
middle_eastern_magic_wand = wepon(
    'middle_eastern_magic_wand', 50, 50, 100, 100, 20)

# 방어구
cloth_armor: armor('cloth_armor', 15, 0, 0, 0, 0)
leather_armor = armor('leather_armor', 35, 0, 5, 0, 5)
chainmail = armor('chainmail', 45, 0, 10, 0, 5)
thornmail = armor('thornmail', 35, 0, 60, 60, 0)

hunter_hood = armor('hunter_hood', 10, 10, 5, 0, 0)
assassin_cloak = armor('assassin_cloak', 25, 5, 10, 0, 5)
claoak_of_agility = armor('claoak_of_agility', 20, 20, 15, 0, 0)
invisibility_cloak = armor('invisibility_cloak', 30, 30, 5, 5, 10)


old_robe = armor('old_robe', 5, 10, 0, 5, 0)
ash_cloak = armor('ash_cloak', 10, 20, 0, 20, 0)
apprentice_cloak = armor('Apprentice Cloak', 15, 15, 0, 10, 0)
cloak_the_you_shall_not_pass = armor(
    'cloak_the_you_shall_not_pass', 50, 50, 50, 50, 50)


# ///////////////////xxxxx
# stage = 15
# hero = player(name, hp, mp, ...)
# monster1 = Monster(name, hp, mp, ...)
# monster2 = Monster(name, hp, mp, ...)
# while stage <= 0:
#     print('전투를 시작합니다')
#     ...
