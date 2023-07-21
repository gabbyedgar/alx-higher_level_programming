#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
import sys
import os
import json
from io import StringIO
from models.square import Square
from models.square import __doc__ as module_doc
from models.base import Base


class TestSquare(unittest.TestCase):
    """Subclass of unittest.TestCase to test Square class functionality"""
    def setUp(self):
        """Redirect stdout to readable buffer to check output of
        methods relying on print function."""
        sys.stdout = StringIO()

    def tearDown(self):
        """Following test completion reassign true stdout file stream to
        sys.stdout so printing goes to the screen as before."""
        sys.stdout = sys.__stdout__

    def test_docstrings(self):
        """Test for existence of docstrings"""
        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Square.__doc__)
        self.assertIs(hasattr(Square, "__init__"), True)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIs(hasattr(Square, "size"), True)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIs(hasattr(Square, "__str__"), True)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIs(hasattr(Square, "update"), True)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIs(hasattr(Square, "to_dictionary"), True)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_normal_instantiation(self):
        """Test that normal usage does not raise an exception"""
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s4.id, 4)

    def test_args_cnt(self):
        """Test correct number and type of arguments"""
        Base._Base__nb_object = 0
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(x=1, y=1)

    def test_raise(self):
        """Test that instances raise correct errors and messages for incorrect
        input values."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10.0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(-10.3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([3])
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 1.1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, x=float(0))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, 1.1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 2, y=float(0))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -1, 3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 2, -1)

    def test_str(self):
        """Test that __str__ magic method produces correct output."""
        Base._Base__nb_object = 0
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s2.__str__(), "[Square] (2) 2/0 - 2")
        self.assertEqual(s3.__str__(), "[Square] (3) 1/3 - 3")

    def test_area(self):
        """Test that area method returns correct values"""
        Base._Base__nb_object = 0
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        s4 = Square(99999999999)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)
        self.assertEqual(s4.area(), 99999999999 ** 2)

    def test_display_offset(self):
        """Test that the `display()` method prints correct output and
        uses offset values when specified. Relies on redirecting stdout
        to StringIO instance for comparing with expected output.
        Wraps calls to display and comparison with stdout in try/finally
        in order to reset stdout to beginning of stream even if the test
        fails.
        """
        Base._Base__nb_object = 0
        s1 = Square(5)
        s1_out = "#####\n" \
                 "#####\n" \
                 "#####\n" \
                 "#####\n" \
                 "#####\n"

        s2 = Square(2, 2)
        s2_out = "  ##\n" \
                 "  ##\n"

        s3 = Square(3, 1, 3)
        s3_out = "\n\n\n" \
                 " ###\n" \
                 " ###\n" \
                 " ###\n"

        try:
            s1.display()
            self.assertEqual(sys.stdout.getvalue(), s1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            s2.display()
            self.assertEqual(sys.stdout.getvalue(), s2_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            s3.display()
            self.assertEqual(sys.stdout.getvalue(), s3_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_size(self):
        """Test that Square `size` attribute is set correctly"""
        Base._Base__nb_object = 0
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "9"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = 1.1
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = 0

    def test_update_args_kwargs(self):
        """Test that `update()` method correctly handles *args and **kwargs"""
        Base._Base__nb_object = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")
        with self.assertRaises(TypeError):
            s1.update(1, 1.1, 1, 1)
        with self.assertRaises(TypeError):
            s1.update(1, "a")
        with self.assertRaises(TypeError):
            s1.update(1, 1, [], 0)
        with self.assertRaises(TypeError):
            s1.update(1, 1, 0, [])
        with self.assertRaises(ValueError):
            s1.update(1, 0)
        with self.assertRaises(ValueError):
            s1.update(1, 1, -1, 1)
        with self.assertRaises(ValueError):
            s1.update(1, 1, 1, -1)
        s1.update(**{'wow': 3, 'hey': 'wow', 'id': 89})
        self.assertEqual(s1.__str__(), "[Square] (89) 1/1 - 1")
        s1.update({'x': 10, 'height': 8})
        self.assertIs(type(s1.id), dict)

    def test_to_dict(self):
        """Test that `to_dictionary()` method produces valid dictionary
        representation of Square instance. Converts to dictionary and
        updates distinct instance to those values and compares the two
        resulting objects to show that they have the same attributes but
        are not identical objects.
        """
        Base._Base__nb_object = 0
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/1 - 10")
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'x': 2,
                                              'size': 10, 'y': 1})
        self.assertIs(type(s1.to_dictionary()), dict)
        s2 = Square(1, 1)
        self.assertEqual(s2.__str__(), "[Square] (2) 1/0 - 1")
        s2.update(**s1.to_dictionary())
        self.assertEqual(s2.__str__(), "[Square] (1) 2/1 - 10")
        self.assertNotEqual(s1, s2)

    def test_create(self):
        """Test that create method from base works with square"""
        s1 = Square.create(**{'id': 89})
        s2 = Square.create(**{'id': 89, 'size': 1})
        s3 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        s4 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s4.y, 3)

    def test_save_to_file(self):
        """Test that `save_to_file()` method of Rectangle instance
        can be used to directly serialize and write to a file. Removes
        file after test if test was able to write to disk.
        """
        Base._Base__nb_object = 0
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([r1, r2])
        self.assertIs(os.path.exists("Square.json"), True)
        with open("Square.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[{"y": 8, '
                                        '"x": 2, '
                                        '"id": 1, '
                                        '"size": 10}, '
                                        '{"y": 0, '
                                        '"x": 0, '
                                        '"id": 2, '
                                        '"size": 2}]'))
        os.remove("Square.json")

    def test_save_to_file_none(self):
        """Test that `save_to_file()` method of Square instance
        can be used to directly serialize and write to a file. Removes
        file after test if test was able to write to disk.
        """
        Base._Base__nb_object = 0
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file(None)
        self.assertIs(os.path.exists("Square.json"), True)
        with open("Square.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[]'))
        os.remove("Square.json")

    def test_save_to_file_mt_list(self):
        """Test that `save_to_file()` method of Square instance
        can be used to directly serialize and write to a file. Removes
        file after test if test was able to write to disk.
        """
        Base._Base__nb_object = 0
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        Square.save_to_file([])
        self.assertIs(os.path.exists("Square.json"), True)
        with open("Square.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[]'))
        os.remove("Square.json")

    def test_load_from_file(self):
        """Test load from file if file non-existent"""
        self.assertEqual(Square.load_from_file(), [])
        Base._Base__nb_object = 0
        r1 = Square(1, 1, 1)
        r2 = Square(2, 2, 2)
        Square.save_to_file([r1, r2])
        Base._Base__nb_object = 0
        rlist = Square.load_from_file()
        self.assertEqual(rlist[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(rlist[1].to_dictionary(), r2.to_dictionary())
