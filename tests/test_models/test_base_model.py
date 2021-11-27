#!/usr/bin/python3
"""unitest for testing BaseModel class """
from models import BaseModel, City, Place, State, User
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Unittests for testing the basemodel class """

    def __init__(self, *args, **kwargs):
        """init for base model test """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
        self.dict = {}
        self.state = State(**{'name': "test_state"})
        self.city = City(**{'state_id': self.state.id, 'name': "test_city"})
        self.user = User(**{'email': "test@test.net",
                            'password': "test_password"})
        self.place = Place(**{'city_id': self.city.id, 'user_id': self.user.id,
                              'description': "", 'latitude': 0.0,
                              'longitude': 0.0, 'name': 'test_place'})

    def setUp(self):
        """set up """
        pass

    def tearDown(self):
        """ tear down"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test default values of instance """
        i = self.value(**self.dict)
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test creation of an instance with dictionary """
        i = self.value(**self.dict)
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test method dictionary and update method """
        i = self.value(**self.dict)
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db'
                     "test relies on filestorage")
    def test_save(self):
        """ Testing save """
        i = self.value(**self.dict)
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Check str format """
        i = self.value(**self.dict)
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test to_dict method """
        i = self.value(**self.dict)
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test dictionary with none arguments """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test dictionary with arguments """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
        new = self.value(**n)
        self.assertIsInstance(new, self.value)

    def test_id(self):
        """Test id of the instant """
        new = self.value(**self.dict)
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test creation of the instance """
        new = self.value(**self.dict)
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test update method """
        new = self.value(**self.dict)
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
