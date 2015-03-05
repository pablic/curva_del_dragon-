def curvaD(n):
    cad = ""
    if n == 1 :
        cad += "I"
    else :cad += curvaD( n-1) +"I"+ cambio(curvaD( n-1 ))
    return cad

def cambio(cad):
    cad = cad[::-1]
    ncad = ""
    for i in range(len(cad)):
        if cad[i] == "I":
            ncad += "D"
        elif cad[i]== "D":
            ncad += "I"
    return ncad
print ("\n"+"Ingresa el numero de la secuencia de LA CURVA DEL DRAGON")
print("que quieres ver :")
p = int (raw_input())
print("\n"+"La secuencia es : \n")
print(curvaD(p) + "\n")