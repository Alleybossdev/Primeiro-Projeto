from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# tabelas

class Usuario(Base):
    __tablename__ = "usuarios"

    id= Column("id", Integer, primary_key=True, autoincrement=True)
    nome= Column("nome", String)
    email= Column("email", String)
    senha= Column("senha", String)
    ativo= Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo



class Livro(Base):
    __tablename__ = "livros"

    id= Column("id", Integer, primary_key=True, autoincrement=True)
    titulo= Column("titulo", String)
    paginas= Column("paginas", Integer)
    dono= Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, paginas, dono):
        self.titulo = titulo
        self.paginas = paginas
        self.dono = dono

Base.metadata.create_all(bind=db)

#CRUD

usuario = Usuario(nome = "Gustavo", email="gcm@email.com", senha="123321")
session.add(usuario)
session.commit()
