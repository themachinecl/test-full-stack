import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres:postgres@localhost/postgresql"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
# sqlacodegen --schema public postgresql://postgres:postgres@localhost:5432/postgres > models2.py //  task create MODEL
