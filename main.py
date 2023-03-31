from tqdm import tqdm
import random
import time
import pygame
import os
import sys
import classes
import math


# 몬스터 정보 보여주기 함수
def view_monsters():
    print("\n몬스터 정보")
    for i, monster in enumerate(monster_list):
        print(f"{i+1}. ", end="")
        monster.update_status()
# 새페이지


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 다음 출력을 새페이지로 넘김


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# 오프닝 시작
# 플레이어 생성 배경음악
pygame.init()  # pygame을 진행할 때 꼭 초기화를 해줘야한다.

loading_sound = pygame.mixer.Sound("bgm/loding.mp3")
loading_sound.play()  # -1 을 하면 무한 반복한다.(게임이 끝나면 꺼짐)
loading_sound.set_volume(0.1)

f = open("img/moals.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()     # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
    time.sleep(0.06)
f.close()
time.sleep(0.5)
clear()

# 다음 출력을 새페이지로 넘김

f = open("img/fq.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
    line = line.strip()     # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
    time.sleep(0.06)
f.close()
time.sleep(0.5)
clear()
# 로딩창
print("Loading...")
time.sleep(1)
clear()

print("Configuring...")
time.sleep(0.5)
for g in tqdm(range(10)):
    time.sleep(0.1)
clear()
# 오프닝 끝

# @@@@@@@@@@@@@@@@@@플레이어@@@@@@@@@@@@@@@@@@
loading_sound.stop()  # 로딩 배경음악 중지

sound = pygame.mixer.Sound("bgm/music.mp3")  # 플레이어 생성 배경음악
sound.play(-1)  # -1 을 하면 무한 반복한다.(게임이 끝나면 꺼짐)
sound.set_volume(0.1)

# 플레이어 이름 생성
print("플레이어 이름 입력 :  ")
character_name = input(" ")

clear()
print(f"당신의 이름은 '{character_name}'입니다.")
time.sleep(0.5)

# 주사위를 굴리라는 안내멘트
print("스탯 주사위를 굴리려면 ENTER KEY를 눌러주세요.")
input()

while True:
    # 주사위 굴리기
    stat_str = random.randint(5, 10)
    stat_dex = random.randint(5, 10)
    stat_int = random.randint(5, 10)

    # 주사위 결과 출력
    print(f"힘 : {stat_str}  민첩 : {stat_dex}  지능 : {stat_int}")
    time.sleep(0.5)

    # 다시 굴리기 질문
    redice = input("다시 굴리시겠습니까? (Y/N) : ").upper()
    if redice == "Y":
        pass
    elif redice == "N":
        break
    else:
        print("잘못 눌렀으므로 다시 굴립니다.")
        pass


while True:
    print("\n직업을 선택해주세요.")
    print("1: 전사  2: 궁수  3: 마법사")
    select_character = input()
    if select_character == "1":
        you = classes.Warrior(f"{character_name}", 300,
                              200, stat_str, stat_dex, stat_int)
        skill_name = "파이참"
        skill_mp = 15
        weapon_list = classes.warrior_weapon_list
        armor_list = classes.warrior_armor_list
        break
    elif select_character == "2":
        you = classes.Archer(f"{character_name}", 300, 200,
                             stat_str, stat_dex, stat_int)
        skill_name = "폭탄화살"
        skill_mp = 15
        weapon_list = classes.archer_weapon_list
        armor_list = classes.archer_armor_list
        break
    elif select_character == "3":
        you = classes.Magician(f"{character_name}", 300,
                               200, stat_str, stat_dex, stat_int)
        skill_name = "py썬더"
        skill_mp = 30
        weapon_list = classes.magician_weapon_list
        armor_list = classes.magician_armor_list
        break
    else:
        print("잘못된 입력입니다.")

# @@@@@@@앞 스토리@@@@@@@@@@@@@@
print("어금니의 탑에 오신 걸 환영합니다!!")
time.sleep(3)
clear()

print("어금니 탑을 공략하기 앞서 간단한 설명 드리겠읍니다!!")
time.sleep(3)
clear()

print("1. 총 15층이 있고 1층씩 올라갈수록 몬스터들이 강해집니다!!")
time.sleep(3)
clear()

print("2. 몬스터를 잡으면 유용한 아이템, 포션을 드랍할 수 있습니다.")
time.sleep(3)
clear()

print("3. 다섯 층씩 올라갈 때마다 보스가 등장하며, 보스 바로 전 층에 레어 몬스터가 있습니다!!")
time.sleep(3)
clear()

print("그럼, 어금니 탑에 입장하겠습니다!!")
time.sleep(3)
clear()

sound.stop()
# 현재 층
pygame.mixer.init()

floor = 1

# 현재 재생 중인 BGM 파일 경로 초기화
current_bgm_file_path = ""

while floor <= 15:
    # 현재 층의 몬스터 리스트 가져오기
    monster_list = eval(f"classes.floor{floor}")

    # 층마다의 bgm 설정
    if floor in [5, 10, 15]:
        bgm_file_path = "bgm/boss_battle.mp3"
        bgm_volume = 0.5
    else:
        bgm_file_path = "bgm/monster.mp3"
        bgm_volume = 0.1

    # 이전 BGM 중지 및 새로운 BGM 재생
    if current_bgm_file_path != bgm_file_path:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(bgm_file_path)
        pygame.mixer.music.set_volume(bgm_volume)
        pygame.mixer.music.play(-1)
        current_bgm_file_path = bgm_file_path

    for monster in monster_list:
        monster.current_hp = monster.max_hp
        monster.alive = True

    clear()
    print(f"어금니의{floor}층에 입장했습니다. 이곳에서는 {len(monster_list)}마리의 몬스터와 전투합니다.")
    time.sleep(0.5)


    while True:
        # 플레이어 정보 보여주기
        print()
        you.update_status()

        # 몬스터 정보 보여주기
        view_monsters()
        
        
        action = None
        while True:
            # 공격방법 선택하기
            print(f"\n공격 방식을 고르세요.\n 1: 일반 공격 2: 스킬 공격({skill_name}) 3: 게임 종료")
            action = input()
            if action == "1":
                you.play_sound_effect("bgm/attack_normal.wav")
                you.attack_hit()
                break
            elif action == "2":
                you.play_sound_effect("bgm/attack_magic.wav")
                you.magic_hit()
                break
            elif action == "3":
                print("어금니 탑을 탈출합니다.")
                sys.exit()
            else:
                print("잘못 고르셨습니다. 다시 선택해 주세요.")

        while True:
            # 대상 몬스터 선택하기
            view_monsters()
            print("\n대상의 번호를 고르세요.")
            try:
                target_monster = int(input()) - 1
            except:
                print("잘못된 대상입니다. 다시 선택해주세요.")
                continue
            if not 0 <= target_monster <= len(monster_list)-1:
                print("잘못된 대상입니다. 다시 선택해주세요.")
            elif action == "1":
                clear()
                # 일반 공격
                you.normal_attack(monster_list[target_monster])
                break
            elif action == "2":
                # 마나 체크
                if you.current_mp < skill_mp:
                    clear()
                    print("마나가 부족합니다. 일반 공격으로 공격합니다.\n")
                    you.normal_attack(monster_list[target_monster])
                    break
                else:
                    clear()
                    # 스킬 공격
                    you.skill_attack(monster_list[target_monster])
                    break

        # 몬스터 사망 체크
        delete_monster_list = []
        for i, monster in enumerate(monster_list):
            if monster.alive == False:
                delete_monster_list.append(i)

                # 몬스터 사망시 경험치 획득
                you.current_exp += monster.exp
                print(f"{monster.name}을(를) 처치하여 {monster.exp}의 경험치를 얻었습니다.")

                # 몬스터 사망시 30% 확률로 포션 획득
                if random.random() < 0.4:
                    potion = random.choice(classes.potions)
                    print(f"보상으로 {potion.name}을 얻었습니다.")
                    potion.use(you)
                    you.update_status()
                # 몬스터 사망시 15% 확률로 무기 획득
                if random.random() < 0.2:
                    floor_level = math.ceil(floor/3) + 1
                    weapon_names = list(weapon_list.keys())
                    random_weapon = random.choice(weapon_names[:floor_level])
                    weapon = weapon_list[random_weapon]
                    print(f"{random_weapon}을 획득했습니다.")
                    weapon.show_item()
                    you.equip_weapon(weapon)

                # 몬스터 사망시 15% 확률로 방어구 획득
                if random.random() < 0.2:
                    floor_level = math.ceil(floor/5) + 1
                    armor_names = list(armor_list.keys())
                    random_armor = random.choice(armor_names[:floor_level])
                    armor = armor_list[random_armor]
                    print(f"{random_armor}을 획득했습니다.")
                    armor.show_item()
                    you.equip_armor(armor)

                # 레벨업
                if you.current_exp >= you.max_exp:
                    you.level += 1
                    you.current_exp = you.current_exp - you.max_exp
                    you.max_exp += 100
                    you.max_hp += round(you.max_hp*0.2)
                    you.current_hp = min(
                        round(you.current_hp + you.max_hp*0.5), you.max_hp)
                    you.max_mp += round(you.max_mp*0.2)
                    you.current_mp = min(
                        round(you.current_mp + you.max_mp*0.5), you.max_mp)
                    print(f"\n축하합니다! {you.level} 레벨이 되었습니다.")
                    you.update_status()

                    # 스탯 포인트 분배
                    stat_count = 3
                    while stat_count > 0:
                        print(
                            f"\n강화할 능력치를 선택해 주세요. (남은 스탯 포인트 : {stat_count})")
                        print("1: 힘, 2: 민첩성, 3: 지능")
                        stat_choice = input()
                        if stat_choice == "1":
                            you.strength += 1
                            stat_count -= 1
                            you.update_status()
                        elif stat_choice == "2":
                            you.dexterity += 1
                            stat_count -= 1
                            you.update_status()
                        elif stat_choice == "3":
                            you.intelligence += 1
                            stat_count -= 1
                            you.update_status()
                        else:
                            print("잘못 선택하셨습니다. 다시 선택해주세요.")
                break

        # 몬스터 사망 처리
        delete_monster_list.sort()
        for i in reversed(delete_monster_list):
            del monster_list[i]

        # 몬스터가 살아있는 경우 몬스터가 플레이어를 공격하기
        for monster in monster_list:
            monster.normal_attack(you)
            # 플레이어가 죽은 경우 게임 종료하기
            if not you.alive:
                print("당신은 죽었습니다. 게임 오버")
                sys.exit()

        # 다음 층 이동
        if len(monster_list) <= 0:
            time.sleep(0.5)
            print(f"\n{floor}층을 클리어하셨습니다!")
            floor += 1
            time.sleep(2)
            break
