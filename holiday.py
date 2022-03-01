name = input("What is your name?")

age = input("What is your age?")

if 18 <= age < 31:
    print( "{0} you are free to go on holiday".format(name))
else:
    print("{0} you are not the right age to go on holiday".format(name))

