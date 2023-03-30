import random


class Character:
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        self.name = name
        self.max_hp = hp
        self.current_hp = self.max_hp
        self.max_mp = mp
        self.current_mp = self.max_mp
        self.normal_damage = self.strength*1.5 + self.dexterity + \
            self.intelligence*0.5  # 일반데미지는 힘3:민첩2:지능1 비율로 영향
        self.level = 1
        self.max_exp = 100  # 필요경험치량은 레벨에 비례
        self.current_exp = 0    # 처음 경험치는 0으로 시작해서 몬스터를 잡을때마다 올라야함 14층 클리어 기준 lv.13달성
        # 잉여경험치 = 현재경험치 - 최대경험치 / 현재 경험치 초기화 후에 +잉여경험치
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.alive = True

    def normal_attack(self, target):
        attack_damage = random.randint(
            int(self.normal_damage*0.8), int(self.normal_damage*1.3))
        print(f"{self.name}의 별로 안아픈 공격 ! ")
        target.current_hp -= attack_damage
        print(f"{target.name}에게 {attack_damage}의 피해를 입혔다 ! ")
        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌다 !")
            self.alive = False
            target.alive = False

       # 캐릭터 상태
    def update_status(self):
        print(f"{self.name}의 현재 상태: HP {self.current_hp} / {self.max_hp}, MP {self.current_mp} / {self.max_mp}, 경험치:{self.current_exp} / {self.max_exp} 레벨 :{self.level} lv")


# 전사 클래스
class Warrior(Character):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        super().__init__(name, hp, mp, strength, dexterity, intelligence)
        self.max_hp = self.max_hp*2
        self.current_hp = self.current_hp*2  # 전사 클래스는 체력 2배 / 마력 0.5배
        self.max_mp = self.max_mp*0.5
        self.current_mp = self.current_mp*0.5
        self.skill_damage = self.normal_damage + \
            self.strength*3  # 스킬데미지는 일반데미지 + 직업 특화스탯에 영향을 받음
        self.warrior_skill_name = "파이참"

    def Warrior_skill(self, target):
        self.current_mp -= 20
        if self.current_mp - 20 < 0:
            print("마나가 부족합니다")
            return
        skill_damage = random.randint(
            int(self.skill_damage*1.3), int((self.skill_damage*2.0)))
        # 스킬을 쓸때마다 스킬 데미지가 힘에 비례해서 증가
        skill_damage += int(self.strength * 0.5)
        target.current_hp -= skill_damage
        print(f"{self.name}의 {self.warrior_skill_name}! ")
        print(f"{target.name}에게 {skill_damage}의 피해를 입혔다 ! ")
        if target.current_hp <= 0:
            print(f"{target.name}이 쓰러졌다 !")
            self.alive = False


# 궁수 클래스
class Archer(Character):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        super().__init__(name, hp, mp, strength, dexterity, intelligence)
        self.max_hp = self.max_hp*1.5   # 궁수 클래스는 체력 1.5배 / 마력 1배
        self.current_hp = self.current_hp*1.5
        self.skill_damage = self.normal_damage + \
            self.dexterity*3  # 스킬데미지는 일반데미지 + 직업 특화스탯에 영향을 받음
        self.archer_skill_name = "폭탄화살"

    def Archer_skill(self, target):
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
            self.alive = False


# 마법사 클래스
class Magician(Character):
    def __init__(self, name, hp, mp, strength, dexterity, intelligence):
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        super().__init__(name, hp, mp, strength, dexterity, intelligence)
        self.max_mp = self.max_mp*2  # 마법사 클래스는 체력 1배 / 마력 2배
        self.current_mp = self.current_mp*2
        self.skill_damage = self.normal_damage + \
            self.intelligence*5  # 스킬데미지는 일반데미지 + 직업 특화스탯에 영향을 받음
        self.magician_skill_name = "py썬더"

    def Archer_skill(self, target):
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
            self.alive = False


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
            self.alive = False

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
