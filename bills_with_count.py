"""
This script aggregates data about bills, including identifying the primary sponsor for each bill
and counting how many legislators supported or opposed each bill.

Steps:
    1. Reads data from input CSV files for bills, legislators, votes, and vote results.
    2. Sets the `primary_sponsor` field of each bill using the sponsor's name.
    3. Increments the supporter or opposer count for each bill based on associated vote results.
    4. Writes the updated bill information to an output CSV file.

Input:
    - input/bills.csv
    - input/legislators.csv
    - input/vote_results.csv
    - input/votes.csv

Output:
    - output/bills.csv: Each bill with updated sponsor and vote count information.
"""
from handlers import assign_bill_primary_sponsors, assign_bill_vote_counts
from models import Bills, Legislators, VoteResults, Votes, VoteType
from utils import parse_csv_to_dataclass_dict, write_objects_to_csv

if __name__ == "__main__":
    bills = parse_csv_to_dataclass_dict(filepath='input/bills.csv', cls=Bills, delimiter=',')
    legislators = parse_csv_to_dataclass_dict(filepath='input/legislators.csv', cls=Legislators, delimiter=',')
    vote_results = parse_csv_to_dataclass_dict(filepath='input/vote_results.csv', cls=VoteResults, delimiter=',')
    votes = parse_csv_to_dataclass_dict(filepath='input/votes.csv', cls=Votes, delimiter=',')

    # 1. Find primary sponsor
    assign_bill_primary_sponsors(bills, legislators)

    # 2. Find voters for bills
    assign_bill_vote_counts(bills, votes, vote_results)

    # 3. Write the result to a CSV file
    write_objects_to_csv('output/bills.csv', bills.values())
