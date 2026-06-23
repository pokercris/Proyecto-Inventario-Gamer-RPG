
inventario_gamer = []

def registrar_personaje():
   
    print("\n--- REGISTRAR NUEVO PERSONAJE ---")
    
    # NOMBRE NO VACIO Y UNICO
    while True:
        nombre = input("Nombre del personaje: ").strip().capitalize()
        if not nombre:
            print(" El nombre no puede estar vacío.")
            continue
        
        # QUE NO SE REPITAN NOMBRES
        duplicado = False
        for personaje in inventario_gamer:
            if personaje['nombre'] == nombre:
                duplicado = True
                break
        
        if duplicado:
            print(" Este personaje ya existe en el inventario. Elige otro nombre.")
        else:
            break

    # VALIDACIO CLASE
    while True:
        clase = input("Clase (Ej: Guerrero, Mago, Asesino): ").strip().capitalize()
        if not clase:
            print(" La clase no puede estar vacía.")
        else:
            break

    # VALIDACION RAREZA
    while True:
        rareza = input("Rareza (Ej: Común, Épico, Legendario): ").strip().capitalize()
        if not rareza:
            print(" La rareza no puede estar vacía.")
        else:
            break

    # DAÑO VALIDACION
    while True:
        try:
            dano = int(input("Puntos de Daño (Número entero): "))
            if dano < 0:
                print(" El daño no puede ser negativo.")
                continue
            break
        except ValueError:
            print(" Entrada inválida. Debes ingresar un número entero.")

    
    nuevo_personaje = {
        "nombre": nombre,
        "clase": clase,
        "rareza": rareza,
        "dano": dano  
    }

    # GUARDAR
    inventario_gamer.append(nuevo_personaje)
    print(f"✅ ¡{nombre} ha sido agregado con éxito al inventario!")


def mostrar_personajes():
    """
    Función para LEER (Read) y mostrar todos los personajes registrados.
    Si la lista está vacía, se le notifica al usuario.
    """
    print("\n--- INVENTARIO DE PERSONAJES ---")
    if not inventario_gamer:
        print(" El inventario está vacío. ¡Registra un personaje primero!")
        return

    
    for i, personaje in enumerate(inventario_gamer, start=1):
        print(f"{i}. Nombre: {personaje['nombre']} | Clase: {personaje['clase']} | Rareza: {personaje['rareza']} | Daño: {personaje['dano']}")


def actualizar_personaje():
    """
    Función para ACTUALIZAR (Update) los datos de un personaje existente.
    Busca al personaje por su nombre.
    """
    print("\n--- ACTUALIZAR PERSONAJE ---")
    if not inventario_gamer:
        print(" No hay personajes para actualizar.")
        return

    nombre_buscar = input("Ingresa el nombre del personaje que deseas modificar: ").strip().capitalize()
    
    personaje_encontrado = None
    for personaje in inventario_gamer:
        if personaje['nombre'] == nombre_buscar:
            personaje_encontrado = personaje
            break

    if not personaje_encontrado:
        print(" Personaje no encontrado.")
        return

    print(f"\nPersonaje encontrado: {personaje_encontrado['nombre']}")
    print("Modifica sus datos (deja en blanco para mantener el valor actual):")

    # -MODIFICADOR CLASE-
    nueva_clase = input(f"Nueva Clase [{personaje_encontrado['clase']}]: ").strip().capitalize()
    if nueva_clase:
        personaje_encontrado['clase'] = nueva_clase

    # -MODIFICADOR RAREZA-
    nueva_rareza = input(f"Nueva Rareza [{personaje_encontrado['rareza']}]: ").strip().capitalize()
    if nueva_rareza:
        personaje_encontrado['rareza'] = nueva_rareza

    # -MODIFICADOR DE DAÑO-
    while True:
        nuevo_dano_input = input(f"Nuevo Daño [{personaje_encontrado['dano']}]: ").strip()
        if not nuevo_dano_input:
            
            break
        try:
            nuevo_dano = int(nuevo_dano_input)
            if nuevo_dano < 0:
                print(" El daño no puede ser negativo.")
                continue
            personaje_encontrado['dano'] = nuevo_dano
            break
        except ValueError:
            print(" Entrada inválida. Debes ingresar un número entero.")

    print(f"✅ ¡Los datos de {personaje_encontrado['nombre']} se actualizaron correctamente!")


def eliminar_personaje():
    """
    Función para ELIMINAR (Delete) un personaje de la lista principal.
    Busca por nombre y remueve el diccionario.
    """
    print("\n--- ELIMINAR PERSONAJE ---")
    if not inventario_gamer:
        print("📭 No hay personajes para eliminar.")
        return

    nombre_buscar = input("Ingresa el nombre del personaje que deseas eliminar: ").strip().capitalize()

    for personaje in inventario_gamer:
        if personaje['nombre'] == nombre_buscar:
            inventario_gamer.remove(personaje)
            print(f" ¡{nombre_buscar} ha sido eliminado del inventario!")
            return

    print(" No se encontró ningún personaje con ese nombre.")


def menu_principal():
    """
    Función principal que controla el flujo del programa mediante un ciclo infinito (while True).
    Muestra el menú interactivo al usuario.
    """
    while True:
        print("\n==============================")
        print("      INVENTARIO GAMER        ")
        print("==============================")
        print("1. Registrar Personaje (Create)")
        print("2. Ver Inventario (Read)")
        print("3. Actualizar Personaje (Update)")
        print("4. Eliminar Personaje (Delete)")
        print("5. Salir del Programa")
        print("==============================")
        
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            registrar_personaje()
        elif opcion == "2":
            mostrar_personajes()
        elif opcion == "3":
            actualizar_personaje()
        elif opcion == "4":
            eliminar_personaje()
        elif opcion == "5":
            print("\n ¡Gracias por usar el sistema de Inventario Gamer! Saliendo...")
            break
        else:
            print(" Opción inválida. Por favor, selecciona un número del 1 al 5.")

# Ejecución del programa
if __name__ == "__main__":
    menu_principal()