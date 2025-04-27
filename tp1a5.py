def actividad5(numromanos):
    valores = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    total = 0
    valoranterior = 0
    
    for letra in reversed(numromanos):
        valor = valores.get(letra, 0)
        
        if valor < valoranterior:
            total -= valor
        else:
            total += valor
        
        valoranterior = valor
    
    return total

numero = input("Escriba un número romano: ")
resultado = actividad5(numero)

print(f"El número equivale a {resultado}.")