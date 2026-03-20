# Cifrador Básico RSA en Python

Este repositorio contiene una implementación educativa del algoritmo de cifrado asimétrico **RSA** (*Rivest-Shamir-Adleman*). El script permite cifrar una palabra carácter por carácter y luego descifrarla utilizando conceptos fundamentales de teoría de números.

## Cómo Funciona el Algoritmo

El proceso de cifrado se divide en tres fases principales:

### 1. Generación de Claves
El programa selecciona dos números primos aleatorios ($p$ y $q$) entre 11 y 97. A partir de ellos, calcula:
* **$n$ (Módulo):** El producto de $p \times q$.
* **$\phi(n)$ (Función de Euler):** Calculado como $(p-1) \times (q-1)$.
* **$e$ (Exponente Público):** Un número aleatorio tal que sea coprimo con $\phi(n)$.
* **$d$ (Exponente Privado):** El inverso multiplicativo de $e$ módulo $\phi(n)$.

### 2. Proceso de Cifrado
Para cada letra de la palabra ingresada:
1. Se obtiene su valor **ASCII** (ej. 'A' = 65).
2. Se aplica la fórmula:  
   $$C = M^e \pmod{n}$$  
   Donde $M$ es el mensaje original y $C$ es el número cifrado.

### 3. Proceso de Descifrado
Para recuperar el mensaje, se toma cada número cifrado $C$ y se aplica:  
   $$M = C^d \pmod{n}$$  
Luego, el valor numérico $M$ se convierte de nuevo a su carácter correspondiente.

## Estructura de las Funciones

| Función | Propósito |
| :--- | :--- |
| `es_primo(numero)` | Evalúa si un número es primo mediante divisiones sucesivas. |
| `mcd(a, b)` | Utiliza el algoritmo de Euclides para encontrar el Máximo Común Divisor. |
| `input()` | Solicita al usuario la palabra clave a procesar. |


## Ejemplo de Salida

Al ejecutar el código, verás un flujo similar a este:

```text
cifrador básico
palabra clave a cifrar: Python

numeros primos generados : p = 61, q = 53
valor de e generado (menor de 100): 17

mensaje cifrado en numeros: [234, 1209, 87, 456, ...]
mensaje descifrado que es la palabra original: Python
