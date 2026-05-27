import math
from flask import render_template, request


def calcular():
    try:
        num1 = float(request.form["num1"])
    except (ValueError, KeyError):
        return render_template("calculadora.html", etapas="Informe um número válido.", resultados="")

    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            etapas = f"Não existe raiz real de {num1}."
            resultado = "Erro"
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    elif operacao == "log":
        if num1 <= 0:
            return render_template("calculadora.html", etapas="Erro: logaritmo indefinido para número ≤ 0.", resultados="")
        resultado = math.log(num1)
        etapas = f"ln({num1}) = {resultado}"

    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template("calculadora.html", etapas="Informe o segundo número para esta operação.", resultados="")
        try:
            num2 = float(num2_valor)
        except ValueError:
            return render_template("calculadora.html", etapas="Segundo número inválido.", resultados="")

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2} = {resultado}"
        elif operacao == "/":
            if num2 == 0:
                return render_template("calculadora.html", etapas="Erro: divisão por zero.", resultados="")
            resultado = num1 / num2
            etapas = f"{num1} ÷ {num2} = {resultado}"
        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ^ {num2} = {resultado}"
        else:
            return render_template("calculadora.html", etapas="Operação inválida.", resultados="")

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)
