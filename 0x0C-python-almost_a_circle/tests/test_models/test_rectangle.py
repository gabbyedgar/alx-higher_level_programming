#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
import sys
import os
import json
from io import StringIO
from models.rectangle import Rectangle
from models.rectangle import __doc__ as module_doc
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Subclass of unittest.TestCase to test Rectangle class functionality"""
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
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIs(hasattr(Rectangle, "__init__"), True)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIs(hasattr(Rectangle, "width"), True)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIs(hasattr(Rectangle, "to_json_string"), True)
        self.assertIsNotNone(Rectangle.to_json_string.__doc__)
        self.assertIs(hasattr(Rectangle, "from_json_string"), True)
        self.assertIsNotNone(Rectangle.from_json_string.__doc__)
        self.assertIs(hasattr(Rectangle, "save_to_file"), True)
        self.assertIsNotNone(Rectangle.save_to_file.__doc__)
        self.assertIs(hasattr(Rectangle, "load_from_file"), True)
        self.assertIsNotNone(Rectangle.load_from_file.__doc__)

    def test_id(self):
        """Test for id property. Set class variable __nb_object to 0 so id
        values are as expected"""
        Base._Base__nb_object = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(1, 1, id="9")
        r5 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, "9")
        self.assertEqual(r5.id, 3)
        Base._Base__nb_object = 0
        self.assertEqual(r5.id, 3)
        r6 = Rectangle(2, 2)
        self.assertEqual(r6.id, 1)

    def test_args_cnt(self):
        """Test correct number and type of arguments"""
        Base._Base__nb_object = 0
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(x=1, y=1)

    def test_raise(self):
        """Test that instances raise correct errors and messages for incorrect
        input values."""
        Base._Base__nb_object = 0
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, -2.4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.0, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(-10.3, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([3], 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 1.1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, x=float(0))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, 1.1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, y=float(0))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1, 3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test that area method returns correct values"""
        Base._Base__nb_object = 0
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        r4 = Rectangle(99999999999, 8888888888)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)
        self.assertEqual(r4.area(), 99999999999 * 8888888888)

    def test_display(self):
        """Test that display method prints correct output. Relies on
        redirecting stdout to StringIO instance for comparing with
        expected output. Wraps calls to display and comparison with
        stdout in try/finally in order to reset stdout to beginning of
        stream even if the test fails.
        """
        Base._Base__nb_object = 0
        r1 = Rectangle(4, 6)
        r1_out = "####\n" \
                 "####\n" \
                 "####\n" \
                 "####\n" \
                 "####\n" \
                 "####\n"
        r2 = Rectangle(2, 2)
        r2_out = "##\n" \
                 "##\n"
        try:
            r1.display()
            self.assertEqual(sys.stdout.getvalue(), r1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            r2.display()
            self.assertEqual(sys.stdout.getvalue(), r2_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_str(self):
        """Test that __str__ magic method produces correct output."""
        Base._Base__nb_object = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_offset(self):
        """Test that `display()` method correctly works with offset values.
        As with `test_display`, `test_display_offset` relies on stdout being
        redirected to a StringIO instance. See `test_display` for details.
        """
        Base._Base__nb_object = 0
        r1 = Rectangle(2, 3, 2, 2)
        r1_out = "\n" \
                 "\n" \
                 "  ##\n" \
                 "  ##\n" \
                 "  ##\n"
        r2 = Rectangle(3, 2, 1, 0)
        r2_out = " ###\n" \
                 " ###\n"
        try:
            r1.display()
            self.assertEqual(sys.stdout.getvalue(), r1_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            r2.display()
            self.assertEqual(sys.stdout.getvalue(), r2_out)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_update1(self):
        """Test that `update()` method works with *args unpacking"""
        Base._Base__nb_object = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(*[89])
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(*[89, 2])
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(*[89, 2, 3])
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(*[89, 2, 3, 4])
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(*[89, 2, 3, 4, 5])
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        with self.assertRaises(TypeError):
            r1.update(*[1, 1.1, 1, 1, 1])
        with self.assertRaises(TypeError):
            r1.update(*[1, "a"])
        with self.assertRaises(TypeError):
            r1.update(*[1, 1, 1.0])
        with self.assertRaises(TypeError):
            r1.update(*[1, 1, "a"])
        with self.assertRaises(TypeError):
            r1.update(*[1, 1, 1, [], 0])
        with self.assertRaises(TypeError):
            r1.update(*[1, 1, 1, 0, []])
        with self.assertRaises(ValueError):
            r1.update(*[1, 0])
        with self.assertRaises(ValueError):
            r1.update(*[1, 1, 0])
        with self.assertRaises(ValueError):
            r1.update(*[1, 1, 1, -1, 1])
        with self.assertRaises(ValueError):
            r1.update(*[1, 1, 1, 1, -1])

    def test_update2(self):
        """Test that `update()` method works with **kwargs unpacking."""
        Base._Base__nb_object = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(**{'height': 1})
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(**{'width': 1, 'x': 2})
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(**{'y': 1, 'width': 2, 'x': 3, 'id': 89})
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(**{'x': 1, 'height': 2, 'y': 3, 'width': 4})
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        r1.update(**{'wow': 3, 'hey': 'wow'})
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        r1.update({'x': 10, 'height': 8})
        self.assertIs(type(r1.id), dict)

    def test_to_dict(self):
        """Test that `to_dictionary()` method produces valid dictionary
        representation of Rectangle instance. Converts to dictionary and
        updates distinct instance to those values and compares the two
        resulting objects to show that they have the same attributes but
        are not identical objects.
        """
        Base._Base__nb_object = 0
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertEqual(r1.to_dictionary(), {'x': 1, 'y': 9,
                                              'id': 1, 'height': 2,
                                              'width': 10})
        self.assertIs(type(r1.to_dictionary()), dict)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r1.to_dictionary())
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertNotEqual(r1, r2)

    def test_save_to_file(self):
        """Test that `save_to_file()` method of Rectangle instance
        can be used to directly serialize and write to a file. Removes
        file after test if test was able to write to disk.
        """
        Base._Base__nb_object = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertIs(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[{"y": 8, '
                                        '"x": 2, '
                                        '"id": 1, '
                                        '"width": 10, '
                                        '"height": 7}, '
                                        '{"y": 0, '
                                        '"x": 0, '
                                        '"id": 2, '
                                        '"width": 2, '
                                        '"height": 4}]'))
        os.remove("Rectangle.json")

    def test_save_to_file_none(self):
        """Test that `save_to_file()` method of Rectangle instance
        can be used to directly serialize and write to a file. Removes
        file after test if test was able to write to disk.
        """
        Base._Base__nb_object = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file(None)
        self.assertIs(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[]'))
        os.remove("Rectangle.json")

    def test_save_to_file_mt_list(self):
        """Test that `save_to_file()` method of Rectangle instance
        can be used to directly serialize and write to a file. Removes
        file after test if test was able to write to disk.
        """
        Base._Base__nb_object = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([])
        self.assertIs(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(json.loads(f.read()),
                             json.loads('[]'))
        os.remove("Rectangle.json")

    def test_load_from_file(self):
        """Test load from file if file non-existent"""
        self.assertEqual(Rectangle.load_from_file(), [])
        Base._Base__nb_object = 0
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        Rectangle.save_to_file([r1, r2])
        Base._Base__nb_object = 0
        rlist = Rectangle.load_from_file()
        self.assertEqual(rlist[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(rlist[1].to_dictionary(), r2.to_dictionary())
