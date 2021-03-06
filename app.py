# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""

# The following are libraries require to run this Loan Qualifier Application
import sys
import fire
import questionary
from pathlib import Path

# These are segments of code that we have modularized and have pulled into the main app.py program
from qualifier.utils.fileio import load_csv, save_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

# List of filters used to determine qualifying banks, modularized
from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """
    # This prompts the user to enter in the path to the CSV file for downloading
    csvpath = questionary.path("Enter a file path to a rate-sheet (.csv):").ask() #changed .text to .path for ease of use
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    temp = load_csv(csvpath)
    return temp


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    # These questions prompt the user to enter in the following personal data, and this allows us to reuse
    # the code for any users input, making this a dynamic program
    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    # This makes sure our values are either integers or floats, depending on the requirements to run the calculations
    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculates the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculates loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Runs qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")
    
    # Returns a filtered list of all qualifying loans
    return bank_data_filtered



def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!

    # If there are no qualifying loans based on users criteria, the system will exit
    if len(qualifying_loans) == 0:
        qualifying_loans = None
    if qualifying_loans == None:
        sys.exit("There are no qualifying loans.")
        
    # This prompts the user to decide if they do indeed qualify for loans, would they like to upload that to 
    # an easy to read CSV file. This will give them an option of (Y/n)    
    confirm_save_file = questionary.confirm("Would you like to save the results to a CSV file?").ask()

    if confirm_save_file == False:
        sys.exit("Your files will not be saved.")
    elif confirm_save_file == True:
        filepath = questionary.path("Enter in the file path to save the CSV file.").ask()
        save_csv(filepath, qualifying_loans)   # If the user opts to save the file, the save_csv module will run
            

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # This gets the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # This filters the qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # This saves the qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)

# This is a test to see if Github replaces files with changes