#!/usr/bin/python3
"""Unittest module for the place class"""
import unittest
import os
import re
import json
import time
from datetime import datetime
from models.place import Place
from models.engine.file_storage import FileStorage
from models.base_models import BaseModel
from models import storage

class TestPlace(unittest.TestCase):
    """test cases for place class"""

    def setUp(self):
        """sets up the test methods"""
        pass
    def tearDown(self):
        """tears down the test methods"""
        self.resetStorage()
        pass
    def resetStorage(self):
        """resets filestorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage_file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Place class."""

        b = Place()
        self.assertEqual(str(type(b)), "<class 'models.place.Place'>")
        self.assertIsInstance(b, Place)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        o = Place()
        for key, value in attributes.items():
            self.assertTrue(hasattr(o, key))
            self.assertEqual(type(getattr(o, key, None)), value)


if __name__ == "__main__":
    unittest.main()