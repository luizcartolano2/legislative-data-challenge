"""
This module contains test cases for the `assign_legislator_vote_counts` function.
It verifies that the vote counts (both supported and opposed bills) for legislators
are updated correctly based on the vote results.

The tests ensure that:
- The vote counts are correctly updated when vote results exist for a legislator.
- A legislator with no vote results has a count of zero for supported and opposed bills.
- Multiple votes for the same legislator are handled correctly.
"""

from handlers import assign_legislator_vote_counts
from models import Legislators, VoteResults, VoteType


def test_basic_vote_count_update():
    """
    Test case for basic update of vote counts for multiple legislators.
    This test checks that a legislator's number of supported and opposed bills
    is correctly updated based on the vote results.

    The test simulates the following:
    - Alice supports one bill and opposes another.
    - Bob supports one bill and has no opposition.
    """
    legislators = {
        1: Legislators(id=1, name="Alice"),
        2: Legislators(id=2, name="Bob"),
    }

    vote_results = {
        101: VoteResults(id=101, legislator_id=1, vote_id=201, vote_type=VoteType.FOR),
        102: VoteResults(id=102, legislator_id=1, vote_id=202, vote_type=VoteType.AGAINST),
        103: VoteResults(id=103, legislator_id=2, vote_id=203, vote_type=VoteType.FOR),
    }

    assign_legislator_vote_counts(legislators, vote_results)

    assert legislators[1].num_supported_bills == 1
    assert legislators[1].num_opposed_bills == 1
    assert legislators[2].num_supported_bills == 1
    assert legislators[2].num_opposed_bills == 0


def test_no_votes():
    """
    Test case where no vote results are provided for a legislator.
    This test ensures that a legislator with no vote results has zero supported
    and opposed bills.

    The test simulates the following:
    - Charlie has no vote results, so both supported and opposed bills should be 0.
    """
    legislators = {
        1: Legislators(id=1, name="Charlie"),
    }
    vote_results = {}

    assign_legislator_vote_counts(legislators, vote_results)

    assert legislators[1].num_supported_bills == 0
    assert legislators[1].num_opposed_bills == 0


def test_multiple_votes_same_legislator():
    """
    Test case where a legislator casts multiple votes, both in support and against bills.
    This test checks that the vote counts are correctly incremented based on multiple votes.

    The test simulates the following:
    - Dana supports two bills and opposes one.
    """
    legislators = {
        1: Legislators(id=1, name="Dana"),
    }

    vote_results = {
        101: VoteResults(id=101, legislator_id=1, vote_id=201, vote_type=VoteType.FOR),
        102: VoteResults(id=102, legislator_id=1, vote_id=202, vote_type=VoteType.FOR),
        103: VoteResults(id=103, legislator_id=1, vote_id=203, vote_type=VoteType.AGAINST),
    }

    assign_legislator_vote_counts(legislators, vote_results)

    assert legislators[1].num_supported_bills == 2
    assert legislators[1].num_opposed_bills == 1
