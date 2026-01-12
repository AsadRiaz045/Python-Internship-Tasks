
with open("poem.txt", "w") as f: f.write("Line 1\nLine 2\nLine 3")
with open("poem.txt", "r") as f:
    lines = f.readlines()

print(len(lines))