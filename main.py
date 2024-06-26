def main():
    hello(input("Whats your name?: "))
    goodbye(input("Whats your name?: "))

def hello(name):
    print(f"hello {name}")

def goodbye(name):
    print(f"goodbye, {name}")
    


main()