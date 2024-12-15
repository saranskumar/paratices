import numpy as np
import matplotlib.pyplot as plt

# Parameters for the amplifier
Vcc = 12  # Supply voltage in volts
Rc = 1e3  # Collector resistor in ohms
Re = 500  # Emitter resistor in ohms
Beta = 100  # Current gain

# Base current range (microamperes to milliamperes)
Ib = np.linspace(0, 50e-6, 500)  # Base current in amperes

# Calculate collector current and voltage gain
Ic = Beta * Ib  # Collector current in amperes
Vce = Vcc - Ic * Rc  # Collector-emitter voltage in volts
Gain = -Rc / Re  # Voltage gain (theoretical, constant for this setup)

# Plotting
plt.figure(figsize=(12, 6))

# Plot Collector Current vs Base Current
plt.subplot(1, 2, 1)
plt.plot(Ib * 1e6, Ic * 1e3, label="Ic vs Ib", color="blue")
plt.title("Collector Current vs Base Current")
plt.xlabel("Base Current (µA)")
plt.ylabel("Collector Current (mA)")
plt.grid()
plt.legend()

# Plot Vce vs Ic
plt.subplot(1, 2, 2)
plt.plot(Ic * 1e3, Vce, label="Vce vs Ic", color="green")
plt.title("Collector-Emitter Voltage vs Collector Current")
plt.xlabel("Collector Current (mA)")
plt.ylabel("Collector-Emitter Voltage (V)")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
