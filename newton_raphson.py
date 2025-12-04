from sympy import symbols, diff, lambdify, sympify

def newton_raphson(f_expr, X_0, E, N):
    """
    Método de Newton-Raphson para encontrar una raíz de f(x).

    Parámetros:
    - f_expr: expresión simbólica de la función f(x)
    - X_0: valor inicial
    - E: cota de error (E > 0)
    - N: número máximo de iteraciones (1 ≤ N ≤ 5)

    Retorna:
    - Xi: aproximación de la raíz
    - error: diferencia entre iteraciones
    - iteraciones: número de iteraciones realizadas
    """


    # Validaciones estrictas
    if not hasattr(f_expr, 'subs'):
        raise TypeError("❌ f_expr debe ser una expresión simbólica de SymPy.")
    if not isinstance(X_0, (int, float)):
        raise TypeError("❌ X_0 debe ser un número.")
    if not isinstance(E, (int, float)) or E <= 0:
        raise ValueError("❌ E debe ser positivo.")
    if not isinstance(N, int) or not (1 <= N <= 50):
        raise ValueError("❌ N debe estar entre 1 y 50.")

    x = symbols('x')
    f_func = lambdify(x, f_expr)
    f_prime_func = lambdify(x, diff(f_expr, x))
    f_second_func = lambdify(x, diff(f_expr, x, 2))

    # Verificación de convergencia
    conv_test = abs((f_func(X_0) * f_second_func(X_0)) / (f_prime_func(X_0)**2))
    print("📝 ENUNCIADO DEL EJERCICIO")
    print(f"Aproximar la raíz de la función f(x) = {f_expr}")
    print(f"mediante el método de Newton-Raphson, iniciando en X₀ = {X_0},")
    print(f"hasta que el error relativo sea menor a {E}, con un máximo de {N} iteraciones.\n")

    print("📘 FORMULAS USADAS")
    print("x_{i+1} = x_i - f(x_i)/f'(x_i)")
    print("Error = |(x_i - x_{i+1})/x_i|\n")

    print("📊 TABLA DE ITERACIONES")
    print(f"{'i':<5}{'x_i':<12}{'x_i+1':<12}{'Error':<12}")
    print("-"*45)

    if conv_test >= 1:
        print(f"⚠️ El método puede no converger porque |(f(x0)*f''(x0))/(f'(x0)^2)| = {conv_test:.6f} ≥ 1\n")

    Xi = X_0
    for i in range(1, N + 1):
        f_val = f_func(Xi)
        f_prime_val = f_prime_func(Xi)

        if f_prime_val == 0:
            raise ZeroDivisionError(f"⚠️ Derivada cero en Xi = {Xi:.6f}. Método falla.")

        Xi_new = Xi - f_val / f_prime_val
        error = abs((Xi - Xi_new) / Xi)

        print(f"{i:<5}{Xi:<12.6f}{Xi_new:<12.6f}{error:<12.6f}")

        if error < E:
            print("\n✅ Criterio de convergencia alcanzado.")
            return Xi_new, error, i

        Xi = Xi_new

    print("\n⚠️ Se alcanzó el número máximo de iteraciones sin cumplir la cota de error.")
    return Xi, error, N


# 🧪 Ejemplo de uso
f_expr = sympify("(x - 2)**2 - log(x)")
X_0 = 1.5
E = 0.02
N = 5

raiz, error, iteraciones = newton_raphson(f_expr, X_0, E, N)

print("\n📌 RESULTADO FINAL")
print(f"Raíz aproximada: {raiz:.6f}")
print(f"Error final: {error:.6f}")
print(f"Iteraciones realizadas: {iteraciones}")

# 🔍 Comprobación final
f_val_final = lambdify(symbols('x'), f_expr)(raiz)
print("\n🔍 COMPROBACIÓN FINAL")
print(f"f({raiz:.6f}) = {f_val_final:.6f}")
if abs(f_val_final) < E:
    print("✅ La raíz cumple con la cota de error establecida.")
else:
    print("⚠️ La raíz no cumple con la cota de error. Revisar parámetros o aumentar iteraciones.")
