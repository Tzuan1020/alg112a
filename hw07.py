from micrograd.engine import Value

def gradient_descent_micrograd(f, initial_params, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
    params = [Value(p) for p in initial_params]

    for iteration in range(max_iterations):
        # 計算梯度
        gradient = grad_micrograd(f, params)

        # 更新參數
        for param, grad_value in zip(params, gradient):
            param -= learning_rate * grad_value

        # 計算目標函數的值
        current_value = f(params).data

        # 判斷是否收斂
        if np.linalg.norm([grad.data for grad in gradient]) < tolerance:
            print(f"Converged after {iteration + 1} iterations.")
            break

        # 打印當前的值和參數
        print(f"Iteration {iteration + 1}: f(p) = {current_value}, p = {[param.data for param in params]}")

    return [param.data for param in params]

def grad_micrograd(f, params):
    result = []

    # 計算梯度
    f_value = f(params)
    f_value.backward()

    for param in params:
        result.append(param.grad)

    return result

# 定義目標函數
def target_function(params):
    x, y, z = params
    return x**2 + y**2 + z**2

# 初始參數
initial_parameters = [1.0, 2.0, -3.0]

# 使用梯度下降法尋找谷底
result_params = gradient_descent_micrograd(target_function, initial_parameters)

print("Optimal parameters:", result_params)
print("Minimum value of the function:", target_function(result_params))

# 此作業是參考第六次作業修改而完成
