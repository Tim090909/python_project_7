def input_from_console():
    """
    Prompt the user to input text from the console.

    Returns:
    str: The text input by the user.
    """
    text = input("Enter something: ")
    return text

def input_from_file_builtin(filename):
    """
    Read text from a file using built-in Python capabilities.

    Args:
    filename (str): The name of the file to read from.

    Returns:
    str: The text read from the file.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return "File not found."

def input_from_file_pandas(filename):
    """
    Read text from a file using the pandas library.

    Args:
    filename (str): The name of the file to read from.

    Returns:
    str: The text read from the file.
    """
    try:
        import pandas as pd
        data = pd.read_csv(filename, header=None)
        text = ' '.join(data.iloc[:, 0].astype(str))
        return text
    except FileNotFoundError:
        return "File not found."