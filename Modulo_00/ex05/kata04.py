# Put this at the top of your kata04.py file 
kata = (0, 4, 132.42222, 10000, 12345.67)


module_str = f"module_{kata[0]:02d}"
ex_str = f"ex_{kata[1]:02d}"
dec1_str = f"{kata[2]:.2f}"
entero_str = f"{kata[3]:.2e}"
dec2_str = f"{kata[4]:.2e}"

print(f"{module_str}, {ex_str} : {dec1_str}, {entero_str}, {dec2_str}")

