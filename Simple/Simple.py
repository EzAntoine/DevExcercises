from random import randint
from operator import itemgetter

def listaDicEdades():
    lista=[]

    for i in range(0,10):
        id=i+1 
        edad=randint(1,100) #Genera un entero aleatorio entre 1 y 100.
        dic={'ID':id, 'Edad':edad}

        lista.append(dic) #Agrega el diccionario creado a la lista.

    print(f"Lista de diccionarios: ",lista,"\n")
    return lista

def ordenarLista(lista):
    ordenada=sorted(lista, key=itemgetter('Edad'),reverse=True) #Ordena la lista recibida por el valor Edad.

    print(f"Lista ordenada: ",ordenada,"\n")

    print(f"ID de la persona mas joven de la lista: ",ordenada[len(ordenada)-1].get('ID'))
    print(f"ID de la persona mas longeva de la lista: ",ordenada[0].get('ID'))

    return ordenada


l=listaDicEdades()
ordenarLista(l)