"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Sección: 10
Proyecto 2: Funciones lambda.
"""
import sys

sys.setrecursionlimit(100000)

#Definiendo las funciones alpha y beta que se usarán para todas las operaciones.
#Función alpha.
alpha = lambda x: x + 1

#Función beta.
beta = lambda x: 2 * x

#Definiendo las funciones de los números naturales.

#Función 0.
cero = lambda f, x: x

#Función 1.
uno = lambda f, x: f(x)

#Función 2.
dos = lambda f, x: f(f(x))

#Función 3.
tres = lambda f, x: f(f(f(x)))

#Función 4.
cuatro = lambda f, x: f(f(f(f(x))))

#Función sucesor.
sucesor = lambda n, f, x: f(n(f, x))

#Función suma.
suma = lambda n, m, f, x: n(f, m(f, x)) #m(f, x) + n(f, x)

#Función multiplicar. n(m(f, x))
mul = lambda n, m, f, x: m(f, x)

#Función exponente.
exponente = lambda n, m, f, x: 1 if m == 0 else mul(n, m, f, x) * exponente(n, m, f, x)

print()
print("-------------------Alpha-------------------")
print()

print("Función 0: ", cero(alpha, 0))
print("Función 1: ", uno(alpha, 0))
print("Función 2: ", dos(alpha, 0))
print("Función 3: ", tres(alpha, 0))
print("Función 4: ", cuatro(alpha, 0))
print("Función sucesor: ", sucesor(cero, alpha, 0))
print("Función suma: ", suma(cero, tres, alpha, 0))
print("Función multiplicación: ", mul(dos, tres, alpha, 0))
#print("Función exponente: ", exponente(dos, tres, alpha, -1))

print()
print("--------------------Beta-------------------")
print()

print("Función 0: ", cero(beta, -1))
print("Función 1: ", uno(beta, -1))
print("Función 2: ", dos(beta, -1))
print("Función 3: ", tres(beta, -1))
print("Función 4: ", cuatro(beta, -1))
print("Función sucesor: ", sucesor(cuatro, beta, -1))
print("Función suma: ", suma(cero, tres, beta, -1))
print("Función multiplicación: ", mul(cero, tres, beta, -1))
#print("Función exponente: ", exponente(dos, tres, beta, -1))