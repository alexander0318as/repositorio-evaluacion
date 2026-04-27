nombre = input("Ingrese apellido y nombre: ")
categoria = input("Ingrese categoría (Junior, Semi Senior, Senior): ").lower()
antiguedad = int(input("Ingrese años de antigüedad: "))


if categoria == "junior":
    basico = 1500
elif categoria == "semi senior":
    basico = 2000
elif categoria == "senior":
    basico = 2500
else:
    print("Categoría inválida")
    exit()


if 1 <= antiguedad <= 5:
    porcentaje = 0.02
elif 6 <= antiguedad <= 10:
    porcentaje = 0.05
elif 11 <= antiguedad <= 20:
    porcentaje = 0.08
else:
    porcentaje = 0.10


monto_antiguedad = basico * porcentaje * antiguedad
sueldo_total = basico + monto_antiguedad
porcentaje_aumento = (monto_antiguedad / basico) * 100


print("\nAPELLIDO Y NOMBRE:", nombre.upper())
print("CATEGORÍA:", categoria.upper())
print("SUELDO BÁSICO: $", basico)
print("ANTIGÜEDAD:", antiguedad, "AÑOS")
print("MONTO ANTIGÜEDAD: $", monto_antiguedad)
print("SUELDO TOTAL: $", sueldo_total)

print("\nOBSERVACIONES:")
if monto_antiguedad > basico:
    print("EL EMPLEADO GANA MÁS POR ANTIGÜEDAD QUE POR SU SUELDO BÁSICO.")
else:
    print("EL EMPLEADO GANA MÁS POR SUELDO BÁSICO QUE POR SU ANTIGÜEDAD.")

print("EL PORCENTAJE DE AUMENTO ES:", porcentaje_aumento, "%")