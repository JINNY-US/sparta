# ~~~~~~~~플레이어 생성~~~~~~~~ #
from tqdm import tqdm
import random
import time
import pygame
import os

# 플레이어 생성 배경음악
pygame.init()  # pygame을 진행할 때 꼭 초기화를 해줘야한다.

loading_sound = pygame.mixer.Sound("bgm/loding.mp3")
loading_sound.play()  # -1 을 하면 무한 반복한다.(게임이 끝나면 꺼짐)
loading_sound.set_volume(0.1)

f = open("img/fd.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()     # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
    time.sleep(0.06)
f.close()
time.sleep(1)

# 다음 출력을 새페이지로 넘김


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print("Loading...")
time.sleep(3)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()
print("Configuring...")
time.sleep(3)
for g in tqdm(range(100)):
    time.sleep(0.1)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Player:
    def __init__(self, name, hp, mp, power, attack_normal, magic_power, attack_magic):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.power = power
        self.attack_nomal = pygame.mixer.Sound("bgm/attack_normal.wav")
        self.magic_power = magic_power
        self.attack_magic = pygame.mixer.Sound("bgm/attack_magic.wav")

    def attack(self):
        print("어떤 공격을 사용하시겠습니까?")
        print("1. 일반공격")
        print("2. 마법공격")

        while True:
            attack_type = input("숫자를 입력하세요: ")
            if attack_type == "1":
                self.attack_nomal.play()
                return "normal"
            elif attack_type == "2":
                self.attack_magic.play()
                return "magic"
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")


clear()
loading_sound.stop()  # 로딩 배경음악 중지

sound = pygame.mixer.Sound("bgm/music.mp3")
sound.play(-1)  # -1 을 하면 무한 반복한다.(게임이 끝나면 꺼짐)
sound.set_volume(0.1)


# 글자 색상 red + ""+reset 하면 글자 색이 입혀진다
# @@@@@@@@@@@@@@@@@색상코드@@@@@@@@@@@@@@@@@@
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
magenta = "\033[95m"
blue = "\033[34m"
reset = "\033[0m"
# 리셋을 안해주면 다음 글자가 색상을 정한 부분처럼된다.


name = input(red+"플레이어의 이름을 입력하세요:"+reset)
hp = random.randint(50, 100)
mp = random.randint(20, 50)
power = random.randint(10, 20)
attack_normal = random.randint(1, 5)
magic_power = random.randint(5, 10)
attack_magic = random.randint(3, 10)

player = Player(name, hp, mp, power, attack_normal,
                magic_power, attack_magic)

# 생성된 플레이어 객체의 정보 출력
print(f"플레이어 이름: {player.name}")
print(f"체력: {player.hp}")
print(f"마력: {player.mp}")
print(f"파워: {player.power}")
print(f"기본공격: {player.attack_nomal}")
print(f"마법파워: {player.magic_power}")
print(f"마법공격: {player.attack_magic}")

# @@@@@@@@@@@Monster calss@@@@@@@@@@@


class Monster:
    def __init__(self, name, hp, monster_hit):
        self.name = name
        self.hp = hp
        self.monster_hit = monster_hit

    def normal_attack(self):
        # 몬스터가 일반공격을 할 때 효과음을 재생합니다.
        pygame.mixer.Sound("bgm/monster_hit.wav").play()
        # 여기서 일반공격의 로직을 구현합니다.
        # ...


# 몬스터 생성
name = "이세계_슬라임"
hp = random.randint(500, 1000)
monster_hit = random.randint(1, 3)


monster = Monster(name, hp, monster_hit)

# 생성된 몬스터 정보
print(f"몬스터 이름: {monster.name}")
print(f"체력: {monster.hp}")
print(f"일반공격: {monster.monster_hit}")


def battle(player, monster):
    print("전투가 시작됩니다!")
    print(f"{player.name}: HP {player.hp}, MP {player.mp}")
    print(f"{monster.name}: HP {monster.hp}")

    while player.hp > 0 and monster.hp > 0:
        # 플레이어의 공격
        attack_type = player.attack()
        if attack_type == "normal":
            damage = random.randint(player.power - 2, player.power + 2)
            monster.hp = max(monster.hp - damage, 0)
            print(f"{player.name}의 일반공격! {monster.name}에게 {damage}의 데미지를 입혔습니다.")
        else:
            if player.mp < 5:
                print("마나가 부족합니다. 일반공격을 사용하세요.")
                continue
            damage = random.randint(
                player.magic_power - 4, player.magic_power + 4)
            player.mp -= 5
            monster.hp = max(monster.hp - damage, 0)
            print(f"{player.name}의 마법공격! {monster.name}에게 {damage}의 데미지를 입혔습니다.")

        if monster.hp == 0:
            print(f"{monster.name}이(가) 쓰러졌습니다.")
            print(f"{player.name}의 승리!")
            break

        # 몬스터의 공격

        damage = random.randint(monster_hit - 2,
                                monster_hit + 2)
        player.hp = max(player.hp - damage, 0)
        print(f"{monster.name}의 공격! {player.name}에게 {damage}의 데미지를 입혔습니다.")

        if player.hp == 0:
            print(f"{player.name}이(가) 쓰러졌습니다.")
            print(f"{player.name}의 패배!")
            break

        # 상태 출력
        print(f"{player.name}: HP {player.hp}, MP {player.mp}")
        print(f"{monster.name}: HP {monster.hp}")


battle(player, monster)
