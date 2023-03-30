class Character:
    def __init__(self, name, hp, mp, level, strength, dexterity, intelligence):
        self.name = name
        self.max_hp = hp + self.level*50    # 레벨이 높으면 hp도 레벨에 비례해서 높아짐
        self.current_hp = self.max_hp
        self.max_mp = mp + self.level*30    # 레벨이 높으면 mp도 레벨에 비례해서 높아짐
        self.current_mp = self.max_mp
        self.normal_damage = self.strength*1.5 + self.dexterity + \
            self.intelligence*0.5  # 일반데미지는 힘3:민첩2:지능1 비율로 영향
        self.level = level
        self.max_exp = 50 + self.level*50  # 필요경험치량은 레벨에 비례
        self.current_exp = 0    # 처음 경험치는 0으로 시작해서 몬스터를 잡을때마다 올라야함 14층 클리어 기준 lv.13달성
        # 잉여경험치 = 현재경험치 - 최대경험치 / 현재 경험치 초기화 후에 +잉여경험치
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.alive = True

    def demage(self, target):
        self.max_hp -= self.nomal_damage
        if self.current_hp <= 0:
            self.alive = False

    def skill_attack(self, target):
        pass


class player(Character):

    def __init__(self, name, hp, mp, exp_gauge, level, strength, dexterity, intelligence):
        super().__init__(self, name, hp, mp, exp_gauge,
                         level, strength, dexterity, intelligence)
        self.wepon = None
        self.armor = None
#  아이템 장착 속성 생성

# 무기 장착 함수
    def equip_wepon(self, wepon):
        if self.wepon is None:
            self.wepon = wepon
            self.max_hp += wepon.hp
            self.max_mp += wepon.mp
            self.strength += wepon.strength
            self.dexterity += wepon.dexterity
            self.intelligence += wepon.intelligence
            print(f"{self.name}은 {self.wepon.name}을 장착하였습니다")
            self.update_status()
        else:
            answer = input(
                f"{self.name}은 {self.wepon.name}을 장착 중입니다, 교체하시겠습니까? (Y/N)")
            if answer.upper() == "Y":
                self.wepon = wepon
                self.max_hp += wepon.hp
                self.max_mp += wepon.mp
                self.strength += wepon.strength
                self.dexterity += wepon.dexterity
                self.intelligence += wepon.intelligence
                print(f"{self.name}은 {wepon.name}을 장착하였습니다!")
                self.update_status()
            else:
                print(f"{self.name}은 {wepon.name}을 장착하지 않았습니다!")

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
            else:
                print(f"{self.name}은 {armor.name}을 장착하지 않았습니다!")


# 포션 사용 함수


    def use_potion(self, potion):
        self.hp += potion.hp_recovery
        self.mp += potion.mp_recovery
        print(f"{self.name}이 {potion.name}을 사용했습니다!  hp:{self.current_hp}/{self.max_hp}  mp:{self.current_mp}/{self.max_mp}")


class wepon:
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


class armor(wepon):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        super().__init__(name, hp, mp, strength, dexterity, intelligence)

    def show_item(self):
        super().show_item()
# wepon클래스와 구조가 같아 상속받아 사용


# 포션 생성 클래스
class potion:
    def __init__(self, name, hp_recovery, mp_recovery):
        self.name = name
        self.hp_recovery = hp_recovery
        self.mp_recovery = mp_recovery


# 사용 예시 (이하 코드들은 능력치 변동 없을 때 값만 변경하기)
hero = player('bob', 300, 300, 200, 200, 200)
# 내 영역이 아니지?
sword = wepon('sword', 0, 0, 0, 0, 0)
# name, hp, mp, strength, dexterity, intelligence 순서
plateArmor = armor('plateArmor', 0, 0, 0, 0, 0)
# name, hp, mp, strength, dexterity, intelligence 순서
red_potion = potion('red_potion', (hero.max_hp-hero.current_hp), 0)
blue_potion = potion('blue_potion', 0, (hero.max_mp-hero.current_mp))
# 인스턴스 생성 -> 클래스지정 -> 속성값 부여

hero.equip_wepon(sword)
hero.equip_armor(plateArmor)
hero.use_potion(red_potion)
# 인스턴스 생성 -> 사용함수 -> 값
# 사용자지정 -> 행동지정 -> 사용아이템지정

