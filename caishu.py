import random

def guess_number():
    secret_num = random.randint(1, 100)
    while True:
        guess = int(input("请猜一个数字（1-100）："))
        if guess == secret_num:
            print("恭喜你，猜对了！")
            break
        elif guess < secret_num:
            print("猜小了，请重新猜一次。")
        else:
            print("猜大了，请重新猜一次。")

# 调用猜数游戏函数
guess_number()
