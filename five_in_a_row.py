import random

# 创建一个15x15的棋盘
board_size = 15
board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

# 打印当前棋盘状态
def print_board():
    for row in board:
        print(' '.join(row))
    print()

# 判断是否有玩家获胜
def check_winner(row, col, player):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 横、竖、斜、反斜方向
    for dr, dc in directions:
        count = 1
        r, c = row, col
        while count < 5:
            r += dr
            c += dc
            if r < 0 or r >= board_size or c < 0 or c >= board_size:
                break
            if board[r][c] == player:
                count += 1
            else:
                break
        r, c = row, col
        while count < 5:
            r -= dr
            c -= dc
            if r < 0 or r >= board_size or c < 0 or c >= board_size:
                break
            if board[r][c] == player:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

# 检查在指定位置下棋是否能够阻止玩家获胜
def check_block(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count_player = 0
        count_empty = 0
        r, c = row, col
        for _ in range(4):
            r += dr
            c += dc
            if r < 0 or r >= board_size or c < 0 or c >= board_size:
                break
            if board[r][c] == 'X':
                count_player += 1
            elif board[r][c] == ' ':
                count_empty += 1
        if count_player == 3 and count_empty == 1:
            for _ in range(4):
                row -= dr
                col -= dc
                if board[row][col] == ' ':
                    return row, col

    return None

# 电脑下棋
def computer_move(player):
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == ' ':
                # 检查电脑是否能赢
                board[row][col] = player
                if check_winner(row, col, player):
                    return row, col
                board[row][col] = ' '
                
                # 检查是否需要阻止玩家获胜
                block_move = check_block(row, col)
                if block_move:
                    return block_move

    while True:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if board[row][col] == ' ':
            board[row][col] = player
            return row, col

# 判断是否平局
def check_draw():
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == ' ':
                return False
    return True

# 主游戏循环
def main():
    print("Welcome to 5-in-a-Row Game!")
    
    while True:
        print_board()
        
        # 玩家下棋
        player_row = int(input("Enter row (0-14): "))
        player_col = int(input("Enter column (0-14): "))
        if board[player_row][player_col] != ' ':
            print("This cell is already occupied. Try again.")
            continue
        board[player_row][player_col] = 'X'
        
        # 判断玩家是否获胜
        if check_winner(player_row, player_col, 'X'):
            print_board()
            print("Congratulations! You win!")
            break
        
        # 判断是否平局
        if check_draw():
            print_board()
            print("It's a draw! Game over.")
            break
        
        # 电脑下棋
        computer_row, computer_col = computer_move('O')
        print(f"Computer's move: row {computer_row}, column {computer_col}")
        
        # 判断电脑是否获胜
        if check_winner(computer_row, computer_col, 'O'):
            print_board()
            print("Computer wins! Game over.")
            break

if __name__ == "__main__":
    main()
