from models import Filme, Sala, Sessao, db


class SessaoService:
    @staticmethod
    def listar():
        return [SessaoService.to_dict(sessao) for sessao in Sessao.listar_com_detalhes()]

    @staticmethod
    def buscar_por_id(sessao_id):
        sessao = db.session.get(Sessao, sessao_id)
        return SessaoService.to_dict(sessao) if sessao else None

    @staticmethod
    def criar(filme_id, sala_id, data_hora, preco):
        if not db.session.get(Filme, filme_id) or not db.session.get(Sala, sala_id):
            return None
        sessao = Sessao.criar(filme_id, sala_id, data_hora, preco)
        return SessaoService.to_dict(sessao)

    @staticmethod
    def to_dict(sessao):
        return {
            "id": sessao.id,
            "filme_id": sessao.filme_id,
            "filme": sessao.filme.titulo,
            "sala_id": sessao.sala_id,
            "sala": sessao.sala.numero,
            "data_hora": sessao.data_hora.isoformat(),
            "preco": sessao.preco,
        }
