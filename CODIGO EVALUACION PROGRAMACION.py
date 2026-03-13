def sistema_control_acceso():
    print("--- Sistema de Control de Acceso al Edificio ---")
    
    # Entrada de datos
    try:
        edad = int(input("Ingrese la edad: "))
        tiene_id = input("¿Tiene identificación? (si/no): ").lower().strip() == "si"
        esta_registrado = input("¿Está registrado en el sistema? (si/no): ").lower().strip() == "si"
        
        # Evaluación de las reglas del sistema
        # Regla base: Debe tener ID y estar registrado
        if tiene_id and esta_registrado:
            
            # Regla específica por edad
            if edad < 18:
                acompanado = input("¿Está acompañado por un adulto? (si/no): ").lower().strip() == "si"
                
                if acompanado:
                    print("\n✅ ACCESO CONCEDIDO: Menor de edad con acompañante autorizado.")
                else:
                    print("\n❌ ACCESO DENEGADO: Los menores de edad deben estar acompañados.")
            
            else:
                print("\n✅ ACCESO CONCEDIDO: Usuario adulto autorizado.")
                
        else:
            # Si falta ID o Registro, no importa la edad
            motivo = ""
            if not tiene_id: motivo += "- Falta identificación. "
            if not esta_registrado: motivo += "- No está en la base de datos."
            
            print(f"\n❌ ACCESO DENEGADO: {motivo}")

    except ValueError:
        print("\n⚠️ ERROR: Por favor, ingrese un número válido para la edad.")

# Ejecutar el programa
sistema_control_acceso()