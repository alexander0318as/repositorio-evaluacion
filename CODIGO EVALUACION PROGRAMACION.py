def sistema_control_acceso():
    # --- ENCABEZADO ---
    print("==========================================")
    print("   SISTEMA DE SEGURIDAD BIOMÉTRICA v2.0   ")
    print("==========================================\n")

    # --- VALIDACIÓN DE LA EDAD (Solo números) ---
    # Usamos un bucle infinito 'while True' que solo se rompe ('break') cuando el dato es válido
    while True:
        entrada_edad = input("Entrada -> Ingrese la edad: ")
        
        # .isdigit() verifica si el texto escrito son solo números (0-9)
        if entrada_edad.isdigit():
            edad = int(entrada_edad) # Convertimos el texto a número entero
            break # Salimos del bucle porque el dato es correcto
        else:
            print("⚠️ ERROR: La edad debe ser un número entero (ej: 25). Inténtelo de nuevo.")

    # --- VALIDACIÓN DE IDENTIFICACIÓN (Solo letras y si/no) ---
    while True:
        # .lower() convierte a minúsculas, .strip() quita espacios accidentales
        tiene_id = input("Entrada -> ¿Tiene identificación? (si/no): ").lower().strip()
        
        # Verificamos que sea solo texto (.isalpha()) y que sea 'si' o 'no'
        if tiene_id.isalpha() and tiene_id in ["si", "no"]:
            # Convertimos la respuesta en un valor Booleano (True o False) para lógica interna
            tiene_id_bool = (tiene_id == "si")
            break
        else:
            print("⚠️ ERROR: Solo se permite 'si' o 'no' (sin números ni símbolos).")

    # --- VALIDACIÓN DE REGISTRO (Solo letras y si/no) ---
    while True:
        esta_registrado = input("Entrada -> ¿Está registrado en el sistema? (si/no): ").lower().strip()
        
        if esta_registrado.isalpha() and esta_registrado in ["si", "no"]:
            esta_registrado_bool = (esta_registrado == "si")
            break
        else:
            print("⚠️ ERROR: Responda únicamente 'si' o 'no'.")

    # --- PROCESAMIENTO DE REGLAS DE NEGOCIO ---
    
    # 1. Verificación base: Sin ID o sin Registro no entra nadie, sin importar la edad.
    if tiene_id_bool and esta_registrado_bool:
        
        # 2. Verificación de seguridad para menores
        if edad < 18:
            print("\n[INFO] Detectado menor de edad. Verificando protocolo de acompañamiento...")
            
            while True:
                acompanado = input("si/no): ").lower().strip()
                if acompanado.isalpha() and acompanado in ["si", "no"]:
                    break
                else:
                    print("⚠️ ERROR: Responda 'si' o 'no'.")
            
            # Resultado final para menores
            if acompanado == "si":
                print("\n✅ ACCESO CONCEDIDO: Menor autorizado con acompañante.")
            else:
                print("\n❌ ACCESO DENEGADO: Los menores no pueden entrar solos.")
        TO
    
        # 3. Resultado para adultos autorizados
        else:
            print("\n✅ ACCESO CONCEDIDO: Usuario adulto verificado correctamente.")
            
    else:
        # Mensaje de rechazo si faltan requisitos básicos
        print("\n❌ ACCESO DENEGADO: No cumple con los requisitos mínimos (ID y Registro).")

# --- INVOCACIÓN DEL PROGRAMA ---
# Esto hace que el código empiece a correr
if __name__ == "__main__":
    sistema_control_acceso()