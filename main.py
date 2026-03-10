import re


def limpiarvalores(valor):
    #Elimina espacios en blanco
    valor=valor.strip()
    #quita los valroes excepto esos que van despues de simbolo raro y los remplaza por lo que esta en als comillas
    valor=re.sub("[^0-9.-]","",valor)

    #si despues de haberlos limpiado no queda nada entonces regresa un cero
    if valor =="":
            return "0"
    return valor


def procesar_linea(linea):
    #separa los valores de comas como si fuera un arreglo de ["1,2,3,4"] a ["1","2","3",...]
    valores=linea.split(",")
    limpio=[]
    #de i en el rango de valores va pasar por toda esa linea o arreglo y los limpiara qudadno solo nuemros separados por comas
    #y se guarda en un arreglo
    for i in valores:
        limpio.append(limpiarvalores(i))
    suma=0
    
    #ahora la variable valor toma un valor del arreglo limpio en limpio y va sumando asi hara con cada linea
    for valor in limpio:
         suma=suma+int(float(valor))

    return suma



def main():
    """
    Lee de stdin linea por linea
    Procesa cada linea
    Imprime el resultado
    """
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == "__main__":
    main()
         
      
       





    