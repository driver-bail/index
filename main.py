# main.py
from my_module import greet

def main():
    """Main function to demonstrate the usage of the greet function."""
    name = input("Enter your name: ")
    greeting = greet(name)
    print(greeting)

if __name__ == "__main__":
    main()
