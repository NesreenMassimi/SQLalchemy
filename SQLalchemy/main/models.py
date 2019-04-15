from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,DATE,DATETIME,Float
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()


engine = create_engine("mysql+pymysql://root:16001700@localhost/test")
Base = declarative_base()
#Session = sqlalchemy.orm.sessionmaker(bind=engine)
#session = Session()


class Post (Base):

    __tablename__ = 'post'
    id = Column(Integer, primary_key=True,autoincrement=True)
    content = Column(String(45))
    created = Column(DATE)
    updated = Column(DATE)
    speciality = Column(Integer,ForeignKey('speciality.id'),nullable=False)


class Speciality(Base):
    __tablename__ = 'speciality'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(45))
    code =Column(String(45),unique=True)
    created = Column(DATE)
    updated=Column(DATE)

class User(Base):
    __tablename__ = 'user'
    id=Column(Integer,primary_key=True,autoincrement=True)
    first_name = Column(String(45))
    last_name=Column(String(45))
    email=Column(String(45),unique=True)
    password=Column(String(60))
    user_type=Column(String(45))
    last_login=Column(DATETIME)
    created = Column(DATE)
    updated = Column(DATE)
    profile = relationship("UserProfile", uselist=False, backref=backref("user"))



class UserEducation(Base):
    __tablename__ = 'user_education'
    id=Column(Integer,primary_key=True,autoincrement=True)
    institution_name=Column(String(45))
    start_date = Column(DATE)
    end_date = Column(DATE)
    user = Column(Integer,ForeignKey("user.id"),nullable=False)
    created = Column(DATE)
    updated = Column(DATE)


class UserProfile(Base):
    __tablename__ = 'user_profile'
    id=Column(Integer,primary_key=True,autoincrement=True)
    weight = Column(Float)
    height = Column(Float)
    about = Column(String(60))
    license_number = Column(Integer)
    users = Column(Integer,ForeignKey("user.id"),nullable=False)
    created = Column(DATE)
    updated = Column(DATE)



Base.metadata.create_all(engine)






