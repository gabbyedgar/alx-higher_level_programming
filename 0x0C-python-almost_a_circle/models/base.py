#!/usr/bin/python3
"""Module to represent Base object to be extended by Square and Rectangle"""
import json
import csv


class Base:
    """Base class to be subclassed by Square and Rectangle"""

    __nb_object = 0
    """Class variable representing the total count of Base (and subclass)
    instances.
    """

    def __init__(self, id=None):
        """Initialize new Base instance

        Args:
            id: Identifier for instance. If None, use current object count.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @classmethod
    def create(cls, **dictionary):
        """Method to create new instance directly from the class. Mainly
        for use by subclasses of Base.

        Args:
            dictionary (dict): Dictionary of attributes, value pairs
                with which to set attributes for new instance.

        Returns: New instance of class from which `create` was called.

        Raises: Errors delegated to subclasses of Base which call this
            method.
        """
        if cls.__name__ == "Rectangle":
            c = cls(1, 1)
        elif cls.__name__ == "Square":
            c = cls(1)
        else:
            c = cls()
        if not hasattr(dictionary, "keys") or not callable(dictionary.keys):
            dictionary = {}
        c.update(**dictionary)
        return c

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to serialize list of dictionary objects into json.

        Args:
            list_dictionaries (list of dicts): List of dictionaries
                of attribute, value pairs for serialization into json
                representation.

        Returns: Json string representation of `list_dictionaries`.

        Raises: Any errors encounterd during serialization.
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Static method to deserialize json string into python objects.

        Args:
            json_string (str): String representation of objects.

        Returns: Python objects represented by `json_string`.

        Raises: Any errors encountered during serialization.
        """
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method to convert `list_objs` to json string and
        save in file with name '<class name>.json'.

        Args:
            list_objs (list): list of objects of class from which
                this method is called.

        Raises: Any errors encountered during serialization and I/O.
        """
        if not list_objs:
            list_objs = []
        with open("{}.json".format(cls.__name__), 'w') as jf:
            jf.write(cls.to_json_string([obj.to_dictionary() for
                                         obj in list_objs]))

    @classmethod
    def load_from_file(cls):
        """Class method to load file containing json serialized objects.
        Attempts to open file named '<class name>.json' and deserialize
        it. If it does not exist, returns empty list.
        """
        try:
            with open("{:s}.json".format(cls.__name__), 'r') as jf:
                list_dictionaries = cls.from_json_string(jf.read())
                return [cls.create(**d) for d in list_dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method to convert `list_objs` to csv format and save
        in file with name '<class name>.csv'.

        Args:
            list_objs (list): list of objects of class from which
                this method is called.

        Raises: Any error encounterd during conversion to csv.
        """
        if not list_objs:
            list_objs = []
        with open("{}.csv".format(cls.__name__), 'w') as csvf:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            else:
                fieldnames = ['id']
            writer = csv.DictWriter(csvf, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Class method to load file containing csv representation of objects.
        Attempts to open file named '<class name>.csv' and convert back to
        original list of objects. If it does not exist, returns empty list.
        """
        try:
            with open("{}.csv".format(cls.__name__), 'r') as csvf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fieldnames = ['id', 'size', 'x', 'y']
                else:
                    fieldnames = ['id']
                reader = csv.DictReader(csvf, fieldnames=fieldnames)
                list_objs = []
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    list_objs.append(cls.create(**row))
                return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles onto the screen using Tkinter and the
        Turtle drawing library.

        Args:
            list_rectangles (list): list of Rectangle instances
        """
        try:
            import turtle
            import random
        except ImportError("Turtle drawing library not available") as e:
            print("[{}]: {}".format(e.__class__.__name__, e))
            for r in list_rectangles:
                print(r, ':')
                r.display()
            print()
            for s in list_squares:
                print(s, ':')
                s.display()
        else:
            max_width = max(max(map(lambda r: r.width, list_rectangles)),
                            max(map(lambda s: s.size, list_squares)))
            max_width_off = max(max(map(lambda r: r.x, list_rectangles)),
                                max(map(lambda s: s.x, list_squares)))
            max_max_width = max_width + max_width_off
            max_height = max(max(map(lambda r: r.height, list_rectangles)),
                             max(map(lambda s: s.size, list_squares)))
            max_height_off = max(max(map(lambda r: r.y, list_rectangles)),
                                 max(map(lambda s: s.y, list_squares)))
            max_max_height = max_height + max_height_off
            max_max_max = max(max_max_width,
                              max_max_height)
            max_len = max(len(list_rectangles), len(list_squares))
            win = turtle.Screen()
            aspect_ratio = 3*max_max_height/(max_max_width*(max_len+1))
            print(aspect_ratio)
            win.setup(width=800, height=int(800*aspect_ratio))
            win.setworldcoordinates(0,
                                    3*max_max_height,
                                    max_max_width*(max_len+1),
                                    0)
            turt = turtle.Turtle()
            turt.hideturtle()
            turt.penup()
            turt.pensize(3)
            turt.color('green', 'blue')
            turt.goto(0, max_max_height/3)
            for i, rect in enumerate(list_rectangles):
                turt.setx(i*max_max_width + (i+1)*max_max_width/(max_len + 1))
                turt.pendown()
                turt.write(rect.__str__())
                turt.dot()
                off_heading = turt.towards(turt.xcor() + rect.x,
                                           turt.ycor() + rect.y)
                curr_heading = turt.heading()
                turt.setheading(off_heading)
                turt.goto(turt.xcor() + rect.x, turt.ycor() + rect.y)
                turt.setheading(curr_heading)
                turt.begin_fill()
                for _ in range(2):
                    turt.forward(rect.width)
                    turt.right(-90)
                    turt.forward(rect.height)
                    turt.right(-90)
                turt.end_fill()
                turt.penup()

            turt.goto(0, 5*max_max_height/3)
            turt.color('orange', 'purple')
            for j, square in enumerate(list_squares):
                turt.setx(j*max_max_width + (j+1)*max_max_width/(max_len + 1))
                turt.pendown()
                turt.write(square.__str__())
                turt.dot()
                off_heading = turt.towards(turt.xcor() + square.x,
                                           turt.ycor() + square.y)
                curr_heading = turt.heading()
                turt.setheading(off_heading)
                turt.goto(turt.xcor() + square.x, turt.ycor() + square.y)
                turt.setheading(curr_heading)
                turt.begin_fill()
                for _ in range(4):
                    turt.forward(square.size)
                    turt.right(-90)
                turt.end_fill()
                turt.penup()
            win.exitonclick()
