#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    # NOTE: declare what the table name is
    __tablename__ = 'students'

    # NOTE: declare the columns
    id = Column(Integer(), primary_key=True)
    name = Column(String())


# NOTE: Still not sure what this is?
if __name__ == '__main__':
    # NOTE: declare what the database is
    engine = create_engine('sqlite:///students.db')
    # NOTE: create the databases
    Base.metadata.create_all(engine)
