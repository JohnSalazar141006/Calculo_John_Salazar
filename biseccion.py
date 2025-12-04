from sympy import symbols, sympify, lambdify

def biseccion_sympy(f_expr, a, b, E, N):
    """
    Método de Bisección para encontrar una raíz de f(x) en [a, b] usando SymPy.

    Parámetros:
    - f_expr: expresión simbólica de la función f(x)
    - a, b: extremos del intervalo (a < b)
    - E: cota de error (E > 0)
    - N: número máximo de iteraciones (1 ≤ N ≤ 50)

    Retorna:
    - mi: aproximación de la raíz
    - error: valor absoluto de f(mi)
    - iteraciones: número de iteraciones realizadas
    """

    # Validaciones estrictas
    if not hasattr(f_expr, 'subs'):
        raise TypeError("❌ f_expr debe ser una expresión simbólica de SymPy.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("❌ a y b deben ser números reales.")
    if a >= b:
        raise ValueError("❌ El valor de a debe ser menor que b.")
    if not isinstance(E, (int, float)) or E <= 0:
        raise ValueError("❌ E debe ser un número positivo.")
    if not isinstance(N, int) or not (1 <= N <= 50):
        raise ValueError("❌ N debe estar entre 1 y 50.")

    x = symbols('x')
    f = lambdify(x, f_expr)

    if f(a) * f(b) >= 0:
        raise ValueError("❌ f(a) y f(b) deben tener signos opuestos.")

    # Enunciado dinámico
    print("📝 ENUNCIADO DEL EJERCICIO")
    print(f"Aproximar la raíz de la función f(x) = {f_expr}")
    print(f"en el intervalo [{a}, {b}], mediante el método de bisección,")
    print(f"hasta que el error relativo sea menor a {E}, con un máximo de {N} iteraciones.\n")

    print("📘 FORMULAS USADAS")
    print("xr = (x_a + x_b)/2")
    print("Error = |(xr_actual - xr_anterior)/xr_actual|\n")

    print("📊 TABLA DE ITERACIONES")
    print(f"{'i':<5}{'x_a':<12}{'x_b':<12}{'x_r':<12}{'f(x_a)*f(x_r)':<20}{'Error':<12}")
    print("-"*75)

    xr_anterior = None

    for i in range(1, N + 1):
        xr = (a + b) / 2
        f_xr = f(xr)
        cambio = f(a) * f_xr

        # Calcular error relativo si hay xr anterior
        if xr_anterior is None:
            error = None
        else:
            error = abs((xr - xr_anterior) / xr)

        print(f"{i:<5}{a:<12.6f}{b:<12.6f}{xr:<12.6f}{cambio:<20.6f}{'' if error is None else f'{error:<12.6f}'}")

        if error is not None and error < E:
            print("\n✅ Criterio de convergencia alcanzado.")
            return xr, error, i

        if f(a) * f_xr < 0:
            b = xr
        else:
            a = xr

        xr_anterior = xr

    print("\n⚠️ Se alcanzó el número máximo de iteraciones sin cumplir la cota de error.")
    return xr, error, N


# 🧪 Ejemplo de uso
f_expr = sympify("(x - 2)**2 - log(x)")
a = 1
b = 2
E = 0.04
N = 50

raiz, error, iteraciones = biseccion_sympy(f_expr, a, b, E, N)

print("\n📌 RESULTADO FINAL")
print(f"Raíz aproximada: {raiz:.6f}")
print(f"Error final: {error:.6f}")
print(f"Iteraciones realizadas: {iteraciones}")
