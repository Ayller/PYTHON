from models import Sala, db


class SalaService:
    @staticmethod
    def listar():
        return [SalaService.to_dict(sala) for sala in Sala.listar()]

    @staticmethod
    def buscar_por_id(sala_id):
        sala = db.session.get(Sala, sala_id)
        return SalaService.to_dict(sala) if sala else None

    @staticmethod
    def criar(numero, capacidade):
        sala = Sala(numero=numero, capacidade=capacidade)
        db.session.add(sala)
        db.session.commit()
        return SalaService.to_dict(sala)

    @staticmethod
    def to_dict(sala):
        return {
            "id": sala.id,
            "numero": sala.numero,
            "capacidade": sala.capacidade,
        }
