# For the polytropic compression of a certain gas ( i.e., Pv^n = C ),
# the work done w_comp = (P_2 v_2 - P_1 v_1)/(n - 1).
# Write a Python program that calculates and prints the work done (kJ) for
# the polytropic expansion of the gas from 650 kPa and 0.020 m^3 to a final volume of 0.080 m^3, where n = 1.3
n = 1.3
P_1 = 650
v_1 = 0.020
v_2 = 0.080
P_2 = P_1 * (v_1 / v_2) ** n
w_comp = ((P_2 * v_2) - (P_1 * v_1))/(n - 1)
print(f"Work done (kJ): {w_comp:.2f}kJ")