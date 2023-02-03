print("Welcome to my Little Word Counter!")
x = 1
while x == 1:
    answer = input("Enter the name of the book, please (q to quit) ").lower()
    if answer != "q":                         # run/not run the program
        answer = answer.title()
        mylist = answer.split()
        number = len(mylist)
        words = str(number)
        if number < 5:                        # analyzing whether the title has more or less than 5 words
            print(f"Wow! '{answer}' has only {words} words! All books with less than 5 words in the title are bestsellers!")
        else:
            print(f"Wow! '{answer}' has {words} words. All books with 5 or more words in the title are bad! >:) ")
    else:
        print("Ok, see you soon!")
        x = x + 1 
