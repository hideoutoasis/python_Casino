from random import randint

print('\n업다운 게임에 오신 것을 환영합니다.\n')


def pythonCasino():
    minimum_number = 1
    maximum_number = 100
    pc_choice = randint(minimum_number, maximum_number)
    count = 0

    print(f'{minimum_number}부터 {maximum_number} 사이의 숫자를 입력해 정답을 맞춰 보세요.')

    while True:
        user_choice = int(input('숫자를 입력해 주세요:'))
        count += 1

        if minimum_number <= user_choice <= maximum_number:

            if user_choice == pc_choice:
                print(f'정답입니다! {count}번 시도하셨습니다.')
                while True:
                    replay = input('게임을 다시 시작하시겠습니까? (y/n): ')

                    if replay == 'y':
                        print(f'이전 게임의 시도횟수는 {count}번입니다.')
                        pythonCasino()

                    elif replay == 'n':
                        print("게임을 종료합니다. thank you for playing my game!")
                        break

                    else:
                        print('y 또는 n으로 답해주세요.')
                break

            elif user_choice > pc_choice:
                print(f'{user_choice}보다 작습니다. 다시 입력해보세요.')

            elif user_choice < pc_choice:
                print(f'{user_choice}보다 큽니다. 다시 입력해보세요.')

        elif user_choice <= minimum_number or user_choice >= maximum_number:
            print('제시된 범위 안에서 숫자를 골라 입력해주세요.')


pythonCasino()
