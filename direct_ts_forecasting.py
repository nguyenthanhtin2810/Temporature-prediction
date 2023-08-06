import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import pickle

# Function to create a direct dataset for time series prediction
def create_direct_data(data, window_size=5, target_size=3):
    i = 1
    while i < window_size:
        data[f"Temperature_{i}"] = data["Temperature"].shift(-i)
        i += 1
    i = 0
    while i < target_size:
        data[f"target_{i}"] = data["Temperature"].shift(-i-window_size)
        i += 1
    data = data.dropna(axis=0)
    return data

# Load the temperature data from a CSV file
data = pd.read_csv("temperature.csv")

# Convert the "Time" column to datetime format
data["Time"] = pd.to_datetime(data["Time"])

# Interpolate missing temperature values
data["Temperature"] = data["Temperature"].interpolate()

# Create direct dataset for time series prediction with a window size of 5 and a target size of 3
window_size, target_size = 5, 3
data = create_direct_data(data, window_size, target_size)

# Prepare input features (x) and target variables (y)
x = data.drop(["Time"] + [f"target_{i}" for i in range(target_size)], axis=1)
y = data[[f"target_{i}" for i in range(target_size)]]

# Split the data into training and testing sets
train_size = int(len(x) * 0.8)
x_train = x[:train_size]
y_train = y[:train_size]
x_test = x[train_size:]
y_test = y[train_size:]

# Initialize a linear regression models and train the linear regression models on the training data
regs = [LinearRegression() for _ in range(target_size)]
for i, reg in enumerate(regs):
    reg.fit(x_train, y_train[f"target_{i}"])

# Make predictions on the testing data and calculate evaluation metrics
y_predict, r2, mae, mse = [], [], [], []
for i, reg in enumerate(regs):
    y_predict.append(reg.predict(x_test))
    r2.append(r2_score(y_test[f"target_{i}"], y_predict[i]))
    mae.append(mean_absolute_error(y_test[f"target_{i}"], y_predict[i]))
    mse.append(mean_squared_error(y_test[f"target_{i}"], y_predict[i]))
print(f"R2 score: {r2}")
print(f"Mean absoluate error: {mae}")
print(f"Mean squared error: {mse}")

# Save models
with open('model_direct.pkl', 'wb') as model_file:
    pickle.dump(regs, model_file)

# Plot the actual temperature and predicted temperature over time
a, b, s = 1, 1, 1
while s != target_size:
    s += 1
    if s > a * b:
        if a <= b:
            a += 1
        else:
            b += 1

plt.figure(figsize=(a*4, b*4))
for i in range(target_size):
    plt.subplot(b, a, i + 1)
    plt.plot(data["Time"][-200:], y_test[i].values[-200:], label="Actual")
    plt.plot(data["Time"][-200:], y_predict[i][-200:], label=f"Predicted_{i}")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.title(f"Model_{i}")
    plt.legend()
    plt.grid()
plt.tight_layout()
# plt.show()
plt.savefig("direct_ts_forecasting.jpg")
