from models import Bills, Legislators, VoteResults, Votes
from utils import parse_csv_to_dataclass

if __name__ == "__main__":
    bills = parse_csv_to_dataclass(filepath='input/bills.csv', cls=Bills, delimiter=',')
    legislators = parse_csv_to_dataclass(filepath='input/legislators.csv', cls=Legislators, delimiter=',')
    vote_results = parse_csv_to_dataclass(filepath='input/vote_results.csv', cls=VoteResults, delimiter=',')
    votes = parse_csv_to_dataclass(filepath='input/votes.csv', cls=Votes, delimiter=',')
    print()
