"""
This script processes vote result data to count the number of bills each legislator supported or opposed.
It reads data from CSV files containing legislators and vote results, updates the vote counts per legislator,
and then writes the updated data to a new CSV file.

Steps:
    1. Parse legislators and vote results from input CSV files.
    2. Tally the number of supported and opposed bills for each legislator.
    3. Write the updated legislator records to an output CSV file.

Input:
    - input/legislators.csv: List of legislators.
    - input/vote_results.csv: List of vote results.

Output:
    - output/legislators-support-oppose-count.csv: Legislators with updated support and opposition counts.
"""
from handlers import assign_legislator_vote_counts
from models import Legislators, VoteResults, VoteType
from utils import parse_csv_to_dataclass_dict, write_objects_to_csv

if __name__ == "__main__":
    legislators = parse_csv_to_dataclass_dict(filepath='input/legislators.csv', cls=Legislators, delimiter=',')
    vote_results = parse_csv_to_dataclass_dict(filepath='input/vote_results.csv', cls=VoteResults, delimiter=',')

    # 1. Find votes for legislators
    assign_legislator_vote_counts(legislators, vote_results)

    # 2. Write the result to a CSV file
    write_objects_to_csv('output/legislators-support-oppose-count.csv', legislators.values())
