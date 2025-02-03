
try:
    x = int("abc")  # Will cause a ValueError
except Exception as e:
    print("An error occurred:", e)