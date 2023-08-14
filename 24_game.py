import random


def evaluate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return None


def main():
    print("Welcome to 24-Point Challenge!")

    while True:
        # 随机生成四个数字
        numbers = [random.randint(1, 9) for _ in range(4)]
        print("Numbers:", numbers)

        expression = input("Enter your expression (use + - * /): ")

        result = evaluate(expression)
        if result is not None and result == 24:
            print("Congratulations! Your answer is correct!")
        else:
            print("Sorry, your answer is incorrect.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
