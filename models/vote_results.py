"""Module to define the VoteResults class for representing voting outcomes.

This module contains the `VoteResults` class, which represents the outcome of a vote
cast by a legislator, including the vote's identifier, the legislator's ID, the vote ID,
and the type of vote (e.g., for, against, abstain).
"""
from dataclasses import dataclass
from .vote_type import VoteType


@dataclass
class VoteResults:
    """
    Represents the results of a vote cast by a legislator.

    Attributes:
        id (int): The unique identifier for the vote result.
        legislator_id (int): The unique identifier of the legislator who cast the vote.
        vote_id (int): The identifier for the specific vote.
        vote_type (VoteType): The type of vote (e.g., for, against, abstain).

    Example:
        vote_result = VoteResults(id=1, legislator_id=1001, vote_id=10, vote_type=1)
    """
    id: int  # pylint: disable=invalid-name
    legislator_id: int
    vote_id: int
    vote_type: VoteType
