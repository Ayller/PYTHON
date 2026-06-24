from flask import Blueprint, redirect, render_template, request, url_for

from models import Filme, Sala, Sessao, db

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")


@cinema_bp.route("/")
def index():
    sessoes = Sessao.listar_com_detalhes()
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()

    if request.method == "POST":
        try:
            filme_id = int(request.form.get("filme_id", 0))
            sala_id = int(request.form.get("sala_id", 0))
            preco = float(request.form.get("preco", 0))
        except ValueError:
            return render_template(
                "cinema/formulario_sessao.html",
                filmes=filmes,
                salas=salas,
                erro="Valores inválidos.",
            )

        data_hora_str = request.form.get("data_hora", "").strip()
        if not filme_id or not sala_id or not data_hora_str:
            return render_template(
                "cinema/formulario_sessao.html",
                filmes=filmes,
                salas=salas,
                erro="Todos os campos são obrigatórios.",
            )

        from datetime import datetime
        data_hora = datetime.fromisoformat(data_hora_str)

        if not db.session.get(Filme, filme_id) or not db.session.get(Sala, sala_id):
            return render_template(
                "cinema/formulario_sessao.html",
                filmes=filmes,
                salas=salas,
                erro="Filme ou sala inválidos.",
            )

        Sessao.criar(filme_id, sala_id, data_hora, preco)
        return redirect(url_for("cinema.index"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
