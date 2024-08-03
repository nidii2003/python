# Given string
s: str = "apple,banana,cherry,dates"

# Split the string into a list based on the delimiter ","
fruits_list = s.split(",")

# Join the list into a single string with each element separated by a space
joined_string = " ".join(fruits_list)

# Print the results
print(fruits_list)
print(joined_string)
