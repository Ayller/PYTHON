from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Janaína Duarte</li>
                <li><strong>Email:</strong> janainaduarte@cotemig.com.br</li>
                <li><strong>Telefone:</strong> (11) 99999-9999</li>
            </ul>

            <h2>Experiência Profissional</h2>
            <ul>
                <li><strong>Empresa:</strong> ABC Tech</li>
                <li><strong>Cargo:</strong> Desenvolvedor de Software</li>
                <li><strong>Período:</strong> Jan 2020 - Presente</li>
            </ul>
        </body>
        </html>
    """


@app.route("/decorator")
def decorator():
    return """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Decorator</title>
        </head>
        <body>
            <h1>O que é um Decorator em Python?</h1>

            <h2>O que é?</h2>
            <p>
                Um <strong>decorator</strong> é uma função que recebe outra função como argumento
                e retorna uma nova função com comportamento modificado, sem alterar o código original.
                Em Python, é representado pelo símbolo <code>@</code> antes da função.
            </p>

            <h2>Para que serve?</h2>
            <p>
                Serve para adicionar funcionalidades extras a uma função de forma simples e reutilizável,
                como autenticação, logging e controle de acesso.
            </p>

            <h2>Como é utilizado no Flask?</h2>
            <p>
                No Flask, o <code>@app.route()</code> mapeia uma URL a uma função Python.
                Quando o usuário acessa aquela URL, o Flask chama automaticamente a função associada.
            </p>
            <pre>
@app.route('/decorator')
def decorator():
    return 'Esta função foi mapeada para /decorator'
            </pre>
        </body>
        </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
