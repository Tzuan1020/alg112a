import numpy as np

def gradient_descent_numeric(f, initial_params, learning_rate=0.01, max_iterations=1000, tolerance=1e-6, step=1e-5):
    params = np.array(initial_params, dtype=float)

    for iteration in range(max_iterations):
        # 計算梯度
        gradient = numeric_gradient(f, params, step)

        # 更新參數
        params -= learning_rate * gradient

        # 計算目標函數的值
        current_value = f(params)

        # 判斷是否收斂
        if np.linalg.norm(gradient) < tolerance:
            print(f"Converged after {iteration + 1} iterations.")
            break

        # 打印當前的值和參數
        print(f"Iteration {iteration + 1}: f(p) = {current_value}, p = {params}")

    return params

def numeric_gradient(f, p, step=1e-5):
    gradient = np.zeros_like(p, dtype=float)

    for k in range(len(p)):
        gradient[k] = df(f, p, k, step)

    return gradient

# 函數 f 的偏微分 df/dp[k] 的數值近似
def df(f, p, k, step):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

# 定義目標函數
def target_function(params):
    x, y, z = params
    return x**2 + y**2 + z**2

# 初始參數
initial_parameters = [1.0, 2.0, -3.0]

# 使用梯度下降法尋找谷底
result_params = gradient_descent_numeric(target_function, initial_parameters)

print("Optimal parameters:", result_params)
print("Minimum value of the function:", target_function(result_params))

# 此作業是參考GPT給出的答案後，經理解所完成
