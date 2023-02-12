#!/usr/bin/python3
"""tests for class amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_models import BaseModel
import time
from datetime import datetime
import re
import json
from models import storage
from models.engine.file_storage import FileStorage

class TestAmenity(unittest.TestCase):
    """Test classes for the Amenity class"""
    def setup(self):
        """setting up test methods"""
        pass
    def tearDown(self):
        """Tears down test methods"""
        self.resetStorage()
        pass
    def resetStorage(self):
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of amenity class"""
        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of amenity class"""
        attributes = storage.attributes()["Amenity"]
        o = Amenity
        for key, value in attributes.items():
            self.assertTrue(hasattr(o, key))
            self.assertEqual(type(getattr(o, key, None)), value)


if __name__ == "__main__":
    unittest.main()
