import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

data = pd.read_csv("xy_data.csv")

x_obs = data["x"].values
y_obs = data["y"].values

def curve(t, theta_deg, M, X):
    theta = np.deg2rad(theta_deg)
    x = (t * np.cos(theta)- np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta)+ X)
    y = (42+ t * np.sin(theta)+ np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta))
    return x, y

def residual(params):
    theta = params[0]
    M = params[1]
    X = params[2]
    t = params[3:]
    x_pred, y_pred = curve(t, theta, M, X)
    return np.concatenate([x_pred - x_obs, y_pred - y_obs])

theta0 = 25
M0 = 0.0
X0 = 50

t0 = np.linspace(6, 60, len(x_obs))
initial = np.concatenate(([theta0, M0, X0], t0))
lower = np.concatenate(([0, -0.05, 0], np.full(len(x_obs), 6)))
upper = np.concatenate(([50, 0.05, 100], np.full(len(x_obs), 60)))
result = least_squares(
    residual,
    initial,
    bounds=(lower, upper),
    verbose=1
)
theta, M, X = result.x[:3]
t_est = result.x[3:]

print("\nEstimated Parameters")
print(f"Theta = {theta:.6f} degrees")
print(f"M = {M:.6f}")
print(f"X = {X:.6f}")

x_fit, y_fit = curve(t_est, theta, M, X)

l1 = np.mean(np.abs(x_fit - x_obs) + np.abs(y_fit - y_obs))

print(f"Mean L1 Distance = {l1:.6f}")

plt.figure(figsize=(7, 7))
plt.scatter(x_obs, y_obs, s=8, label="Given Points")
plt.scatter(x_fit, y_fit, s=5, label="Predicted Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Inverse Parameter Estimation")
plt.legend()
plt.grid(True)
plt.savefig("output.png", dpi=300)
plt.show()
