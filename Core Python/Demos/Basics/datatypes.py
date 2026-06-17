### Numeric Data Types

# 1. int
# Store integer value (Immutable)
x = 10

# 2. float
# Store decimal value (Immutable)
x = 10.5

# 3. complex
# Store real + imaginary value (Immutable)
x = 5 + 20j


### Text Data Type

# 1. str
# Store text using single quotes (Immutable)
x = 'first line'

# Store text using double quotes (Immutable)
x = "first line"

# Store multiline text using triple single quotes (Immutable)
x = '''It is first line,
It is second line.'''

# Store multiline text using triple double quotes (Immutable)
x = """It is first line,
It is second line."""


### Sequential Data Types

# 1. list
# Store multiple values (Mutable)
x = [10, 20, 30, 40]

# 2. tuple
# Store multiple values (Immutable)
x = (10, 20, 30, 40)

# 3. range
# Generate sequence of numbers (Immutable)
x = range(1, 10)


### Set Data Types

# 1. set
# Store unique values (Mutable)
x = {10, 20, 30, 40}

# 2. frozenset
# Store immutable set values (Immutable)
x = frozenset({10, 20, 30, 40})


### Mapping Data Type

# 1. dict
# Store data in key-value pair (Mutable)
x = {1: 'python', 2: 'Java', 3: 'C'}


### Other Data Types

# 1. bool
# Store True or False value (Immutable)
x = False
x = True

# 2. NoneType
# Store no value (Immutable)
x = None


# Print datatype of current value
print(type(x))