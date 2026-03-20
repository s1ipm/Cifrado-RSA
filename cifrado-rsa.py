import random

def es_primo(numero): # función para verificar si un numero es primo
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mcd(a, b): # función para hallar el máximo común divisor (algoritmo de euclides)
    while b != 0:
        a, b = b, a % b
    return a

print("cifrador rsa básico")

# solicitar la palabra a cifrar
palabra = input("palabra clave a cifrar: ")

# generar p y q aleatorios y validar que sean primos
p = 0
while not es_primo(p):
    p = random.randint(11, 97)

q = 0
while not es_primo(q) or p == q:
    q = random.randint(11, 97)

# calculamos n (el modulo) y phi (la funcion de euler)
n = p * q
phi = (p - 1) * (q - 1)

# generar e aleatorio menor que 100 y coprimo con phi
e = 0
while True:
    e = random.randint(2, 99)
    # e debe ser menor que phi y su mcd con phi debe ser 1
    if e < phi and mcd(e, phi) == 1:
        break

# calculo de d (inverso modular)
# buscamos d tal que (e * d) % phi == 1
d = 1
while (e * d) % phi != 1:
    d += 1

# convertir letras a ascii y cifrar
mensaje_cifrado = []
for letra in palabra:
    codigo_ascii = ord(letra) # convertimos la letra a su valor numérico ascii
    # cifrado: (mensaje ^ e) mod n
    # usamos pow(a, b, c) para manejar potencias grandes eficientemente
    numero_cifrado = pow(codigo_ascii, e, n)
    mensaje_cifrado.append(numero_cifrado)

# descifrado (comprobación)
mensaje_descifrado = ""
for numero in mensaje_cifrado:
    # descifrado: (cifrado ^ d) mod n
    codigo_original = pow(numero, d, n)
    letra_original = chr(codigo_original) # convertimos el numero ascii de vuelta a texto
    mensaje_descifrado = mensaje_descifrado + letra_original

print("\nvalores generados")
print(f"valor de p: {p}")
print(f"valor de q: {q}")
print(f"valor de n (p * q): {n}")
print(f"valor de phi ((p-1)*(q-1)): {phi}")
print(f"valor de e (llave pública): {e}")
print(f"valor de d (inverso modular): {d}")

print("\nresultados del cifrado")
print(f"mensaje cifrado en numeros: {mensaje_cifrado}")

print("\ncomprobación del descifrado")
print(f"mensaje descifrado final: {mensaje_descifrado}")
