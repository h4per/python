
import random
from decouple import config

def play_game():
    my_money = int(config("MY_MONEY"))
    nums = list(range(1, 31))

    while True:
        print(f"Ваши деньги: {my_money}")
        bet = int(input("Поставьте деньги: "))
        if bet > my_money:
            print(f"Извините у вас не хватает средств на ставку. Попробуйте еще раз\n")
            continue

        win_number = random.choice(nums)
        select_number = int(input("Выбирайте номера с 1 по 30: "))

        if select_number > 30:
            print(f"Э брат больше 30 чисел нет. Заново давай\n")
            continue

        elif bet > my_money:
            print("Извините у вас не хватает средств на ставку. Попробуйте еще раз")
            continue

        elif select_number == win_number:
            my_money += bet * 2
            print(f"Поздравляю!Вы выиграли!")
        else:
            my_money -= bet
            print(f"Вы проиграли. У вас осталось {my_money}")

        choice = input("Хотите ли еще раз поиграть? (да/нет): \n")
        if choice != "да":
            break
        print(f"Игра продолжается. Ваш баланс {my_money}\n")
        
play_game()