"""
Module to define the Bills class for representing legislative bills.

This module contains a single class, `Bills`, which represents a legislative bill with
attributes for the bill's identifier, title, and the sponsor's identifier.
"""
from dataclasses import dataclass


@dataclass
class Bills:
    """
    Represents a bill with associated details.

    Attributes:
        id (int): The unique identifier for the bill.
        title (str): The title or name of the bill.
        sponsor_id (int): The identifier of the sponsor of the bill.
        primary_sponsor (str): The name of the primary sponsor of the bill (default is "Unknown").
        supporter_count (int): The number of supporters for the bill.
        opposer_count (int): The number of opposers to the bill.
    Example:
        bill = Bills(id=1, title="Education Reform Act", sponsor_id=101)
    """
    id: int  # pylint: disable=invalid-name
    title: str
    sponsor_id: int
    primary_sponsor: str = "Unknown"
    supporter_count: int = 0
    opposer_count: int = 0
