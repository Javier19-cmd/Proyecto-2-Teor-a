"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Sección: 10
Proyecto 2: Funciones lambda.
"""

#Definiendo las funciones alpha y beta que se usarán para todas las operaciones.
#Función alpha.
alpha = lambda x: x + 1

#Función beta.
beta = lambda x: 2 * x

#Definiendo las funciones de los números naturales.

#Función 0.
zero = lambda f, x: f(x)

#Función 1.
one = lambda f, x: f(f(x))

#Función 2.
two = lambda f, x: f(f(f(x)))

#Función 3.
three = lambda f, x: f(f(f(f(x))))

print("Función 0: ", zero(alpha, -1))
print("Función 1: ", one(alpha, -1))
print("Función 2: ", two(alpha, -1))
print("Función 3: ", three(alpha, -1))
