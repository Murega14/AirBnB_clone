#!/usr/bin/python3
"""Unittest module for the city class"""
import unittest
from datetime import datetime
import time
import re
import json
import os
from models.city import City
from models import storage
from models.engine.file_storage import FileStorage
from models.base_models import BaseModel

class TestCity(unittest.TestCase):
    """Test cases for the city class"""

    def setUp(self):
        """sets up the test methods"""
        pass
    def tearDown(self):
        """Tears down the test methods"""
        self.resetStorage()
        pass
    def resetStorage(self):
        """Resets filestorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage_file_path):
            os.remove(FileStorage._FileStorage_file_path)

    def test_8_instantiation(self):
        """tests instantiation of class City"""
        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Test attributes of the class City"""
        attributes = storage.attributes()["City"]
        o = City()
        for key, value in attributes.items():
            self.assertTrue(hasattr(o, key))
            self.assertEqual(type(getattr(o, key, None)), value)


if __name__ == "__main__":
    unittest.main()