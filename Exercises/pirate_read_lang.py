import sys

new_file = open(sys.argv[1], 'r')
print(new_file.read())

def printus():
    print("Welcome!")