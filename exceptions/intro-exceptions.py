number = input("Enter a number: ")

try:
    print(int(number) * 3)
except ValueError:
    print("Input Value Error, {} is not a int".format(number))