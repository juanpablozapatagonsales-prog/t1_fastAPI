import requests

URL = "https://first-proejct-in-fastapi.onrender.com"
RUTA = "/trainee/"

# campo: tipo (str = texto, int = número)
CAMPOS = {
    "document": str,
    "firstName": str,
    "lastName": str,
    "email": str,
    "age": int,
    "programn": str,
    "record_number": int,
}


def imprimir_aprendiz(aprendiz):
    print("-" * 30)
    for campo, valor in aprendiz.items():
        print(f"{campo}: {valor}")


def mostrar(respuesta):
    print("\nCódigo:", respuesta.status_code)
    try:
        datos = respuesta.json()
    except ValueError:
        print(respuesta.text)
        return

    if isinstance(datos, list):
        if not datos:
            print("No hay aprendices registrados")
        for aprendiz in datos:
            imprimir_aprendiz(aprendiz)
    elif isinstance(datos, dict):
        imprimir_aprendiz(datos)
    else:
        print(datos)


def pedir_datos(permitir_vacios=False):
    datos = {}
    for campo, tipo in CAMPOS.items():
        while True:
            valor = input(f"{campo}: ")
            if valor == "" and permitir_vacios:
                break
            try:
                datos[campo] = tipo(valor)
                break
            except ValueError:
                print("Debe ser un número")
    return datos


def ver_todos():
    mostrar(requests.get(URL + RUTA, timeout=60))


def ver_uno():
    id = input("ID: ").strip()
    mostrar(requests.get(f"{URL}{RUTA}{id}", timeout=60))


def crear():
    mostrar(requests.post(URL + RUTA, json=pedir_datos(), timeout=60))


def actualizar():
    id = input("ID: ").strip()
    print("(deja vacío lo que no quieras cambiar)")
    datos = pedir_datos(permitir_vacios=True)
    mostrar(requests.put(f"{URL}{RUTA}{id}", json=datos, timeout=60))


def eliminar():
    id = input("ID: ").strip()
    mostrar(requests.delete(f"{URL}{RUTA}{id}", timeout=60))


def menu():
    opciones = {
        "1": ver_todos,
        "2": ver_uno,
        "3": crear,
        "4": actualizar,
        "5": eliminar,
    }
    while True:
        print("\n--- API de aprendices ---")
        print("1. Ver todos")
        print("2. Ver uno por ID")
        print("3. Crear")
        print("4. Actualizar")
        print("5. Eliminar")
        print("0. Salir")
        eleccion = input("Elige: ")

        if eleccion == "0":
            break
        if eleccion not in opciones:
            print("Opción no válida")
            continue
        try:
            opciones[eleccion]()
        except requests.exceptions.RequestException as error:
            print("Error de conexión:", error)


menu()
