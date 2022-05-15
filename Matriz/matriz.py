import numpy as np 


def crearMatriz():

    matriz=np.random.randint(10,size=(5,5))

    return matriz      

def buscarConsecutivos(matriz):
    
    cont=1
    inicio=0
    
    for i in range(0,5): 
        inicio=matriz[i][0]
        anterior=inicio
        cont=1

        for j in range(0,5):
            if (anterior+1==matriz[i][j]): 
                cont+=1
                if cont==4:
                    print("Se encontro una cadena de 4 numeros consecutivos!")
                    print(f"Valor inicial: ",inicio)
                    print(f"Valor final: ",matriz[i][j])
                    break
            else: cont=1            #Si no es igual al anterior vuelve el cont a 1.

            anterior=matriz[i][j]



m=crearMatriz()
print(m)
buscarConsecutivos(m)