"""This module defines the `VoteType` enumeration, which represents the type of vote
a legislator can cast in a legislative process. The enum includes support for
'FOR' and 'AGAINST' vote types, each with a corresponding integer value
used in vote result calculations or storage.
"""
from enum import Enum


class VoteType(Enum):
    """
    Enumeration representing the possible types of votes a legislator can cast.

    Attributes:
        FOR (int): A vote in favor of the bill (value: 1).
        AGAINST (int): A vote against the bill (value: 2).
    """
    FOR = 1
    AGAINST = 2
