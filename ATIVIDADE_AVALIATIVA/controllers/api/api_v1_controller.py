from datetime import datetime

from flask import Blueprint, jsonify, request

from services import FilmeService, SalaService, SessaoService

api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")


@api_v1_bp.route("/filmes", methods=["GET"])
def listar_filmes():
    return jsonify(FilmeService.listar()), 200


@api_v1_bp.route("/filmes/<int:filme_id>", methods=["GET"])
def buscar_filme(filme_id):
    filme = FilmeService.buscar_por_id(filme_id)
    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404
    return jsonify(filme), 200


@api_v1_bp.route("/filmes", methods=["POST"])
def criar_filme():
    dados = request.get_json(silent=True) or {}
    titulo = dados.get("titulo")
    duracao_min = dados.get("duracao_min")
    classificacao = dados.get("classificacao")

    if not titulo or not duracao_min or not classificacao:
        return jsonify({"erro": "titulo, duracao_min e classificacao são obrigatórios"}), 400

    filme = FilmeService.criar(titulo, duracao_min, classificacao)
    return jsonify(filme), 201


@api_v1_bp.route("/salas", methods=["GET"])
def listar_salas():
    return jsonify(SalaService.listar()), 200


@api_v1_bp.route("/salas/<int:sala_id>", methods=["GET"])
def buscar_sala(sala_id):
    sala = SalaService.buscar_por_id(sala_id)
    if not sala:
        return jsonify({"erro": "Sala não encontrada"}), 404
    return jsonify(sala), 200


@api_v1_bp.route("/salas", methods=["POST"])
def criar_sala():
    dados = request.get_json(silent=True) or {}
    numero = dados.get("numero")
    capacidade = dados.get("capacidade")

    if not numero or not capacidade:
        return jsonify({"erro": "numero e capacidade são obrigatórios"}), 400

    sala = SalaService.criar(numero, capacidade)
    return jsonify(sala), 201


@api_v1_bp.route("/sessoes", methods=["GET"])
def listar_sessoes():
    return jsonify(SessaoService.listar()), 200


@api_v1_bp.route("/sessoes/<int:sessao_id>", methods=["GET"])
def buscar_sessao(sessao_id):
    sessao = SessaoService.buscar_por_id(sessao_id)
    if not sessao:
        return jsonify({"erro": "Sessão não encontrada"}), 404
    return jsonify(sessao), 200


@api_v1_bp.route("/sessoes", methods=["POST"])
def criar_sessao():
    dados = request.get_json(silent=True) or {}
    try:
        filme_id = int(dados.get("filme_id", 0))
        sala_id = int(dados.get("sala_id", 0))
        preco = float(dados.get("preco", 0))
    except (TypeError, ValueError):
        return jsonify({"erro": "Valores inválidos"}), 400

    data_hora_str = dados.get("data_hora", "")
    if not filme_id or not sala_id or not data_hora_str:
        return jsonify({"erro": "filme_id, sala_id e data_hora são obrigatórios"}), 400

    try:
        data_hora = datetime.fromisoformat(data_hora_str)
    except ValueError:
        return jsonify({"erro": "data_hora inválida, use o formato ISO 8601"}), 400

    sessao = SessaoService.criar(filme_id, sala_id, data_hora, preco)
    if not sessao:
        return jsonify({"erro": "Filme ou sala inválidos"}), 400

    return jsonify(sessao), 201


@api_v1_bp.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "API está funcionando"}), 200
