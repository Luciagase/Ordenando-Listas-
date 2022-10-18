# Ejercicio 1: Utilice las funciones anteriores para agregar elementos faltantes
# Ejercicio 2: Utilice las funciones anteriores para elminar elementos sobrantes

def ejercicio1():
    lista = ['P', 't']
    lista.insert(1,'y')
    lista.extend(['h','o','n'])
    assert ''.join(lista) == 'Python'
   

def ejercicio2():
    lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    del lista [1]
    del lista [2:4]
    del lista [4]
    del lista [5:]
    assert lista == list(range(1, 6))


