import random
import sys
# 캐릭터 클래스 스탯당 공격력추가 , 레벨업, 레벨업마다 스탯증가 구현 필요


class Character:
    def __init__(self, name, hp, mp, exp_gauge, nomal_attack, skill, level, strength, dexterity, intelligence):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.max_mp = mp
        self.current_mp = mp
        self.max_exp = exp_gauge
        self.current_exp = exp_gauge
        self.nomal_attack = nomal_attack
        self.skill = skill
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.alive = True

    def demage(self, target):
        self.max_hp -= self.nomal_attack
        if self.current_hp <= 0:
            self.alive = False

    def skill_attack(self, target):
        pass


# 베이스 몬스터 클레스
class Monster:
    def __init__(self, name, hp, mp, nomal_attack, skill, level, exp):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.max_mp = mp
        self.current_mp = mp
        self.nomal_attack = nomal_attack
        self.skill = skill
        self.alive = True
        self.level = level
        self.exp = exp

    def demage(self, target):
        self.max_hp -= self.nomal_attack
        if self.current_hp <= 0:
            self.alive = False


print("플레이어 이름 입력 :  ")
character_name = input(" ")
print("주사위를 굴려주세요 (1번을 눌러주세요)")
dice = input(" ")


print(f"당신은{character_name}이군요")
# 캐릭터 딕셔너리
character_dict = {"1": Character(f"name={character_name}", 300, 20, 0, 15, 25, 1, 5, 5, 5),
                  "2": Character(f"name={character_name}", 200, 50, 0, 30, 40, 1, 5, 5, 5),
                  "3": Character(f"name={character_name}", 150, 100, 0, 10, 50, 1, 5, 5, 5)}


# 일반 몬스터 딕셔너리
monster_dict = {"monster1": Monster("들짐승", 50, 0, 10, 0, 1, 20),
                "monster2": Monster("늑대인간", 100, 0, 15, 0, 3, 30),
                "monster3": Monster("고블린", 120, 0, 20, 0, 4, 35),
                "monster4": Monster("거대독거미", 200, 0, 40, 0, 6, 50),
                "monster5": Monster("빨간슬라임", 200, 0, 40, 0, 6, 50),
                "monster6": Monster("케로베로스", 250, 0, 50, 0, 7, 60),
                "monster7": Monster("오우거", 300, 0, 55, 0, 7, 60),
                "monster8": Monster("서큐버스", 440, 0, 70, 0, 8, 85),
                "monster9": Monster("드라큘라", 450, 0, 80, 0, 9, 90),
                }
# 엘리트 몬스터 딕셔너리
strong_monster_dict = {
    "strong_monster1": Monster("군필여고생", 111, 0, 20, 0, 4, 40),
    "strong_monster2": Monster("케로베로스", 333, 0, 50, 0, 10, 90),
    "strong_monster3": Monster("악마", 666, 0, 100, 0, 13, 150)
}
# 보스몬스터 딕셔너리
boss_monster_dict = {
    "boss_monster1": Monster("보스몬스터1", 150, 10, 20, 35, 7, 70),
    "boss_monster2": Monster("보스몬스터2", 300, 10, 35, 50, 10, 100),
    "boss_monster3": Monster("보스보스", 999, 20, 120, 150, 99, 999)
}


print("직업선택 ? ? 1: 전사  2: 궁수  3: 마법사  ")
select_character = str(input(" "))
if select_character == "1":
    character = character_dict["1"]
elif select_character == "2":
    character = character_dict["2"]
elif select_character == "3":
    character = character_dict["3"]
else:
    print("잘못된 입력입니다. 다시 선택해주세요")


# def generate_monsters(floor):
#     monsters_on_floor = []

#     if floor % 5 == 0:  # 보스 몬스터를 추가하는 층
#         boss_monster = boss_monster_dict[f"boss_monster{floor // 5}"]
#         monsters_on_floor.append(boss_monster)
#     else:
#         if floor % 4 == 0:  # 엘리트 몬스터를 추가하는 층
#             for i in range(floor - 3, floor - 1):  # floor - 3, floor - 2에 해당하는 몬스터를 추가
#                 if f"monster{i}" in monster_dict:
#                     monsters_on_floor.append(monster_dict[f"monster{i}"])
#             elite_monster = strong_monster_dict[f"strong_monster{floor // 4}"]
#             monsters_on_floor.append(elite_monster)
#         else:  # 일반 몬스터를 추가하는 층
#             start_monster = max(1, floor - 2)
#             end_monster = min(floor, 9)  # 일반 몬스터는 9번까지만 있습니다.
#             if floor == 6:
#                 start_monster = 4
#                 end_monster = 4
#             for i in range(start_monster, end_monster + 1):
#                 if f"monster{i}" in monster_dict:  # 몬스터 딕셔너리에 키가 있는지 확인
#                     monster = monster_dict[f"monster{i}"]
#                     monsters_on_floor.append(monster)

#     return monsters_on_floor


# # 각 층별 몬스터를 저장할 빈 딕셔너리를 생성
# floors = {}

# # 15층까지 각 층에 몬스터 배치
# for floor in range(1, 16):
#     floors[floor] = generate_monsters(floor)

# # 각 층의 몬스터를 출력하여 확인
# for floor, monsters in floors.items():
#     print(f"층: {floor}, 몬스터: {[monster.name for monster in monsters]}")
