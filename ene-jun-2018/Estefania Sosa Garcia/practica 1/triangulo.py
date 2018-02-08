import sys
l= list(map(int, input().strip().split(' ')))
#aqui creo que tengo un error 
for x in l:
    if (x<-100) or (x>100):
        print("fuera de rango")
        l= list(map(int, input().strip().split(' ')))

if (l[0]+l[1])>l[2] and (l[0]+l[2])>l[1] and (l[1]+l[2])>l[0]:
    if (l[0]==l[1]==l[2]):
        print("equilatero")
    elif(l[0]==l[1] or l[0]==l[2] or l[1]==l[2]):
        print("isoceles")
    else:
        print("escaleno")
else:
    print("no triangulo")
