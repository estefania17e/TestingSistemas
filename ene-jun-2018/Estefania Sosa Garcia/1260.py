trees = {}

cases = int(input())

vacio = input(.split('\n'))

for x in range(cases):
    #limpiar la lista cada que haga un bucle el for
    trees.clear()
    cien_porciento = 0

    #ciclo while para capturar los árboles
    while True:
        #entrada de árboles
        in_trees = input()

        #si no tiene datos, salir del while
        if in_trees=="":
            break
        
        #si se ingresó un dato, se le agrega una unidad al árbol en cuestión
        if trees.get(in_trees):
            trees[in_trees]+=1
        
        #si no, deja el diccionario en 1
        else:
            trees[in_trees]=1
        
        #se agrega una unidad al 100%
        cien_porciento+=1

    #condición para imprimir un salto de línea cuando muestre la salida
    if x<num_casos-1:
        print("")

#ciclo para mostrar la salida
for arbol, porciento in sorted(trees.items()):
    porciento=100+(porciento/cien_porciento-1)*100
    print("%s %.4f" %(arbol,porciento))