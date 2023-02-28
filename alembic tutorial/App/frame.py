from sqlalchemy import create_engine as ce, Integer, Date, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Table, insert, create_engine, MetaData
from sqlalchemy import MetaData
from App.database.database import Base


class School(Base):
    __tablename__ = 'school'

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(VARCHAR(20))
    teachers_relationship = relationship('Teacher', backref='school')


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key = True)
    Name = Column(VARCHAR(28))
    department_name = Column(VARCHAR(30))
    department_id = Column(Integer)
    school_id = Column(Integer, ForeignKey('school.id'))
    School_relationship = relationship('School', backref='Teacher')
