# Simonne ter Weele
# sat2uh
import fileinput
import sys

def greetings(msg):
    print(msg)

def main():
    aGreet = input("Enter a greeting: ")
    greetings(aGreet)

if __name__ == "__main__":
    main()