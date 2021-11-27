#!/usr/bin/python3
"""Unittests for testing the User class """



from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """  """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.dict = {'email': "test@test.net", 'password': "test_password",
                     'first_name': "", 'last_name': ""}

    def test_first_name(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.password), str)
