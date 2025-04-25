from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+mysqlconnector://username:password@localhost:3306/resort_booking"

engine = create_engine(DATABASE_URL)

db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
