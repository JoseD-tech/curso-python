
# Variables

string = "Juan" 
numerica = 2.2
boolean = True

#listas 
lista = [1, 18, 25, 2]

lista.append(7)
lista.append(2)

lista.sort()

lista2 = lista.copy()

lista2.append(9)

# tuplas

tupla = ( 1, 3, 7, 1,3,3,4 )


# Diccionario

diccionario = {
    'cedula': 32250736,
    "tipo_cuenta": 'Corriente',
    'clave': 3040,
    "saldo": 400
}

diccionario['saldo'] = diccionario.get('saldo') - 10

diccionario2 = len(diccionario)

print(diccionario2)


