# Given string
s: str = "   Python is fun!   "

# Remove leading and trailing spaces
stripped_string = s.strip()

# Left justify with '*' within a width of 20
left_justified = stripped_string.ljust(20, '*')

# Right justify with '*' within a width of 20
right_justified = stripped_string.rjust(20, '*')

# Print the results
print(stripped_string)
print(left_justified)
print(right_justified)
