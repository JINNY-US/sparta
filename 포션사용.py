# 랜덤 모듈 임포트
import random
import sys
import os

# 플래이어 틀


class Player:
    def __init__(self, name, alive):
        self.name = name
        self.hp = 100
        self.alive = alive
        self.power = random.randrange(15, 20)
        self.magic = random.randrange(30, 80)
        self.mp = 1
        self.portion_use = 30
        self.portion = 1


# 플레이어 데미지

    def damage(self, power):
        self.hp -= power
        if self.hp <= 0:
            self.alive = False

           # 포션 사용
    def healing(self, portion_use):
        self.hp += portion_use

        # 필살기 mp소모
    def use_magic(self):
        if self.mp <= 0:
            print("남은 MP가 없습니다 다음 행동을 할 수 없습니다.")
            return 0
        else:
            self.mp -= 1
            return self.magic

        # 포션소모
    def use_Portion(self):
        if self.portion <= 0:
            print("남은 포션이 없습니다.")
            return 0
        else:
            self.portion -= 1
            return self.portion_use

       # 캐릭터 상태

    def update_status(self):
        print(f"{self.name}의 현재 상태: HP {self.hp}, MP {self.mp}, 포션{self.portion}")

        # 몬스터 클레스


class monster():
    def __init__(self, name, hp, power, alive):
        self.name = name
        self.hp = hp
        self.power = power
        self.alive = alive

        # 몬스터 데미지
    def damage(self, power):
        self.hp -= power
        if self.hp <= 0:
            self.alive = False

            # 몬스터 상태
    def update_status(self):
        print(f"몬스터의 현재 상태: HP {self.hp}")


        # 플레이어 이름 인풋으로 받기 , 인스턴스 생성
player_name = input("캐릭터의 이름은?: ")
player = Player(player_name, True)

# 각 숫자에 다른 몬스터 생성하기 , 몬스터 선택하기
print("세갈래 길에 도착했습니다 어떤 길로 가시겠습니까 1.오른쪽 2.왼쪽 3.중앙:  ")
select_num = int(input(" "))

if select_num == 1:
    monster = monster('dog', 100, random.randint(10, 20), True)
    print("개 몬스터가 튀어나왔다")
elif select_num == 2:
    monster = monster('cat', 120, random.randint(15, 25), True)
    print("고양이 몬스터가 튀어나왔다")
elif select_num == 3:
    monster = monster('boss', 150, 30, True)
    print("보스 몬스터가 튀어나왔다")
else:
    print("잘못된 입력입니다.")


# 공격 방법 입력받기 / 행동 선택
def get_attack_type():
    while True:
        attack_type = input(
            "어떤 공격을 하시겠습니까? (일반공격 :'1', 필살기(1회사용) :'2' 포션사용 :'3' ) ")
        if attack_type == "1" or attack_type == "2" or attack_type == "3":
            return attack_type
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


# 반복문을 돌려 몬스터와 배틀하기 while 문으로 hp가 떨어져 alive의 값이 False 로 바뀔때까지 돌기
while player.alive and monster.alive:

   # 플레이어 , 몬스터의 상태를 불러와서 현재상태 보여주기
    print("=" * 30)
    player.update_status()
    monster.update_status()

    attack_type = get_attack_type()
    # 1번을 입력했을때
    if attack_type == "1":
        attack_power = player.power
        print(f"{player.name}가 {player.power}의 피해를 입혔습니다.")
        monster.damage(attack_power)
        # 2번을 압력했을때 (필살기 사용시)
    elif attack_type == "2":
        magic = player.use_magic()
        print(f"{player.name}가 필살기를 사용!! 몬스터가 {magic}의 피해를 입었습니다.")
        monster.damage(magic)
        # 포션을 사용했을때
    else:
        portion = player.use_Portion()
        print(f"{player.name}가 포션을 사용 {player.name}이(가) {portion}만큼 회복했습니다.")
        player.healing(portion)

    # 몬스터의 공격 (attack_type 선택 후에 몬스터가 살아있을때)
    if monster.alive:
        print(f"몬스터가 {player.name}에게 {monster.power}의 피해를 입혔습니다.")
        player.damage(monster.power)

     # 몬스터 or 플레이어의 hp가 없을때 플레이어의 alive 값만 참일때 if 그게 아닐때 else
if player.alive:
    print("승리 ! 중요한건 꺽이지 않는 마음")
else:
    print("패배 ! 중요한건 꺽여도 그냥하는 마음")
