print(5*"-"+"MENCARI NILAI FAHRENHAIT KE KELVIN"+"-"*5)
fahrenhait = float(input("masukan nilainya? "))
# f=...k
kelvin = (fahrenhait + 459.67) * 5/9
print(f"nilai f=...k : {kelvin}")
print("\n---------------------------\n")

print(5*"-"+"MENCARI NILAI KELVIN KE FAHRENHAIT"+"-"*5)
kelvin = float(input("masukan angka? "))
# k=...f
fahrenhait = (kelvin * 9/5) - 459.67
print(f"nilai k=...f : {fahrenhait}")

