def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

print("enter a number")
no =int(input())

triple= make_multiplier(3)
print(triple(no))