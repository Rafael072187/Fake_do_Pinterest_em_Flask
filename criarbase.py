from Copia_do_Pinterest import app, database
from Copia_do_Pinterest.models import Usuario, Foto


def criar_banco():
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Banco de dados criado com sucesso em Copia_do_Pinterest/comunidade.db")

if __name__ == "__main__":
    criar_banco()

