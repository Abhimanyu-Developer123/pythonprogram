
file = open("sample.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())  # Removes the newline character
file.close()
