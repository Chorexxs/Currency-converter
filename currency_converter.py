# Programa para convertir dólares en euros

# Primero se define la función main

def main():
    print("Programa para convertir dolares en euros")
    print("")

    # El usuario escribe la cantidad y el programa la convierte en número con  "eval()"

    dollars = eval(input("Escribe la cantidad: "))
    print("")
    euros = convert_to_euros(dollars)

    print("Son", euros, "euros")

# Función que convierte los dólares en euros


def convert_to_euros(dollars):
    return dollars * 0.90

# Se llama a la función "main()" para ejecutar el programa


main()
