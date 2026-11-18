# %%
import numpy as np

# Dataset
rng = np.random.default_rng()
inputs = rng.uniform(-5, 5, 100)
noise = rng.normal(0, 0.5, 100)
outputs = 3 * inputs + 2 + noise

# %%
print(outputs)

# %%
weight = rng.random()
bias = rng.random()

# %%
def predictions(inputs, weight, bias):
    return weight * inputs + bias

# %%
print(predictions(inputs, weight, bias))

# %%
# MSE
def mse_calculation(predictions, outputs):
    error = predictions - outputs
    
    return np.mean(error**2)

# %%
print(mse_calculation(predictions(inputs, weight, bias), outputs))

# %%
# Derivatives
def derivative_weight(predictions, outputs, inputs):
    return np.mean(2 * (predictions - outputs) * inputs)

def derivative_bias(predictions, outputs):
    return np.mean(2 * (predictions - outputs))

# %%
print(derivative_weight(predictions(inputs, weight, bias), outputs, inputs))
print(derivative_bias(predictions(inputs, weight, bias), outputs))

# %%
# Update weight and bias
def gradient_descent(inputs, weight, bias, outputs, learning_rate, iteration):
    for i in range(1, iteration + 1):
        predict = predictions(inputs, weight, bias)
        loss = mse_calculation(predict, outputs)

        weight -= learning_rate * derivative_weight(predict, outputs, inputs)
        bias -= learning_rate * derivative_bias(predict, outputs)

        if (i % 100 == 0):
            print("Iteration = " + str(i))
            print("Weight = " + str(weight))
            print("Bias = " + str(bias))
            print("MSE = " + str(loss))

    return weight, bias

# %%
learning_rate = 0.01
iteration = 1000

weight, bias = gradient_descent(inputs, weight, bias, outputs, learning_rate, iteration)


