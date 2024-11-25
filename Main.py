import csv

def generate_next_10_numbers(start: int) -> str:
    """
    Generate the next 10 numbers starting from the given integer.

    Args:
        start (int): The starting integer.

    Returns:
        str: A comma-delimited string of the next 10 numbers.
    
    Example:
        >>> generate_next_10_numbers(5)
        '6,7,8,9,10,11,12,13,14,15'
    """
    numbers = [start + i + 1 for i in range(10)]
    return ','.join(map(str, numbers))


def list_to_comma_string(items: list[str]) -> str:
    """
    Convert a list of strings into a comma-delimited string.

    Args:
        items (list[str]): A list of strings to be joined.

    Returns:
        str: A single string where items are separated by commas.
    
    Example:
        >>> list_to_comma_string(["apple", "banana", "cherry"])
        'apple,banana,cherry'
    """
    return ','.join(items)


def write_to_csv(headers: str, data: str, readme: str) -> None:
    """
    Write headers and data to a CSV file.

    Args:
        headers (str): A comma-delimited string representing the CSV headers.
        data (str): A comma-delimited string of data values.
        filename (str): README.py

    Returns:
        None
    
    Example:
        >>> write_to_csv("col1,col2", "1,2,3,4", "output.csv")
        # Creates a file named 'output.csv' with the given data.
    """
    with open(readme, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers.split(','))
        writer.writerow(data.split(','))


if __name__ == "__main__":
    # Example usage
    headers = "col1,col2,col3"
    data = generate_next_10_numbers(5)
    print(f"Generated Data: {data}")

    write_to_csv(headers, data, "output.csv")
    print("CSV file 'output.csv' has been created.")
