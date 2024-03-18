from app.io.input import input_from_console, input_from_file_builtin, input_from_file_pandas
from app.io.output import output_to_console, output_to_file_builtin

def main():
    console_text = input_from_console()

    filename_builtin = "data/input_file.txt"
    file_builtin_text = input_from_file_builtin(filename_builtin)

    filename_pandas = "data/input_file.txt"
    file_pandas_text = input_from_file_pandas(filename_pandas)

    output_to_console(console_text)
    output_to_console(file_builtin_text)
    output_to_console(file_pandas_text)

    output_to_file_builtin("data/output_builtin.txt", console_text + "\n" + file_builtin_text + "\n" + file_pandas_text)


if __name__ == "__main__":
    main()