import random
def es_primo(numero): # función para verificar si un numero es primo
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def mcd(a, b): # función para hallar el máximo común divisor (algoritmo de euclides)
    while b != 0:
        a, b = b, a % b
    return a

print("cifrador básico")

palabra = input("palabra clave a cifrar: ")

# seleccionamos dos números primos aleatorios p y q
p = 0
while not es_primo(p):
    p = random.randint(11, 97)

q = 0
while not es_primo(q) or p == q:
    q = random.randint(11, 97)

print(f"\nnumeros primos generados : p = {p}, q = {q}")

# calculamos n (el modulo) y phi (la funcion de euler)
n = p * q
phi = (p - 1) * (q - 1)

# buscamos 'e' que sea coprimo con phi (llave pública)
e = 0
while True:
    e = random.randint(2, 99)
    if mcd(e, phi) == 1:
        break

print(f"valor de 'e' generado (menor de 100): {e}")

# calculamos 'd' como el inverso multiplicativo de e modulo phi (llave privada)
d = 1
while (e * d) % phi != 1:
    d = d + 1

mensaje_cifrado = []

for letra in palabra: # proceso de cifrado letra por letra
    codigo_ascii = ord(letra) # convertimos la letra a su valor numérico ascii
    numero_cifrado = (codigo_ascii ** e) % n # aplicamos la formula rsa: (mensaje ^ e) mod n
    mensaje_cifrado.append(numero_cifrado)

print(f"\nmensaje cifrado en numeros: {mensaje_cifrado}")

mensaje_descifrado = ""

for numero in mensaje_cifrado: # proceso de descifrado numero por numero
    codigo_original = (numero ** d) % n # aplicamos la formula inversa rsa: (cifrado ^ d) mod n
    letra_original = chr(codigo_original) # convertimos el numero ascii de vuelta a texto
    mensaje_descifrado = mensaje_descifrado + letra_original

print(f"mensaje descifrado que es la palabra original: {mensaje_descifrado}")