"""
This module contains helper functions for enriching bill data by:
1. Assigning the primary sponsor's name to each bill based on legislator data.
2. Counting the number of supporting and opposing votes for each bill.

These functions operate on dictionaries of parsed dataclass instances.
"""

from models import VoteType, Bills, Legislators, Votes, VoteResults


def assign_bill_primary_sponsors(bills: dict[int, Bills], legislators: dict[int, Legislators]):
    """
    Assigns the name of the primary sponsor to each bill using the sponsor_id.

    Args:
        bills (dict[int, Bills]): Dictionary of bills keyed by bill ID.
        legislators (dict[int, Legislators]): Dictionary of legislators keyed by legislator ID.
    """
    for bill in bills.values():
        if bill.sponsor_id in legislators:
            bill.primary_sponsor = legislators[bill.sponsor_id].name


def assign_bill_vote_counts(
    bills: dict[int, Bills],
    votes: dict[int, Votes],
    vote_results: dict[int, VoteResults]
):
    """
    Updates each bill's supporter and opposer count based on vote results.

    Args:
        bills (dict[int, Bills]): Dictionary of bills keyed by bill ID.
        votes (dict[int, Votes]): Dictionary of votes keyed by vote ID.
        vote_results (dict[int, VoteResults]): Dictionary of vote results keyed by result ID.
    """
    for vote_result in vote_results.values():
        vote = votes[vote_result.vote_id]
        bill = bills[vote.bill_id]

        if vote_result.vote_type == VoteType.FOR:
            bill.supporter_count += 1
        elif vote_result.vote_type == VoteType.AGAINST:
            bill.opposer_count += 1
