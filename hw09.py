def matrix_print(matrix):
    """印出矩陣"""
    for row in matrix:
        print(row)

def find_path(matrix, start_x, start_y):
    def dfs(x, y):
        nonlocal matrix

        print("=========================")
        print(f"x={x} y={y}")
        matrix_print(matrix)

        # 遞迴終止條件
        if x >= 6 or y >= 8:
            return False
        if matrix[x][y] == '*' or matrix[x][y] == '+':
            return False

        # 將當前位置設為 '.' 表示已經走過
        if matrix[x][y] == ' ':
            matrix[x] = matrix[x][:y] + '.' + matrix[x][y + 1:]

        # 如果當前位置是終點，返回成功
        if matrix[x][y] == '.' and (x == 5 or y == 7):
            return True

        # 定義四個可能的移動方向：右、下、左、上
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # 嘗試往四個方向移動
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 6 and 0 <= new_y < 8 and matrix[new_x][new_y] == ' ':
                # 如果在新位置找到路徑，返回成功
                if dfs(new_x, new_y):
                    return True

        # 如果在所有方向都沒有找到路徑，標記當前位置為 '+'，返回失敗
        matrix[x] = matrix[x][:y] + '+' + matrix[x][y + 1:]
        return False

    # 啟動深度優先搜索
    return dfs(start_x, start_y)

# 迷宮矩陣
maze = [
    "********",
    "** * ***",
    "     ***",
    "* ******",
    "*     **",
    "***** **"
]

# 從起點 (2, 0) 開始尋找路徑
find_path(maze, 2, 0)

print("=========================")
matrix_print(maze)
# 此份作業是藉由老師的範例和GPT嘗試理解後所完成
