"""
Nombre: Javier Sebastián Valle Balsells
Carnet: 20159
Sección: 10
Proyecto 2: Funciones lambda.

Referencias: 

1. Como imprimier el resultado de una función lambda: https://stackoverflow.com/questions/67552413/printing-of-a-function-or-lambda
"""

def get_name(f): #Función para poder ver el resultado que computa la función lambda.
    try: name = [k for k,v in globals().items() if v==f][0]
    except: return f
    return '%s: %s' % (name, f)

#Definiendo las funciones alpha y beta que se usarán para todas las operaciones.
#Función alpha.
alpha = lambda x: x + 1

#Función beta.
beta = lambda x: 2 * x

#Definiendo las funciones de los números naturales.

#Función 0.
cero = lambda f: lambda x: x

#Función 1.
uno = lambda f: lambda x: f(x)

#Función 2.
dos = lambda f: lambda x: f(f(x))

#Función 3.
tres = lambda f: lambda x: f(f(f(x)))

#Función 4.
cuatro = lambda f: lambda x: f(f(f(f(x))))

#Función 5.
cinco = lambda f: lambda x: f(f(f(f(f(x)))))

#Función sucesor.
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))

#Función suma.
suma = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))

#Función multiplicar. n(m(f, x)). m se va a componer con sigo misma n veces.
multiplicar = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)

#Función exponente.
exponente = lambda m: lambda n: lambda f: lambda x: n(m)(f)(x)

N = get_name #Función para obtener el nombre de la función.
# T = lambda x: lambda y: x #Función para obtener el primer elemento de una tupla.
# N(T(2)(3))

# print(N(T(2)(3)))

print()
print("-------------------Alpha-------------------")
print()

print("Función 0: ", N(cero(alpha)(0)))
print("Función 1: ", N(uno(alpha)(0)))
print("Función 2: ", N(dos(alpha)(0)))
print("Función 3: ", N(tres(alpha)(0)))
print("Función 4: ", N(cuatro(alpha)(0)))
print("Función 5: ", N(cinco(alpha)(0)))
print("Función sucesor: ", N(sucesor(uno)(alpha)(0)))
print("Función suma: ", N(suma(dos)(dos)(alpha)(0)))
print("Función multiplicar: ", N(multiplicar(dos)(tres)(alpha)(0)))
print("Función exponente: ", N(exponente(cinco)(cuatro)(alpha)(0)))

print()
print("--------------------Beta-------------------")
print()

print("Función 0: ", N(cero(beta)(-1)))
print("Función 1: ", N(uno(beta)(-1)))
print("Función 2: ", N(dos(beta)(-1)))
print("Función 3: ", N(tres(beta)(-1)))
print("Función 4: ", N(cuatro(beta)(-1)))
print("Función 5: ", N(cinco(beta)(-1)))
print("Función sucesor: ", N(sucesor(uno)(beta)(-1)))
print("Función suma: ", N(suma(dos)(dos)(beta)(-1)))
print("Función multiplicar: ", N(multiplicar(dos)(tres)(beta)(-1)))
print("Función exponente: ", N(exponente(cinco)(cuatro)(beta)(-1)))