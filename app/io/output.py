def output_to_console(text):
    """
    Function to output text to the console.

    Args:
    text (str): The text to be output to the console.
    """
    print(text)

def output_to_file_builtin(filename, text):
    """
    Function to write text to a file using built-in Python capabilities.

    Args:
    filename (str): The name of the file to write to.
    text (str): The text to be written to the file.
    """
    with open(filename, 'w') as file:
        file.write(text)

def output_to_file_pandas(filename, text):
    """
    Function to write text to a file using the pandas library.

    Args:
    filename (str): The name of the file to write to.
    text (str): The text to be written to the file.
    """
    try:
        import pandas as pd
        data = pd.DataFrame({'Text': [text]})
        data.to_csv(filename, index=False, header=False)
    except ImportError:
        print("Pandas library not available. Install it using 'pip install pandas'.")
