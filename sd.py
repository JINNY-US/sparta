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


f = open("img/fd.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()     # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
    time.sleep(0.06)
f.close()
time.sleep(1)


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


class Player:
    def __init__(self, name, hp, mp, power, normal_attack, magic_power, magic_attack):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.power = power
        self.normal_attack = normal_attack
        self.magic_power = magic_power
        self.magic_attack = magic_attack

    def attack(self):
        print("어떤 공격을 사용하시겠습니까?")
        print("1. 일반공격")
        print("2. 마법공격")

        while True:
            attack_type = input("숫자를 입력하세요: ")
            if attack_type == "1":
                return "normal"
            elif attack_type == "2":
                return "magic"
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")


clear()
loading_sound.stop()  # 로딩 배경음악 중지

sound = pygame.mixer.Sound("bgm/music.mp3")
sound.play(-1)  # -1 을 하면 무한 반복한다.(게임이 끝나면 꺼짐)

name = input("플레이어의 이름을 입력하세요: ")
hp = random.randint(50, 100)
mp = random.randint(20, 50)
power = random.randint(10, 20)
normal_attack = random.randint(1, 5)
magic_power = random.randint(5, 10)
magic_attack = random.randint(3, 10)

player = Player(name, hp, mp, power, normal_attack, magic_power, magic_attack)
