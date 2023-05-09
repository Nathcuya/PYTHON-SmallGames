import random


def generate_numbers():
    """生成4个1~9的整数"""
    return [random.randint(1, 9) for _ in range(4)]


def calculate_24(numbers):
    """计算是否能得出24"""
    if len(numbers) == 1:
        return abs(numbers[0] - 24) < 1e-6
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            a, b = numbers[i], numbers[j]
            rest_numbers = [
                numbers[k] for k in range(len(numbers)) if k != i and k != j
            ]
            if (
                
                calculate_24([a + b] + rest_numbers)
                or calculate_24([a - b] + rest_numbers)
                or calculate_24([b - a] + rest_numbers)
                or calculate_24([a * b] + rest_numbers)
            ):
                return True
            if b != 0 and a % b == 0 and calculate_24([a // b] + rest_numbers):
                return True
            if a != 0 and b % a == 0 and calculate_24([b // a] + rest_numbers):
                return True
    return False


if __name__ == "__main__":
    while True:
        numbers = generate_numbers()
        print("请使用以下4个数字，通过加减乘除得出24：", numbers)
        user_input = input()
        if user_input == "exit":
            break
        if calculate_24(numbers):
            print("恭喜你，你赢了！")
        else:
            print("很遗憾，你输了。")
