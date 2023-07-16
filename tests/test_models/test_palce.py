#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace_instantiation
    TestPlace_save
    TestPlace_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place
from contextlib import redirect_stdout
import io
import sys
import inspect


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args_instantiates(self):
        """Test no args instantiates"""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        """Test new instance stored in objects"""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test id is public str"""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Test created at is public datetime"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test updated at is public datetime"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        """Test city id is public class attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Test user id is public class attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)

    def test_name_is_public_class_attribute(self):
        """Test name is public class attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(pl))
        self.assertNotIn("name", pl.__dict__)

    def test_description_is_public_class_attribute(self):
        """Test description is public class attribute"""
        pl = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(pl))
        self.assertNotIn("desctiption", pl.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        """Test number rooms is public class attribute"""
        pl = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(pl))
        self.assertNotIn("number_rooms", pl.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        """Test number bathrooms is public class attribute"""
        pl = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(pl))
        self.assertNotIn("number_bathrooms", pl.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        """Test max guest is public class attribute"""
        pl = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(pl))
        self.assertNotIn("max_guest", pl.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        """Test price by night is public class attribute"""
        pl = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(pl))
        self.assertNotIn("price_by_night", pl.__dict__)

    def test_latitude_is_public_class_attribute(self):
        """Test latitude  is public class attribute"""
        pl = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(pl))
        self.assertNotIn("latitude", pl.__dict__)

    def test_longitude_is_public_class_attribute(self):
        """Test longitude is public class attribute"""
        pl = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(pl))
        self.assertNotIn("longitude", pl.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        """Test amenity ids is public class attribute"""
        pl = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(pl))
        self.assertNotIn("amenity_ids", pl.__dict__)

    def test_two_places_unique_ids(self):
        """Test two places unique ids"""
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    def test_two_places_different_created_at(self):
        """Test two places different created at"""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_two_places_different_updated_at(self):
        """Test two places different updated at"""
        pl1 = Place()
        sleep(0.05)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    def test_str_representation(self):
        """Test str representation"""
        dt = datetime.today()
        dt_repr = repr(dt)
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        plstr = pl.__str__()
        self.assertIn("[Place] (123456)", plstr)
        self.assertIn("'id': '123456'", plstr)
        self.assertIn("'created_at': " + dt_repr, plstr)
        self.assertIn("'updated_at': " + dt_repr, plstr)

    def test_args_unused(self):
        """Test args unused"""
        pl = Place(None)
        self.assertNotIn(None, pl.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation with kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        pl = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(pl.id, "345")
        self.assertEqual(pl.created_at, dt)
        self.assertEqual(pl.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None kwargs"""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUp(self):
        """Create storage file"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Remove storage file"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test one save"""
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        self.assertLess(first_updated_at, pl.updated_at)

    def test_two_saves(self):
        """Test two saves"""
        pl = Place()
        sleep(0.05)
        first_updated_at = pl.updated_at
        pl.save()
        second_updated_at = pl.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        pl.save()
        self.assertLess(second_updated_at, pl.updated_at)

    def test_save_with_arg(self):
        """Test save with arg"""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.save(None)

    def test_save_updates_file(self):
        """Test save updates file"""
        pl = Place()
        pl.save()
        plid = "Place." + pl.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test to dict type"""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test to dict contains correct keys"""
        pl = Place()
        self.assertIn("id", pl.to_dict())
        self.assertIn("created_at", pl.to_dict())
        self.assertIn("updated_at", pl.to_dict())
        self.assertIn("__class__", pl.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test to dict contains added attributes"""
        pl = Place()
        pl.middle_name = "Holberton"
        pl.my_number = 98
        self.assertEqual("Holberton", pl.middle_name)
        self.assertIn("my_number", pl.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test to dict datetime attributes are strs"""
        pl = Place()
        pl_dict = pl.to_dict()
        self.assertEqual(str, type(pl_dict["id"]))
        self.assertEqual(str, type(pl_dict["created_at"]))
        self.assertEqual(str, type(pl_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test to dict output"""
        dt = datetime.today()
        pl = Place()
        pl.id = "123456"
        pl.created_at = pl.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(pl.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test contrast to dict dunder dict"""
        pl = Place()
        self.assertNotEqual(pl.to_dict(), pl.__dict__)

    def test_to_dict_with_arg(self):
        """Test to dict with arg"""
        pl = Place()
        with self.assertRaises(TypeError):
            pl.to_dict(None)


class TestPlace(unittest.TestCase):
    """
    class for testing Place class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Place, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """set up method for place class
        """
        self.P = Place()

    def tearDown(self):
        """initialized method for place
        """
        self.P = None

    def test_type(self):
        """test method for type testing of place
        """
        self.assertIsInstance(self.P, Place)
        self.assertEqual(type(self.P), Place)
        self.assertEqual(issubclass(self.P.__class__, Place), True)
        self.assertEqual(isinstance(self.P, Place), True)

    def test_city_id_type(self):
        """tests the city_id class attributes type for Place
        """
        self.assertEqual(type(Place.city_id), str)

    def test_user_id_type(self):
        """tests the user_id class attributes type for Place
        """
        self.assertEqual(type(Place.user_id), str)

    def test_name_type(self):
        """tests the name class attributes type for Place
        """
        self.assertEqual(type(Place.name), str)

    def test_description_type(self):
        """tests the description class attributes type for Place
        """
        self.assertEqual(type(Place.description), str)

    def test_number_rooms_type(self):
        """tests the number_rooms class attributes type for Place
        """
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms_type(self):
        """tests the number_bathrooms class attributes type for Place
        """
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest_type(self):
        """tests the max_guest class attributes type for Place
        """
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night_type(self):
        """tests the price_by_night class attributes type for Place
        """
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude_type(self):
        """tests the latitude class attributes type for Place
        """
        self.assertEqual(type(Place.latitude), float)

    def test_longitude_type(self):
        """tests the longitude class attributes type for Place
        """
        self.assertEqual(type(Place.longitude), float)

    def test_basic_attribute_set(self):
        """test method for basic attribute assignment
        """
        self.P.first_name = 'Meco'
        self.P.last_name = 'Montes'
        self.assertEqual(self.P.first_name, 'Meco')
        self.assertEqual(self.P.last_name, 'Montes')

    def test_string_return(self):
        """tests the string method
        """
        string = str(self.P)
        Pid = "[{}] ({})".format(self.P.__class__.__name__,
                                 self.P.id)
        test = Pid in string
        self.assertEqual(True, test)
        test = "updated_at" in string
        self.assertEqual(True, test)
        test = "created_at" in string
        self.assertEqual(True, test)
        test = "datetime.datetime" in string
        self.assertEqual(True, test)

    def test_to_dict(self):
        """tests to_dict method
        """
        my_dict = self.P.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.P.created_at.isoformat())
        self.assertEqual(datetime, type(self.P.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.P.__class__.__name__)
        self.assertEqual(my_dict['id'], self.P.id)

    def test_to_dict_more(self):
        """tests to_dict method
        """
        my_dict = self.P.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.P.created_at, time)

    def test_from_dict_basic(self):
        """tests the from_dict method
        """
        my_dict = self.P.to_dict()
        P1 = self.P.__class__(**my_dict)
        self.assertEqual(P1.id, self.P.id)
        self.assertEqual(P1.updated_at, self.P.updated_at)
        self.assertEqual(P1.created_at, self.P.created_at)
        self.assertEqual(P1.__class__.__name__,
                         self.P.__class__.__name__)

    def test_from_dict_hard(self):
        """test from_dict method for class objects
        """
        self.P.name = 'Meco'
        self.P.amenity_ids = ['90870987907', '0897909', '987907']
        my_dict = self.P.to_dict()
        self.assertEqual(my_dict['name'], 'Meco')
        P1 = self.P.__class__(**my_dict)
        self.assertEqual(P1.created_at, self.P.created_at)
        self.assertEqual(type(P1.number_rooms), int)
        self.assertEqual(type(P1.number_bathrooms), int)
        self.assertEqual(type(P1.max_guest), int)
        self.assertEqual(type(P1.price_by_night), int)
        self.assertEqual(type(P1.latitude), float)
        self.assertEqual(type(P1.longitude), float)
        self.assertEqual(type(P1.amenity_ids), list)
        self.assertEqual(self.P.number_rooms, P1.number_rooms)
        self.assertEqual(self.P.number_bathrooms,
                         P1.number_bathrooms)
        self.assertEqual(self.P.max_guest, P1.max_guest)
        self.assertEqual(self.P.price_by_night, P1.price_by_night)
        self.assertEqual(self.P.latitude, P1.latitude)
        self.assertEqual(self.P.longitude, P1.longitude)

    def test_unique_id(self):
        """test for unique ids for class objects
        """
        P1 = self.P.__class__()
        P2 = self.P.__class__()
        self.assertNotEqual(self.P.id, P1.id)
        self.assertNotEqual(self.P.id, P2.id)

    def test_id_type_string(self):
        """test id of the class is a string
        """
        self.assertEqual(type(self.P.id), str)

    def test_updated_time(self):
        """test that updated time gets updated
        """
        time1 = self.P.updated_at
        self.P.save()
        time2 = self.P.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)


if __name__ == "__main__":
    unittest.main()
