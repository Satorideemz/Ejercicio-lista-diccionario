

def repetidos(lista):
    resultado = {}
   

    for numero in lista:
        if numero in resultado:
            resultado[numero] += 1
        else:
            resultado[numero] = 1
    return resultado


if __name__ == "__main__":
    numero = input('Ingresa numeros: ')
    print(repetidos(numero))
