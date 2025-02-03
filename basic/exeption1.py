
try:
    file = open("Githubprocess.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")