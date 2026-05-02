"""
Bank data storage system
Made by: Rain
Version: 1.0.0
"""


class Bank:
    """A simple file-based data storage system using custom delimiters."""

    def store(self, file_name, variable_name, contents):
        """Store a variable with its contents to a file."""
        with open(file_name, "a") as f:
            f.write(f":% {variable_name} %: {contents}\n")

    def get_value(self, file_name, variable_name):
        """Retrieve the value of a stored variable."""
        with open(file_name, "r") as f:
            tokens = f.read().split("%:")

        for index in range(len(tokens)):
            if tokens[index] == f":% {variable_name}":
                return tokens[index + 1]
        return None

    def get_line(self, file_name, variable_name):
        """Get the entire line containing a variable."""
        with open(file_name, "r") as f:
            lines = f.readlines()

        for line in lines:
            if variable_name in line:
                return line
        return None

    def delete(self, file_name, variable_name):
        """Delete all lines containing a variable."""
        with open(file_name, "r") as f:
            lines = f.readlines()

        with open(file_name, "w") as f:
            for line in lines:
                if variable_name not in line:
                    f.write(line)

    def replace(self, file_name, variable_name, new_contents):
        """Replace the contents of a variable."""
        with open(file_name, "r") as f:
            lines = f.readlines()

        with open(file_name, "w") as f:
            for line in lines:
                if variable_name in line:
                    f.write(f":% {variable_name} %: {new_contents}\n")
                else:
                    f.write(line)

    def get_all(self, file_name):
        """Retrieve all contents from a file."""
        with open(file_name, "r") as f:
            return f.read()
