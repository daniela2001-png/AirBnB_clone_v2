#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)
import os
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
from models.base_model import Base


class DBStorage():
    """
    New engine DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        constructor
        """
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        # will be localhost
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        connection = 'mysql+mysqldb://{}:{}@localhost/{}'
        self.__engine = create_engine(connection.format(
            user, pwd, db), pool_pre_ping=True)
        if (os.getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.
        If cls is None, queries all types of objects.
        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """
        add a new object to db
        """
        self.__session.add(obj)

    def save(self):
        """
        commit  the objetc to db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        # create tables into a db
        Base.metadata.create_all(self.__engine)
        # creamos el session object
        # expire_on_commmot = false >>> ignore the query sql
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """
        close session
        """
        self.__session.close()
