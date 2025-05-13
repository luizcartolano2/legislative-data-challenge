"""Module to define the Bill class for representing legislative bills.

This module contains the `Bill` class, which represents a bill with details about its
identifier, title, supporter and opposer counts, and the primary sponsor of the bill.
"""
from dataclasses import dataclass


@dataclass
class Bill:
    """
    Represents a legislative bill with details about its support and opposition.

    Attributes:
        id (int): The unique identifier for the bill.
        title (str): The title or name of the bill.
        supporter_count (int): The number of supporters for the bill.
        opposer_count (int): The number of opposers to the bill.
        primary_sponsor (str): The name of the primary sponsor of the bill (default is "Unknown").

    Example:
        bill = Bill(id=1, title="Tax Reform Act", supporter_count=200, opposer_count=50, primary_sponsor="Jane Doe")
    """
    id: int  # pylint: disable=invalid-name
    title: str
    supporter_count: int
    opposer_count: int
    primary_sponsor: str = "Unknown"
