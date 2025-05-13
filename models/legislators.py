"""Module to define the Legislators class for representing legislative members.

This module contains a single class, `Legislators`, which represents a legislator with
attributes for the legislator's identifier and name.
"""
from dataclasses import dataclass


@dataclass
class Legislators:
    """
    Represents a legislator with basic information.

    Attributes:
        id (int): The unique identifier for the legislator.
        name (str): The full name of the legislator.
        num_supported_bills (int): The number of bills the legislator has supported.
        num_opposed_bills (int): The number of bills the legislator has opposed.

    Example:
        legislator = Legislators(id=1, name="John Doe")
    """
    id: int  # pylint: disable=invalid-name
    name: str
    num_supported_bills: int = 0
    num_opposed_bills: int = 0
