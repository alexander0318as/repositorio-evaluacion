dia = int(input("Día: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))


fecha_correcta = False

if mes in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= dia <= 31:
        fecha_correcta = True
elif mes in [4, 6, 9, 11]:
    if 1 <= dia <= 30:
        fecha_correcta = True
elif mes == 2:
    if 1 <= dia <= 28:
        fecha_correcta = True

if fecha_correcta:
    nombre_evento = input("Nombre del evento: ")
    horario = input("Horario (ej: 9:30 / 11:45): ")

    
    hora_inicio = int(horario.split(":")[0])
    if hora_inicio < 12:
        periodo = "AM"
    else:
        periodo = "PM"

    print("\nFECHA CORRECTA.")
    print(f"\nFECHA: {dia:02d}/{mes:02d}/{anio}")
    print("NOMBRE:", nombre_evento.upper())
    print("HORARIO:", horario, periodo)
else:
    print("\nFECHA INCORRECTA.")
    print("FAVOR VERIFICAR E INTENTAR DE NUEVO.")