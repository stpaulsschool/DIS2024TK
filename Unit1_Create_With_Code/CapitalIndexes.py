print("Welcome to my Capital Indexes Counter!")  # it can only print the letters themselves
x = 1
while x == 1:
    mylist = []
    capital_indexes = input("Enter the text, please (q to quit) ")
    if capital_indexes != "q":
        for item, char in enumerate(capital_indexes):
            if char.isupper():
                mylist.append(item+1)
        print(mylist)
    else:
        print("Ok, see you soon!")
        x = x + 1
