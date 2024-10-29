# The n-th energy level for an electron in a Hydrogen atom is given by
# E_n = - (m_e * e^4) / (8*epsilon^2 * h^2) * (1 / n^2)
# where m_e = 9.1094E-31 kg is the electron mass, e = 1.6022E-19 C is the elementary charge,
# epsilon = 8.8542E-12 C^2 s^2 / (kg^1 m^3) is the electrical permittivity of vacuum,
# and h = 6.6261E-34 Js. Write a Python program that calculates and prints the energy level E_n for n = 1, . . ., 20
m_e = 9.1094E-31
e = 1.6022E-19
h = 6.6261E-34
epsilon = 8.8542E-12
for n in range(1, 21):
    E_n = - (m_e * e**4) / ((8 * epsilon**2) * h**2) * (1 / n**2)
    print(f"E_{n} = {E_n:.4e}J")