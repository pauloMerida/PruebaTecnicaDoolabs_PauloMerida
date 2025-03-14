#Paulo Mérida
from collections import deque
def sumar(numero):
    return numero+1

def multiplicar(numero):
    return numero*2


def invertir(numero):
    return int(str(numero)[::-1])

def main():
    
    procedimiento=""
    x=int(input("Ingrese el número x: "))
    y=int(input("Ingrese el número y: "))
    visitados = set()
    cola = deque()
    cola.append((x, 0, [x]))
    visitados.add(x)
    #Manejar casos extremos
    #que pasa si X es Y
    if x==y:
        print("No se requieren pasos")
        return "Pasos 0, numero: "+x
    elif y<x:
        # obligado a invertir y ver si ahora x es menor
        num_inv=invertir(x)
        if y<x:
            return ("No tiene solucion")
    contador=0
    num_inv=invertir(x)
    if num_inv<y and (x*2)<num_inv and num_inv>x:
        procedimiento+="invertir -> "+str(x)+" -> "
        x=num_inv
        contador+=1
        procedimiento+=str(x)+" -> "

    opere=False
    suma=True
    '''while x!=y:

        #intentar invertir
        num_inv=invertir(x)
        if num_inv<y and x*2<num_inv  and num_inv>x :
            procedimiento+="invertir -> "+str(x)+" -> "
            x=num_inv
            contador+=1
            procedimiento+=str(x)+" -> "
            opere=True

        #intentar multiplicar
        num_x2=multiplicar(x)
        if num_x2<=y and opere==False:
            contador+=1
            procedimiento+=str(x)+"* 2 -> "+str(num_x2) +" -> "
            x=num_x2
            opere=True
        
        #Verificar si ya puedo solo sumar
        num_inv=invertir(x)
        if num_inv<=x:
            num_inv=y+2

        num_x2=multiplicar(x)
        if num_inv>y and num_x2>y and opere==False:
            suma=True
            

        #sumarle numeros
        if opere==False and suma==True:
            
            num_sumado =sumar(x)
            contador+=1
            procedimiento+=str(x)+"+ 1 -> "+str(num_sumado) +" -> "
            x=num_sumado
            suma =False
        if x==y:
            break
        opere=False
    print( procedimiento+" Cantidad de pasos "+str(contador))'''
    while cola:
        actual, pasos, camino = cola.popleft()
        
        # Si llegamos al objetivo, devolvemos la cantidad de pasos y el camino
        if actual == y:
            for col in cola:
                print ("Cola" +str(col))
            for vis in visitados:
                print("Visitados"+str(vis))
            return pasos, camino
        
        # Generar las posibles operaciones
        opciones = [
            (multiplicar(actual), "Multiplicar por 2"),
            (sumar(actual), "Sumar 1"),
            (invertir(actual), "Invertir número")
        ]
        
        for nuevo_numero, operacion in opciones:
            if nuevo_numero not in visitados and nuevo_numero <= 10 ** 5:
                visitados.add(nuevo_numero)
                cola.append((nuevo_numero, pasos + 1, camino + [nuevo_numero]))
    
    return -1, []

result=main()
print(result)
