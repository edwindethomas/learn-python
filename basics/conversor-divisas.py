def conversor(tipo_pesos,valor_dolar):
    pesos = float(input("¿Cuántos pesos " + tipo_pesos +  " tienes?: "))
    dolares = str(round(pesos / valor_dolar,2))
    print("Tienes $" + dolares+ " dólares")


menu = """
***Conversior de monedas***

1) Pesos Mexicanos a dólares
2) Pesos Colombianos a dólares
3) Pesos Argentinos a dólares
 """
opcion = input(menu)

if opcion == '1':
    conversor('mexicanos',19.77)
elif opcion == '2':
    conversor('colombianos',3875)
elif opcion == '3':
    conversor('argentinos',65)
else:
    print("Ingresa una opción correcta")