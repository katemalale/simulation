import random

# Dummy spectrum data (simulating rows from a dataset)
spectrum_data = [
    {
        "bandwidth": 10e6,  # 10 MHz
        "data_rate": 50e6,  # 50 Mbps
        "signal_power": 5,   # dBm
        "interference_power": 1,  # dBm
        "noise_power": 0.5,  # dBm
        "request_time": 0.001,
        "decision_time": 0.002,
        "e2e_delay": 0.1
    },
    {
        "bandwidth": 20e6,
        "data_rate": 100e6,
        "signal_power": 10,
        "interference_power": 3,
        "noise_power": 0.7,
        "request_time": 0.003,
        "decision_time": 0.004,
        "e2e_delay": 0.15
    }
]

# Dummy AI model: randomly choose one of 3 available frequency bands
def select_band():
    return random.choice(["Band A", "Band B", "Band C"])

# Metrics
def calculate_spectrum_efficiency(bandwidth, data_rate):
    return data_rate / bandwidth  # bits/sec/Hz

def calculate_interference_mitigation(signal, interference, noise):
    return signal / (interference + noise)  # Simplified SINR

def calculate_latency(req_time, dec_time, e2e):
    return (dec_time - req_time) + e2e

def calculate_throughput(data_rate, time_period=1):
    return data_rate / time_period

# Run simulation
print("\n🔧 Running RTSO Simulation...\n")
for i, row in enumerate(spectrum_data):
    print(f"--- Scenario {i + 1} ---")

    chosen_band = select_band()
    se = calculate_spectrum_efficiency(row['bandwidth'], row['data_rate'])
    ime = calculate_interference_mitigation(row['signal_power'], row['interference_power'], row['noise_power'])
    latency = calculate_latency(row['request_time'], row['decision_time'], row['e2e_delay'])
    throughput = calculate_throughput(row['data_rate'])

    print(f"Selected Band: {chosen_band}")
    print(f"Spectrum Efficiency: {se:.2f} bits/sec/Hz")
    print(f"Interference Mitigation (SINR): {ime:.2f}")
    print(f"Latency: {latency:.4f} seconds")
    print(f"Network Throughput: {throughput/1e6:.2f} Mbps")
    print("-----------------------------\n")