# 스테이터스 틀 만들어지면 아이템 능력치 부여
# 전사 무기
# name, hp, mp, strength, dexterity, intelligence 순서
wood_clup = wepon('wood_clup', 10, 0, 5, 0, 0)
great_clup = wepon('great_clup', 30, 0, 5, 5, 0)
battle_axe = wepon('battle_axe', 30, 20, 10, 5, 0)
claymore = wepon('claymore', 30, 25, 20, 5, 0)
short_sword = wepon('short_sword', 10, 0, 5, 0, 0)
great_sword = wepon('great_sword', 30, 25, 20, 10, 0)
flashing_light_stick = wepon('flashing_light_stick', 50, 50, 40, 20, 30)
# 궁수 무기
# name, hp, mp, strength, dexterity, intelligence 순서
short_bow = wepon('short_bow', 10, 0, 5, 5, 0)
long_bow = wepon('long_bow', 10, 5, 5, 10, 15)
composite_bow = wepon('composite_bow', 15, 10, 5, 15, 10)
oriental_bow = wepon('oriental_bow', 15, 10, 10, 20, 5)
is_this_a_real_bow = wepon('is_this_a_real_bow', 30, 20, 15, 30, 0)
fire_breathing_staff = wepon('fire_breathing_staff', 50, 30, 30, 40, 30)
# 마법사 무기
# name, hp, mp, strength, dexterity, intelligence 순서
wand = wepon('wand', 5, 20, 0, 0, 10)
wood_staff = wepon('wood_staff', 5, 25, 0, 5, 10)
Grimoire_of_Eyes_in_a_Triangle = (
    'Grimoire_of_Eyes_in_a_Triangle', 3, 3, 3, 3, 33)
needlessly_large_rod = ('needlessly_large_rod', 20, 60, 0, 0, 20)
elder_wand = wepon('elder_wand', 20, 50, 5, 0, 30)
middle_eastern_magic_wand = wepon(
    'middle_eastern_magic_wand', 50, 50, 5, 5, 30)


# 데미지 공식 str *1.5 + dex + int *0.5  기본공격 = 데미지 *0.8 ~ 1.3(공통)
# 마법공격 전사: (데미지 + str *3) *1.3~2.0 <=궁수 같음(dex*3)
# 마법사 (데미지 + int *5)*1.3~2.0
# 전사 hp 300 mp 200 str 5~10 dex 5~10 int 5~10
# 궁수 hp 300 mp 200 str 5~10 dex 5~10 int 5~10
# 마법사 hp 300 mp 200 str 5~10 dex 5~10 int 5~10
#
# 전사 mp사용:20   15 30
# 기본공격 (5, 5, 5)12~19.5 (10, 10, 10)24~39
# 마법공격 (5,5,5) 39~60 (10,10,10) 78~120
#
# 궁수 mp사용:15
# 기본공격 (5, 5, 5)12~19.5 (10, 10, 10)24~39
# 마법공격 (5, 5, 5) 39~60 (10, 10, 10) 78~120

# 마법사 mp사용:30
# 기본공격 (5, 5, 5)12~19.5 (10, 10, 10)24~39
# 마법공격 (5, 5, 5) 52~80 (10, 10, 10) 104~160

# 초반 몬스터 데미지 8~26 hp 50~120 중보 데미지26 hp 111

# 방어구
# name, hp, mp, strength, dexterity, intelligence 순서
# 초반
cloth_armor: armor('cloth_armor', 20, 5, 5, 0, 0)
# 중반
leather_armor = armor('leather_armor', 35, 10, 5, 5, 0)
chainmail = armor('chainmail', 60, 20, 10, 10, 5)
# 이벤트
thornmail = armor('thornmail', 200, 50, 50, 10, 10)

# 초반
hunter_hood = armor('hunter_hood', 10, 10, 0, 5, 0)
# 중반
assassin_cloak = armor('assassin_cloak', 25, 10, 5, 10, 0)
claoak_of_agility = armor('claoak_of_agility', 50, 25, 10, 5, 0)
# 이벤트
invisibility_cloak = armor('invisibility_cloak', 200, 60, 45, 15, 10)

# 초반
old_robe = armor('old_robe', 5, 20, 0, 0, 5)
# 중반
ash_cloak = armor('ash_cloak', 15, 20, 0, 10, 10)
apprentice_cloak = armor('Apprentice Cloak', 30, 40, 0, 0, 20)
# 이벤트
cloak_the_you_shall_not_pass = armor(
    'cloak_the_you_shall_not_pass', 100, 100, 20, 20, 50)


# lv 1 100
# lv 2 200
# lv 3 300
# lv 4 400
# lv 5 500
# lv 6 600 ...

# m1   100  lv 2 exp 0/200
# m1 m2   230 lv 3 exp 30/300
# m1 m2 m3  365 lv4 exp 95/400
# m2 m3 sm1  405 lv 5 exp 100/500
# b1   170  lv 5 exp270/500
# ----
# m4  150 lv 5 exp 420/500
# m4 m5  300 lv 6 exp 220/600
# m4 m5 m6  460 lv 7 exp 80/700
# m5 m6 s2 500 lv 7 exp 580/700
# b2 200 lv 8 exp 80/800
# ---------
# m7  160 lv 8 exp 240/800
# m7 m8  345 lv 8 exp 585/800
# m7 m8 m9 535 lv 9 exp 220/900
# m8 m9 s3 625 lv 9 exp 845 /900
# b3 논외
# ``````````````
# 전사의 경우 9렙 기준 hp300 mp 200
# 궁수의 경우 9렙 기준 hp300 mp 200
# 마법사의 경우 9렙 기준 hp300 mp 200
