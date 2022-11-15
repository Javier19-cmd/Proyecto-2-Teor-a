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

#Función 6.
seis = lambda f: lambda x: f(f(f(f(f(f(x))))))

#Función 7.
siete = lambda f: lambda x: f(f(f(f(f(f(f(x)))))))

#Función sucesor.
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))

#Función suma.
suma = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))

#Función multiplicar. n(m(f, x)). m se va a componer con sigo misma n veces.
multiplicar = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)

#Función exponente. n(m)(f)(x) = m^n(f)(x). 
exponente = lambda m: lambda n: lambda f: lambda x: n(m)(f)(x)

print()
print("-------------------Alpha-------------------")
print()
print("Función cero: ",cero(alpha)(0))
print("Función uno: ",uno(alpha)(0))
print("Función dos: ",dos(alpha)(0))
print("Función tres: ",tres(alpha)(0))
print("Función cuatro: ",cuatro(alpha)(0))
print("Función cinco: ",cinco(alpha)(0))
print("Función sucesor de cero: ",sucesor(cero)(alpha)(0))
print("Función suma: ", suma(cuatro)(tres)(alpha)(0))
print("Función multiplicar: ", multiplicar(cuatro)(tres)(alpha)(0))
print("Función exponente: ", exponente(cuatro)(tres)(alpha)(0))

print()
print("--------------------Beta-------------------")
print()

print("Función 0: ", cero(beta)(-1))
print("Función 1: ", uno(beta)(-1))
print("Función 2: ", dos(beta)(-1))
print("Función 3: ", tres(beta)(-1))
print("Función 4: ", cuatro(beta)(-1))
print("Función 5: ", cinco(beta)(-1))
print("Función sucesor: ", sucesor(uno)(beta)(-1))
print("Función suma: ", suma(dos)(dos)(beta)(-1))
print("Función multiplicar: ", multiplicar(dos)(tres)(beta)(-1))
print("Función exponente: ", exponente(cinco)(cuatro)(beta)(-1))