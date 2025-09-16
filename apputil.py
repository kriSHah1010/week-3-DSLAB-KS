# Exercise 1: The Fibonacci Series

def fib(n):
    """
    Return the nth Fibonacci number using recursion.
    Parameters
    n : int
        The position in the Fibonacci sequence (0-based index).
    Returns
    int
        The nth Fibonacci number.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# Ask the user for input
n = int(input("Which element of the Fibonacci sequence do you want to know? "))

# Validate input
if n < 0:
    print("Negative values are not allowed. Please enter a non-negative integer.")
else:
    # Print the nth Fibonacci number
    print(f"\nThe {n}th Fibonacci number is: {fib(n)}")

    # Print the full sequence up to n
    print("\nFibonacci sequence up to that number:")
    for i in range(n + 1):
        print(fib(i), end=" ")
    print()  





# Exercise 2 :  a (single) recursive function, `to_binary()`, that converts an integer into its binary

def to_binary(n):
    """
    Convert a non-negative integer to its binary representation using recursion.

    Parameters
    ----------
    n : int
        The integer to be converted (must be non-negative).

    Returns
    -------
    str
        Binary representation of the input integer.
    """
    if n < 0:
        raise ValueError("Only non-negative integers are allowed.")

    if n in (0, 1):
        return str(n)

    return to_binary(n // 2) + str(n % 2)

# Ask the user for input
user_input = input("Enter a non-negative integer to convert into binary: ")

# Validate input
if not user_input.isdigit():
    print("Invalid input. Please enter a non-negative integer.")
else:
    n = int(user_input)
    print(f"Binary representation of {n} is: {to_binary(n)}")


# Exercise 3: Write a function for each of the following tasks

import pandas as pd

# Load the dataset
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    """
    Return a list of all column names, sorted by the number of missing values.
    Columns with fewer missing values appear first.
    """
    # Clean 'gender' column: strip spaces and convert to lowercase
    if 'gender' in df_bellevue.columns:
        df_bellevue['gender'] = df_bellevue['gender'].str.strip().str.lower()
        print(" Cleaned 'gender' column: stripped spaces, made lowercase.")

    # Count missing values per column
    missing_counts = df_bellevue.isnull().sum()

    # Sort columns by missing values
    sorted_columns = missing_counts.sort_values().index.tolist()

    return sorted_columns

def task_2():
    """
    Return a DataFrame with columns:
    - 'year': each unique year in the dataset
    - 'total_admissions': number of admissions per year
    """
    if 'date_in' not in df_bellevue.columns:
        print(" 'date_in' column not found. Check dataset.")
        return None

    # Extract year from 'date_in' column
    df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce').dt.year

    # Group by 'year' and count the number of entries
    admissions_by_year = df_bellevue.groupby('year').size().reset_index(name='total_admissions')

    return admissions_by_year

def task_3():
    """
    Return a Series with:
    - Index: gender
    - Values: average age for each gender
    """
    if 'gender' not in df_bellevue.columns or 'age' not in df_bellevue.columns:
        print("'gender' or 'age' column missing. Check dataset.")
        return None

    # Group by 'gender' and calculate the mean age
    avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean()

    return avg_age_by_gender


def task_4():
    """
    Return a list of the 5 most common professions in order of prevalence.
    """
    if 'profession' not in df_bellevue.columns:
        print(" 'profession' column not found. Check dataset.")
        return None

    # Count the occurrences of each profession and get the top 5
    common_professions = df_bellevue['profession'].value_counts().head(5).index.tolist()

    return common_professions


print("--- Task 1: Sorted Column Names by Missing Values ---")
print(task_1())
print("\n")

print("--- Task 2: Total Admissions by Year ---")
print(task_2())
print("\n")

print("--- Task 3: Average Age by Gender ---")
print(task_3())
print("\n")

print("--- Task 4: Top 5 Most Common Professions ---")
print(task_4())
print("\n")