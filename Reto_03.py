# Reto 03

# Restaurante

# Billetes
billete_5, billete_10, billete_20, billete_50, billete_100, billete_200, billete_500 = 5, 10, 20, 50, 100, 200, 500

# carta y precios
platos = ["paella", "judiones de la granja", "guisantes con jamon", "entrecot", "salmon"]
precio = [7, 9, 8, 15, 12]

carta = dict(zip(platos, precio))

nombre_restaurante = " Bienvenidos a Casa Paco "

# Título
title_bar_len = 50
print("#" * title_bar_len)
print(nombre_restaurante.center(title_bar_len, "#"))
print("#" * title_bar_len)


def imprimir_carta():
    """ Función que imprime la carta """
    print(" >> Carta << ".center(title_bar_len))
    for k_nombre, v_precio in carta.items():
        print(k_nombre.capitalize(), ":", v_precio, " €")


imprimir_carta()

more = True
menu_cliente = []

while more:
    menu_cliente.append(input("\nElige un plato\n>>> "))
    res_cliente = input("Deseas pedir algo más? (y/n): ")

    while res_cliente.lower() != "y" and res_cliente.lower() != "n":
        print("respuesta no válida")
        res_cliente = input("Deseas pedir algo más? (y/n): ")
    if res_cliente.lower() == "y":
        more = True
        imprimir_carta()
    elif res_cliente.lower() == "n":
        more = False

factura = 0

menu_cliente_revisado = []

for plato in menu_cliente:
    if plato.lower() in platos:
        factura = factura + carta[plato]
        menu_cliente_revisado.append(plato.capitalize())
    else:
        print("El plato {plato} no existe".format(plato=plato))

print("Menu: ", menu_cliente_revisado)
print("Total a pagar: ", factura, " €")
