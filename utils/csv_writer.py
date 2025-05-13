"""This module provides functionality to serialize a list of Python objects (e.g., dataclass instances)
to a CSV file using the standard `csv` module."""
import csv
from typing import Iterable


def write_objects_to_csv(filename: str, objects: Iterable):
    """
    Writes a list of objects (typically dataclass instances) to a CSV file.

    Each object's attributes are extracted using `vars()` and written as a row in the CSV file.
    All objects must have the same attributes (i.e., same set of keys from `vars()`).

    Args:
        filename (str): The path to the CSV file to write.
        objects (Iterable): A list, tuple, or dict_values of objects (e.g., dataclass instances)
            that support attribute access via `__dict__`.
    """
    # Convert to list in case it's dict_values or other iterable
    obj_list = list(objects)

    if not obj_list:
        raise ValueError("The objects list can't be empty.")

    # Convert each object to a dictionary
    try:
        rows = [vars(obj) for obj in obj_list]
    except TypeError as e:
        raise ValueError("Objects must be class instances with __dict__ or use a dataclass") from e

    # Extract headers from first row
    fieldnames = rows[0].keys()

    # Write to CSV
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
