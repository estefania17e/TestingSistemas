import sys

def bonAppetit(n, k, b, ar):
    charge = 0
    for val in ar:
        charge += val/2.0
    charge = charge - ar[k]/2.0
    if b == charge:
        return 'Bon Appetit'
    else:
        return int(b-charge)
    
if __name__ == '__main__': 
    n, k = input('n articulos , indice que ana no comio').strip().split(' ')
    n, k = [int(n), int(k)]
    ar = list(map(int, input('precios').strip().split(' ')))
    b = int(input('dinero que cobraron a ana').strip())
    result = bonAppetit(n, k, b, ar)
    print(result)
