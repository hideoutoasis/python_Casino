import random
import time

print('가위바위보 게임에 오신 것을 환영합니다.\n')


def rspGame():
    rsp = ['가위', '바위', '보']

    user_win = 0
    computer_win = 0
    draw = 0
    flag = 0

    print('가위 바위 보 중 하나를 정하여 내고 컴퓨터를 이겨보세요.\n준비되셨나요? 시작합니다.')

    while True:
        user_choice = input('가위 바위 보:')

        computer_choice = random.choice(rsp)

        if user_choice not in rsp:
            print('가위, 바위, 보 중 선택하여 한글로 입력해주세요.')
            continue

        elif user_choice == computer_choice:
            print('가위...')
            time.sleep(1)
            print('바위...')
            time.sleep(1)
            print('보!!')
            time.sleep(1)
            print(f'당신:{user_choice}, 컴퓨터:{computer_choice}.\n비겼습니다.')
            draw += 1

        elif (user_choice == '가위' and computer_choice == '보') or (user_choice == '바위' and computer_choice == '가위') or (user_choice == '보' and computer_choice == '바위'):
            print('가위...')
            time.sleep(1)
            print('바위...')
            time.sleep(1)
            print('보!!')
            time.sleep(1)
            print(f'당신:{user_choice}, 컴퓨터:{computer_choice}. \n이겼습니다!')
            user_win += 1

        else:
            print('가위...')
            time.sleep(1)
            print('바위...')
            time.sleep(1)
            print('보!!')
            time.sleep(1)
            print(f'당신:{user_choice}, 컴퓨터:{computer_choice}. \n졌습니다.')
            computer_win += 1

        while True:
            replay = input('\n다시 하시겠습니까? ( ㅇ, y / ㄴ, n ): ').lower()

            if replay == 'y' or replay == 'ㅇ':
                print(f'승: {user_win} / 패: {computer_win} / 무: {draw}')
                break

            elif replay == 'n' or replay == 'ㄴ':
                print(f'승: {user_win} / 패: {computer_win} / 무: {draw}')
                print("게임을 종료합니다. thank you for playing my game!")
                flag = 1
                break

            else:
                print('ㅇ, y 또는 ㄴ, n으로 답해주세요.')
                continue

        if flag == 1:
            break


rspGame()
