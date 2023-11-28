def minimos_quadrados(x_values, y_values):
    # Número de pontos
    n = len(x_values)

    # Somatório de x, y, xy, x^2 e x^3
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(xi * yi for xi, yi in zip(x_values, y_values))
    sum_x_squared = sum(xi ** 2 for xi in x_values)
    sum_x_cubed = sum(xi ** 3 for xi in x_values)

    # Coeficientes a, b e c
    denominator = n * sum_x_squared - sum_x ** 2
    a = (n * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y - a * sum_x) / n
    c = (sum_x_squared * sum_y - sum_x * sum_xy) / denominator

    return a, b, c


def main():
    # Número de pontos
    num_points = int(input("Informe o número de pontos: "))

    # Listas para armazenar os valores de x e y
    x_values = [0] * num_points
    y_values = [0] * num_points

    # Entrada dos valores de x e y
    for i in range(num_points):
        x_values[i] = float(input(f"Informe o valor do ponto x[{i + 1}]: "))
        y_values[i] = float(input(f"Informe o valor do ponto y[{i + 1}]: "))

    # Cálculo dos coeficientes usando o método dos mínimos quadrados
    coefficients = minimos_quadrados(x_values, y_values)

    # Saída dos coeficientes e da fórmula de y
    print(f"Coeficiente a: {coefficients[0]}")
    print(f"Coeficiente b: {coefficients[1]}")
    print(f"Coeficiente c: {coefficients[2]}")
    print(f"Fórmula de y: y = {coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]}")


if __name__ == "__main__":
    main()
