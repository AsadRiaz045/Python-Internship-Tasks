
filename = input("Enter a filename to open: ")

try:
    f = open(filename, "r")
    
    
    print("File successfully opened!")
    f.close()

except FileNotFoundError:
    
    print("File not found")
