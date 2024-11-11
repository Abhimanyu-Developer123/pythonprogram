def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier

print("enter a number")
no =int(input())

double = make_multiplier(2)
print(double(no))
