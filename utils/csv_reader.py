""" Docstring for the csv_reader.py module.
This module provides a utility function for parsing CSV files into lists of dataclass instances.

It is particularly useful for reading structured data from CSV files and automatically mapping
that data into typed Python dataclasses, with basic support for type conversion of standard
primitive types (int, float, bool, str).
Example:
>>> @dataclass
... class Person:
...     id: int
...     name: str
...     age: int
...
>>> people = parse_csv_to_dataclass_dict("people.csv", Person, delimiter=",")
>>> print(people[0].name)
John Doe
"""
import csv
import enum
from dataclasses import fields, is_dataclass
from typing import Type, TypeVar, List


T = TypeVar('T')


def parse_csv_to_dataclass_dict(filepath: str, cls: Type[T], delimiter: str) -> dict[int, T]:
    """
    Parses a CSV file into a list of instances of the given dataclass.

    This function reads a CSV file where each row represents an instance of a dataclass,
    and converts the data into typed instances of the specified dataclass `cls`.

    The function supports basic type conversion for `int`, `float`, `bool`, and `str`.
    Boolean fields are considered `True` if the value is one of: 'true', '1', or 'yes'
    (case-insensitive); otherwise, they are `False`.

    Args:
        filepath (str): The path to the CSV file to read.
        cls (Type[T]): The dataclass type to instantiate from each CSV row.
        delimiter (str): The delimiter used in the CSV file (e.g., ',', ';', '\t').

    Returns:
        List[T]: A list of dataclass instances created from the CSV data.
    """
    if not is_dataclass(cls):
        raise ValueError(f"{cls} must be a dataclass type")

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        result = {}
        cls_fields = {f.name: f.type for f in fields(cls)}

        for row in reader:
            kwargs = {}
            for key, value in row.items():
                if key in cls_fields:
                    field_type = cls_fields[key]
                    try:
                        if isinstance(field_type, type) and issubclass(field_type, enum.Enum):
                            kwargs[key] = field_type(int(value))
                        elif field_type == int:
                            kwargs[key] = int(value)
                        elif field_type == float:
                            kwargs[key] = float(value)
                        elif field_type == bool:
                            kwargs[key] = value.lower() in ('true', '1', 'yes')
                        else:
                            kwargs[key] = value
                    except Exception as e:
                        raise ValueError(f"Error converting field '{key}' to {field_type}: {e}") from e
            cls_object = cls(**kwargs)
            if not hasattr(cls_object, 'id'):
                raise ValueError(f"Dataclass {cls.__name__} must have an 'id' field to use as key")
            result[cls_object.id] = cls_object
        return result
