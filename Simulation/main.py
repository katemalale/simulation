import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load Excel file
df = pd.read_excel("rtso_data.xlsx")

# Calculate Spectrum Efficiency
df['Spectrum_Efficiency'] = df['Data_Rate_bps'] / df['Bandwidth_Hz']

# Simple AI prediction (simulate)
df['Predicted_Spectrum_Efficiency'] = df['Spectrum_Efficiency'] * 0.95

# Interference score
df['Interference_Score'] = df['Interference_Power_dBm'] / (df['Signal_Power_dBm'] + 1)

# First plot
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Spectrum_Efficiency'], label='Actual', color='green')
plt.plot(df['Time'], df['Predicted_Spectrum_Efficiency'], label='Predicted', color='blue', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Spectrum Efficiency (bps/Hz)')
plt.title('Spectrum Efficiency Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("spectrum_efficiency.png")  # Optional: saves the plot as a file
plt.show()

# Second plot
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Interference_Score'], label='Interference Score', color='red')
plt.xlabel('Time')
plt.ylabel('Interference Score')
plt.title('Interference Score Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("interference_score.png")  # Optional: saves the plot
plt.show()
