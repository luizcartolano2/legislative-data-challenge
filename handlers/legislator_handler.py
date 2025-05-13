"""
This module provides a function to update each legislator's vote count
based on their recorded vote results.

The function modifies `Legislators` dataclass instances in place, increasing the
number of supported or opposed bills depending on the type of vote recorded.
"""

from models import VoteType, Legislators, VoteResults


def assign_legislator_vote_counts(
    legislators: dict[int, Legislators],
    vote_results: dict[int, VoteResults]
):
    """
    Updates the support and opposition counts for each legislator based on vote results.

    Args:
        legislators (dict[int, Legislators]): Dictionary of legislators keyed by legislator ID.
        vote_results (dict[int, VoteResults]): Dictionary of vote results keyed by result ID.

    Notes:
        - Assumes all vote_result.legislator_id values exist in the legislators dictionary.
        - Modifies the Legislators objects in-place.
    """
    for vote_result in vote_results.values():
        legislator = legislators[vote_result.legislator_id]
        if vote_result.vote_type == VoteType.FOR:
            legislator.num_supported_bills += 1
        elif vote_result.vote_type == VoteType.AGAINST:
            legislator.num_opposed_bills += 1
