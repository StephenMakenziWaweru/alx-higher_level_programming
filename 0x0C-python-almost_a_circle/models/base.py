#!/usr/bin/python3
"""Base class module"""
import json
import csv


class Base():
    """Base class"""
    ___nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.___nb_objects += 1
            self.id = Base.___nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string rep of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string rep of list_objs to .json file"""
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionaries from json string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """loads instance attributes from .json file and creates instances"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes list_objs to csv file"""
        if list_objs is not None:
            if cls.__name__ == "Rectangle":
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            elif cls.__name__ == "Square":
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
            with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """loads instance attributes from csv file and creates instances"""
        ret = []
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for obj in reader:
                    v = [eval(i) for i in obj]
                    if cls.__name__ == "Rectangle":
                        dct = {"id": v[0], "width": v[1], "height": v[2],
                               "x": v[3], "y": v[4]}
                    elif cls.__name__ == "Square":
                        dct = {"id": v[0], "size": v[1], "x": v[2], "y": v[3]}
                    ret.append(cls.create(**dct))
            return ret
        except FileNotFoundError:
            return ret
