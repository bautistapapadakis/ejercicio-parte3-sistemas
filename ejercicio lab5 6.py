
tareas = []

def agregar_tarea():
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha = input("Ingrese la fecha de vencimiento (dd/mm/aaaa): ")

    tarea = {
        "descripcion": descripcion,
        "fecha": fecha,
        "completada": False
    }

    tareas.append(tarea)
    print("✅ Tarea agregada correctamente\n")


def mostrar_tareas():
    if len(tareas) == 0:
        print("No hay tareas.\n")
        return

    print("\n📋 Lista de tareas:")
    for i, tarea in enumerate(tareas):
        estado = "✔" if tarea["completada"] else "❌"
        print(f"{i+1}. {tarea['descripcion']} | Fecha: {tarea['fecha']} | Estado: {estado}")
    print()


def completar_tarea():
    mostrar_tareas()
    if len(tareas) == 0:
        return

    num = int(input("Ingrese el número de la tarea a completar: "))
    if 1 <= num <= len(tareas):
        tareas[num - 1]["completada"] = True
        print("✅ Tarea marcada como completada\n")
    else:
        print("❌ Número inválido\n")


def eliminar_tarea():
    mostrar_tareas()
    if len(tareas) == 0:
        return

    num = int(input("Ingrese el número de la tarea a eliminar: "))
    if 1 <= num <= len(tareas):
        tareas.pop(num - 1)
        print("🗑 Tarea eliminada\n")
    else:
        print("❌ Número inválido\n")


# Menú principal
while True:
    print("===== ADMINISTRADOR DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("❌ Opción inválida\n")