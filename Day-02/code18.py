file = open("example.txt", "r")
lines = file.readlines()

num_lines = len(lines)

print("Number of lines in the file:", num_lines)

file.close()
