
def outer():
    def inner():
        print("hi")
    inner()
outer() 