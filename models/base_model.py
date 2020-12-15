#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """
        Arguments
          - *args: is a Tuple that contains all arguments (won’t be used).
          - **kwargs: is a dictionary that contains all arguments by key/value.
        Functions/methods:
          - strptime(): creates a datetime object from the given instance.
          - setattr(): sets the value of the attribute of an object.
        """

        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    pass
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.
                            strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def _str_(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self._dict_)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self._dict_)
        dictionary.update({'_class_':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
