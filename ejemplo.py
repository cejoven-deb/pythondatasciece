n = "Hola, Estoy repasando python"
print(n)
# No se pueden cambiar los valores después de definir las tuplas
# Las tuplas van con parentesis
tuple=(1,2,3)
print(tuple)

print(tuple[0])

tupla=(1,2,3,4,5,6)

# Va a buscar el número 2 dentro de la tupla
print(2 in tupla)

#Las listas van con corchetes y se pueden cambiar los valores
#Append, permite agrega elementos  a las listas 

lista=[]

lista.append(1)

print(lista)

# Vamos a ecorrer una lista con un ciclo for


lista=[1,2,3,'m',9.8]
for e in lista:
    print(e)
    
# Vamos a hacer otro ejemplo de la lista
#Vamos a cambiar el 3 por un 100
lista=[1,2,3,'m',9.8]
lista[2]=1000
print(lista)

#Concatenar lista
listaA=[1,2,3]
listaB=[4,5,6]
listaA += listaB

print(listaA)

#Vamos a usar append


