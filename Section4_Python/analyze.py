import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("data.csv")
z_scores = stats.zscore(df[["temperature", "humidity"]])
filtered_df = df[(abs(z_scores) < 2).all(axis=1)]

plt.figure(figsize=(10, 5))
plt.plot(filtered_df["time"], filtered_df["temperature"], marker='o', label="Temperature (°C)")
plt.plot(filtered_df["time"], filtered_df["humidity"], marker='x', label="Humidity (%)")
plt.title("Filtered Sensor Readings")
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graph.png")

with open("report.txt", "w") as f:
    f.write("Sensor Data Report\n")
    f.write("==================\n\n")
    f.write(f"Total readings: {len(df)}\n")
    f.write(f"Valid readings after filtering: {len(filtered_df)}\n")
    f.write(f"Average temperature: {filtered_df['temperature'].mean():.2f} °C\n")
    f.write(f"Average humidity: {filtered_df['humidity'].mean():.2f} %\n")
