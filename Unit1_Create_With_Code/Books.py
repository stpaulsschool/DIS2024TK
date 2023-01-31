answer = input("Welcome to my little Book Title Counter! Do you want me to count the symbols in the title of the book you say? (Yes/No)")
if answer == "Yes" or "yes":
     book = input("What is the title of the book? ")
     length = str(len(book))
     print("There are " +length+ " symbols in the book title " +book+ " including the spaces.")
else:
    input("Ok")
