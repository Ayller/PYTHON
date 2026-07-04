from models import Filme, db


class FilmeService:
    @staticmethod
    def listar():
        return [FilmeService.to_dict(filme) for filme in Filme.listar()]

    @staticmethod
    def buscar_por_id(filme_id):
        filme = db.session.get(Filme, filme_id)
        return FilmeService.to_dict(filme) if filme else None

    @staticmethod
    def criar(titulo, duracao_min, classificacao):
        filme = Filme(titulo=titulo, duracao_min=duracao_min, classificacao=classificacao)
        db.session.add(filme)
        db.session.commit()
        return FilmeService.to_dict(filme)

    @staticmethod
    def to_dict(filme):
        return {
            "id": filme.id,
            "titulo": filme.titulo,
            "duracao_min": filme.duracao_min,
            "classificacao": filme.classificacao,
        }
