"""
Fichero aleatorios.py

Nombre del alumno: Maria Freixas Solé

Este fichero implementa un generador de números pseudoaleatorios utilizando
el método del Congruente Lineal (LGC). Se incluyen una clase llamada `Generador`
y una función generadora `secuencia()` para producir secuencias de números.
Ambas implementaciones están documentadas y acompañadas de pruebas unitarias.
"""

class Generador:
    """
    Clase que implementa un generador de números pseudoaleatorios
    en el rango 0 <= Xn < m, mediante el método LGC (Linear Congruential Generator).

    Atributos:
        m (int): módulo de la operación.
        a (int): multiplicador.
        c (int): incremento.
        x (int): semilla o valor inicial de la secuencia.

    Métodos:
        __init__(): inicializa los atributos del generador.
        __next__(): devuelve el siguiente número pseudoaleatorio.
        __call__(): permite reiniciar el generador con una nueva semilla.

    >>> g = Generador(m=32, a=9, c=13, semilla=11)
    >>> for _ in range(4):
    ...     print(next(g))
    ...
    16
    29
    18
    15

    >>> g(29)
    >>> for _ in range(4):
    ...     print(next(g))
    ...
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, semilla=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = semilla

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, nueva_semilla, /):
        self.x = nueva_semilla


def secuencia(*, m=2**48, a=25214903917, c=11, semilla=1212121):
    """
    Función generadora que produce una secuencia de números pseudoaleatorios
    mediante el método del Congruente Lineal (LGC).

    Argumentos:
        m (int): módulo.
        a (int): multiplicador.
        c (int): incremento.
        semilla (int): valor inicial para la secuencia.

    Retorna:
        Generador tipo coroutine, que produce nuevos números y
        permite reiniciar la secuencia con `.send()`.

    >>> gen = secuencia(m=64, a=5, c=46, semilla=36)
    >>> for _ in range(4):
    ...     print(next(gen))
    ...
    34
    24
    38
    44

    >>> gen.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(gen))
    ...
    44
    10
    32
    14
    """
    x = semilla
    while True:
        siguiente = (a * x + c) % m
        nueva_semilla = (yield siguiente)
        if nueva_semilla is not None:
            x = nueva_semilla
        else:
            x = siguiente


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
