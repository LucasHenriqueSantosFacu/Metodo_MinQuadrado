def regressao_linear_mmq(x_values, y_values):
    # Número de pontos
    n = len(x_values)

    # Soma dos valores de x, y, x² e xy
    soma_x = sum(x_values)
    soma_y = sum(y_values)
    soma_x2 = sum(x ** 2 for x in x_values)
    soma_xy = sum(x * y for x, y in zip(x_values, y_values))

    # Coeficientes da regressão linear (a e b)
    coeficiente_a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    coeficiente_b = (soma_y - coeficiente_a * soma_x) / n

    return coeficiente_a, coeficiente_b


# Valores de exemplo para a regressão linear
valores_x_exemplo = [-2, -1, 1, 3]
valores_y_exemplo = [-3, 0, 2, 6]

# Obtém os coeficientes da regressão linear
coeficiente_a, coeficiente_b = regressao_linear_mmq(valores_x_exemplo, valores_y_exemplo)

# Imprime a equação da reta resultante: f(x) = ax + b
print("Equação da Reta: f(x) = {:.4f}x + {:.4f}".format(coeficiente_a, coeficiente_b))
