# Legislative Data Challenge
A project to organize a large amount of publicly available government data. Given the ability to visualize all of the bills that legislators voted for or against.

## Table of Contents

- [Installation](#installation)
- [Questions](#questions)
- [License](#license)


## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/luizcartolano2/legislative-data-challenge.git
   ```
2. Navigate into the project directory
3. Install the dependencies
    ```bash
    python3 -m venv <yourenv>
    source <yourenv>/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
   ```
4. Run the main files
   ```bash
    python bills_with_count.py
    python legislators_with_count.py
    ```
5. You can also run the test files
    ```bash
   pytest handlers/bill_handler_test.py handlers/legislator_handler_tests.py --maxfail=1 --disable-warnings -q
    ``` 

## Questions
1. **Discuss your solution’s time complexity. What tradeoffs did you make?**
    - For this question, we can analyze each method, one by one.
    - The `assign_bill_primary_sponsors` that is responsible for assigning the primary sponsor field on the Bill class iterates over the list of Bill objects. If we call the size of this list `n`, my complexity is going to be `O(n)`. And since I'm working with dicts and how they are implemented in Python (using hash tables), most of my lookup operations will spend, on average, `O(1)`. 
    - The `assign_bill_vote_counts` that is responsible for assigning the counts for the Bill object iterates over the list of Vote Results objects. If we call the size of this list `m`, the complexity will be `O(m)`. And again, dict lookups will be on average `O(1)`.
    - The `assign_legislator_vote_counts` also iterates over the Vote Results objects, so again, `O(m)`.
    - Converting the CSVs into my dict of `<int, Object>` will also be linear, depending on the input size.
    - Concat all those operations together will, at max, add a constant to my linear complexity (I'll run the loop 2/3 times), which shouldn't be an issue since it's just a constant.
    - I believe the biggest tradeoff with this approach is that it complicates the solution a bit, requiring handling dicts and models for each CSV.

2. **How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?**
    - To account for new columns, like "Bill Voted On Date" or "Co-Sponsors", I will need to change my models (inside the models folder) to include those new columns. And then modify the code logic to see these fields as required.

3. **How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?**
    - My solution is already parsing the CSV into a list of Legislators or Bills. The biggest change I would need to support this new structure for the input data would be to convert the data from the list into my models and also adapt to have a dict where each object is mapped to its id.

4. **How long did you spend working on the assignment?**
   - I spent approximately **3 hours** working on the assignment. This time includes initial problem understanding, solution design, coding, testing, debugging, and also documentation and proper setup of the GitHub repo.

## License
[MIT](LICENSE)
