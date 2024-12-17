from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, func, text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    ip_address = Column(String)
    #password = Column(String) #You will handle passwords separately and securely.

def get_db_session(db_url):
    engine = create_engine(db_url)
    session = scoped_session(sessionmaker(bind=engine))
    return session

def fetch_users(session, email=None, ip_address=None):
    query = session.query(User)
    if email:
        query = query.filter(User.email == email)
    if ip_address:
        query = query.filter(User.ip_address == ip_address)
    return query.all()
