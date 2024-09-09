from sqlalchemy.orm import Session
from .models import User, engine, Base, SessionLocal, pwd_context

def init_db():
    # Cria todas as tabelas
    Base.metadata.create_all(bind=engine)

    # Cria uma sessão de banco de dados
    db = SessionLocal()
    
    try:
        # Verifica se já existe um usuário com o nome 'teste'
        if not db.query(User).filter(User.username == "teste").first():
            # Cria um novo usuário com o nome 'teste' e senha 'teste'
            hashed_password = pwd_context.hash("teste")
            new_user = User(username="teste", hashed_password=hashed_password)
            db.add(new_user)
            db.commit()
            print("Usuário 'teste' criado com sucesso.")
        else:
            print("Usuário 'teste' já existe.")
    finally:
        db.close()

# if __name__ == "__main__":
#     init_db()
