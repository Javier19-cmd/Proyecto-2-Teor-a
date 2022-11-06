# Proyecto 2 (Teoría de la Computación): Funciones lambda

El presente proyecto consiste en definir una serie de números, el rango de los números está comprendido entre cero y siete, con funciones lambda. Las funciones numéricas se definieron de la siguiente forma: 

- La función cero se definió de la siguiente manera: cero = λf.λx = x.
- La función uno se definió de la siguiente manera: uno = λf.λx = f(x).
- La función dos se definió de la siguiente manera: dos = λf.λx = f(f(x)).
- La función tres se definió de la siguiente manera: tres = λf.λx = f(f(f(x))).
- La función cuatro se definió de la siguiente manera: cuatro = λf.λx = f(f(f(f(x)))).
- La función cinco se definió de la siguiente manera: cinco = λf.λx = f(f(f(f(f(x))))).
- La función seis se definió de la siguiente manera: seis = λf.λx = f(f(f(f(f(f(x)))))).
- La función siete se definió de la siguiente manera: siete = λf.λx = f(f(f(f(f(f(f(x))))))).

Seguido de esta definición se realizaron ciertas operaciones aritméticas con estos números. Dichas operaciones aritméticas son las siguientes: sucesor, suma, multiplicación y potencia.

- La función sucesor de definió de la siguiente manera: sucesor = λn.λf.λx = a(f(b(f(x)))).
- La función suma se definió de la siguiente manera: suma = λm.λn.λf.λx = a(f(b(f(x)))).
- La función multiplicación se definió de la siguiente manera: suma = λm.λn.λf.λx = a((b(f(x)))).
- La función de potencia se definió de la siguiente manera: potencia = λm.λn.λf.λn = n(m)(f)(x).

# Sugerencia:

Se recomienda que para poder llevar a cabo este proyecto se tenga claro a nivel teórico que es una función lambda y su definición, dado que existen documentaciones que definen las funciones lambda de diferente manera. Asimismo, es importante tener en claro como es que funciona a nivel matemático como es que funciona una composición de funciones, dado que tanto para definir un número como para definir una función numérica se debe tener en claro como funiona la composición de funciones y se debe tener cierta habilidad para poderlas componer. 
