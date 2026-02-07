import sympy as sp

# Definimos la función de Riemann
def Integral_Riemann(f, a, b, n):
    x = sp.Symbol('x')
    delta_x = (b - a) / n
    suma = 0
    # Usamos rectángulos izquierdos
    for i in range(n):
        xi = a + i*delta_x
        suma += f.subs(x, xi)
    Area = suma * delta_x
    return Area

# -------------------------------
# Ejemplo: Integral de 0 a 1 (x^2 * e^(x^3+1) dx)
x = sp.Symbol('x')
f = x**2 * sp.exp(x**3 + 1)

# Valor real de la integral con sympy
valor_real = sp.integrate(f, (x, 0, 1))
print("Valor real de la integral:", valor_real.evalf())

# Aproximación con Riemann (n=4 particiones)
valor_aproximado = Integral_Riemann(f, 0, 1, 4)
print("Valor aproximado (Riemann con 4 particiones):", valor_aproximado.evalf())

# Error relativo
error_relativo = abs((valor_real - valor_aproximado) / valor_real)
print("Error relativo:", error_relativo.evalf())
