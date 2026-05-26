
def sumar(boton = 0):
    while True:
        try:
            numero = int(input('numero'))
        except:
            print('Solo numeros') 
        boton += numero
        print(boton)
def boton():
    numero = 0
    while True:
        boton = input()
        numero += 1 
        print (numero)
sumar()
