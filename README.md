# Bank Library

A simple file-based data storage system using custom delimiters.

## Features

- Store and retrieve variables from files
- Get specific lines containing variables
- Delete variables from files
- Replace variable contents
- Retrieve all file contents

## Installation

```bash
pip install -e .
```

Or, if you want to install from a specific location:

```bash
pip install /path/to/Bank\ lib
```

## Usage

```python
from banklib import Bank

# Create a Bank instance
db = Bank()

# Store a variable
db.store("data.txt", "username", "John")

# Retrieve a value
value = db.get_value("data.txt", "username")
print(value)  # Output: John

# Get an entire line
line = db.get_line("data.txt", "username")

# Replace a value
db.replace("data.txt", "username", "Jane")

# Delete a variable
db.delete("data.txt", "username")

# Get all contents
all_data = db.get_all("data.txt")
print(all_data)
```

## Methods

- `store(file_name, variable_name, contents)` - Store a variable with its contents
- `get_value(file_name, variable_name)` - Retrieve the value of a stored variable
- `get_line(file_name, variable_name)` - Get the entire line containing a variable
- `delete(file_name, variable_name)` - Delete all lines containing a variable
- `replace(file_name, variable_name, new_contents)` - Replace the contents of a variable
- `get_all(file_name)` - Retrieve all contents from a file

## Author

Rain

## License

MIT
