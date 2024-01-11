import numpy as np

def evaluate_polynomial(coefficients, x):
    """
    求解 n 次多項式在給定 x 的值

    參數:
    coefficients (list): 多項式的係數，從高次到低次排列
    x (float): 在多項式中要代入的 x 值

    返回值:
    float: 多項式在 x 值處的計算結果
    """
    # 將係數轉換成 NumPy 多項式對象
    poly = np.poly1d(coefficients)

    # 計算多項式在 x 值處的值
    result = poly(x)

    return result

# 測試例子
# 多項式：3x^3 + 2x^2 - x + 5
coefficients = [3, 2, -1, 5]
x_value = 2.5

# 計算多項式在 x = 2.5 的值
result = evaluate_polynomial(coefficients, x_value)

# 輸出結果
print(f"The result of the polynomial at x = {x_value} is: {result}")
# 此作業是藉由GPT輔助所完成
