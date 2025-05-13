"""Module to define the Votes class for representing votes on legislative bills.

This module contains the `Votes` class, which represents a vote associated with a
specific bill, including the vote's identifier and the identifier of the bill being voted on.
"""
from dataclasses import dataclass


@dataclass
class Votes:
    """
    Represents a vote associated with a legislative bill.

    Attributes:
        id (int): The unique identifier for the vote.
        bill_id (int): The unique identifier for the bill being voted on.

    Example:
        vote = Votes(id=1, bill_id=1001)
    """
    id: int  # pylint: disable=invalid-name
    bill_id: int
