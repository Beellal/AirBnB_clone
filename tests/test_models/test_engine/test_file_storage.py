#!/usr/bin/python3

import unittest
import os
import contextlib
import json
import models
import pep8

#class
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):
    def test_pep8_FileStorage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def setUp(self):
        """Set up test objects as needed."""
        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()
        if os.path.exists("file.json"):
            pass
        else:
            os.mknod("file.json")

    def tearDown(self):
        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test that all() returns a list of all objects."""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, self.storage._FileStorage__Objects)

    def storage_empty(self):
        """Test that all() returns an empty list if no objects."""
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """Test that all() returns a dictionary."""
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """Test that new() adds an object to the storage."""
        obj = self.storage.all()
        self.u1.id = 1234
        self.u1.name = "Julien"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """Test that json file is loaded."""
        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))

if __name__ == '__mane__':
    unittest.main()