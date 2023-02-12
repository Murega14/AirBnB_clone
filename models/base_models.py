#!/usr/bin/python3
"""BaseModel defines all the common methods and attributes"""
import uuid
from datetime import datetime
import models

class Basemodel:
    """base model class"""
    def __init__(self, *args, **kwargs):
        """class initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
    
    def __repr__(self):
        """returns the string function"""
        return self.__str__()
    
    def save(self):
        """saves class"""
        self.updated_at = datetime.now
        models.storage.save()

    def to_dict(self):
        
        