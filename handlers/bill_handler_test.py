"""
This module contains test cases for the `assign_bill_primary_sponsors` and
`assign_bill_vote_counts` functions. These functions are responsible for
assigning primary sponsors to bills and counting the number of supporters and
opposers for each bill based on the provided vote results.

Test functions include:
- `test_assign_bill_primary_sponsors`: Tests that the correct primary sponsor is assigned to bills.
- `test_assign_bill_primary_sponsors_unknown`: Tests the scenario where a bill's sponsor ID is not found in the list
- `test_assign_bill_vote_counts`: Tests the correct update of supporter and opposer counts for each bill.
- `test_no_votes_for_bill`: Tests the scenario where no votes are cast for a bill.
"""
from handlers import assign_bill_primary_sponsors, assign_bill_vote_counts
from models import Legislators, Bills, Votes, VoteResults, VoteType


def test_assign_bill_primary_sponsors():
    """
    Test case for assigning primary sponsors to bills based on the sponsor_id.
    This test ensures that the primary sponsor of a bill is correctly assigned
    based on the legislator's ID.

    Simulates:
    - Alice sponsors the "Education Reform Act" bill.
    - Bob sponsors the "Healthcare Reform Act" bill.
    """
    legislators = {
        1: Legislators(id=1, name="Alice"),
        2: Legislators(id=2, name="Bob"),
    }

    bills = {
        101: Bills(id=101, title="Education Reform Act", sponsor_id=1),
        102: Bills(id=102, title="Healthcare Reform Act", sponsor_id=2),
    }

    assign_bill_primary_sponsors(bills, legislators)

    assert bills[101].primary_sponsor == "Alice"
    assert bills[102].primary_sponsor == "Bob"


def test_assign_bill_primary_sponsors_unknown():
    """
    Test case where a bill's sponsor_id is not found in the legislators dictionary.
    This test ensures that if a sponsor ID is missing from the list of legislators,
    the sponsor is set to "Unknown".

    Simulates:
    - Alice sponsors the "Education Reform Act" bill.
    - A non-existent legislator (ID=3) sponsors the "Healthcare Reform Act" bill.
    """
    legislators = {
        1: Legislators(id=1, name="Alice"),
        2: Legislators(id=2, name="Bob"),
    }

    bills = {
        101: Bills(id=101, title="Education Reform Act", sponsor_id=1),
        102: Bills(id=102, title="Healthcare Reform Act", sponsor_id=3),  # No legislator with id=3
    }

    assign_bill_primary_sponsors(bills, legislators)

    # Bill 101 has a sponsor with id=1, so it should be assigned to Alice
    assert bills[101].primary_sponsor == "Alice"

    # Bill 102 has a sponsor with id=3, which doesn't exist in the legislators dict, so it should be "Unknown"
    assert bills[102].primary_sponsor == "Unknown"


def test_assign_bill_vote_counts():
    """
    Test case for assigning supporter and opposer counts to bills based on vote results.
    This test ensures that the supporter and opposer counts are updated correctly
    for each bill based on the vote type in the vote results.

    Simulates:
    - "Education Reform Act" bill with 1 supporter (legislator 1) and 1 opposer (legislator 3).
    - "Healthcare Reform Act" bill with 1 opposer (legislator 2) and no supporters.
    """
    bills = {
        101: Bills(id=101, title="Education Reform Act", sponsor_id=1),
        102: Bills(id=102, title="Healthcare Reform Act", sponsor_id=2),
    }

    votes = {
        201: Votes(id=201, bill_id=101),
        202: Votes(id=202, bill_id=102),
    }

    vote_results = {
        301: VoteResults(id=301, legislator_id=1, vote_id=201, vote_type=VoteType.FOR),
        302: VoteResults(id=302, legislator_id=2, vote_id=202, vote_type=VoteType.AGAINST),
        303: VoteResults(id=303, legislator_id=3, vote_id=201, vote_type=VoteType.AGAINST),
    }

    assign_bill_vote_counts(bills, votes, vote_results)

    assert bills[101].supporter_count == 1
    assert bills[101].opposer_count == 1
    assert bills[102].supporter_count == 0
    assert bills[102].opposer_count == 1


def test_no_votes_for_bill():
    """
    Test case where no vote results are available for a bill.
    This test ensures that when there are no votes for a bill, the supporter and opposer counts are zero.

    Simulates:
    - "Education Reform Act" bill with no vote results.
    """
    bills = {
        101: Bills(id=101, title="Education Reform Act", sponsor_id=1),
    }

    votes = {
        201: Votes(id=201, bill_id=101),
    }

    vote_results = {}  # No vote results

    assign_bill_vote_counts(bills, votes, vote_results)

    assert bills[101].supporter_count == 0
    assert bills[101].opposer_count == 0
