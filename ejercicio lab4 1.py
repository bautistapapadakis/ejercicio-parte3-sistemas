def agregar_tarea(tareas, tarea, fecha_limite, prioridad, completada=False):
    nueva_tarea = {
        "Tarea": tarea,
        "Fecha limite": fecha_limite,
        "Prioridad": prioridad,
        "Completada": completada
    }
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")


def mostrar_tareas(tareas, completadas=None):
    if not tareas:
        print("No hay tareas.")
        return

    for i, tarea in enumerate(tareas, 1):
        # Filtrar según estado
        if completadas is True and not tarea["Completada"]:
            continue
        if completadas is False and tarea["Completada"]:
            continue

        print(f"\nTarea {i}:")
        for clave, valor in tarea.items():
            print(f"{clave}: {valor}")


def marcar_completada(tareas):
    if not tareas:
        print("No hay tareas para marcar.")
        return

    mostrar_tareas(tareas)

    try:
        indice = int(input("Ingrese el número de la tarea a completar: ")) - 1

        if 0 <= indice < len(tareas):
            tareas[indice]["Completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Debe ingresar un número válido.")


if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar TODAS las tareas")
        print("3. Mostrar tareas COMPLETADAS")
        print("4. Mostrar tareas PENDIENTES")
        print("5. Marcar tarea como completada")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = input("Ingrese la fecha limite (dd/mm/yyyy): ")
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)

        elif opcion == "2":
            mostrar_tareas(lista_tareas)

        elif opcion == "3":
            mostrar_tareas(lista_tareas, completadas=True)

        elif opcion == "4":
            mostrar_tareas(lista_tareas, completadas=False)

        elif opcion == "5":
            marcar_completada(lista_tareas)

        elif opcion == "6":
            break

        else:
            print("Opción no válida.")
