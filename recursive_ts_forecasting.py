import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import pickle

# Function to create a recursive dataset for time series prediction
def create_recursive_data(data, window_size=5):
    i = 1
    while i < window_size:
        data[f"Temperature_{i}"] = data["Temperature"].shift(-i)
        i += 1
    data["target"] = data["Temperature"].shift(-i)
    data = data.dropna(axis=0)
    return data

# Load the temperature data from a CSV file
data = pd.read_csv("temperature.csv")

# Convert the "Time" column to datetime format
data["Time"] = pd.to_datetime(data["Time"])

# Interpolate missing temperature values
data["Temperature"] = data["Temperature"].interpolate()

# Create a recursive dataset for time series prediction with a window size of 5
data = create_recursive_data(data, window_size=5)

# Prepare input features (x) and target variable (y)
x = data.drop(["Time", "target"], axis=1)
y = data["target"]

# Split the data into training and testing sets
train_size = int(len(x) * 0.8)
x_train = x[:train_size]
y_train = y[:train_size]
x_test = x[train_size:]
y_test = y[train_size:]

# Initialize a linear regression model and train the linear regression model on the training data
reg = LinearRegression()
reg.fit(x_train, y_train)

# Make predictions on the testing data and calculate evaluation metrics
y_predict = reg.predict(x_test)
print(f"R2 score: {r2_score(y_test, y_predict)}")
print(f"Mean absolute error: {mean_absolute_error(y_test, y_predict)}")
print(f"Mean squared error: {mean_squared_error(y_test, y_predict)}")

# Save model
with open('model_recursive.pkl', 'wb') as model_file:
    pickle.dump(reg, model_file)

# Plot the actual temperature and predicted temperature over time
plt.plot(data["Time"][-500:], y_test.values[-500:], label="Actual")
plt.plot(data["Time"][-500:], y_predict[-500:], label="Predicted")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature vs Time Graph")
plt.legend()
plt.grid()
# plt.show()
plt.savefig("recursive_ts_forecasting.jpg")
