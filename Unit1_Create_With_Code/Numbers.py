import random
while True:
    hi = input("Hi! Guess what number from 1 to 10 I am thinking about! (y to play, q to quit) ").lower()
    if hi == "y":
        hints = input("Do you want me to say if the number is greater or lower? (y for yes, n for no) ").lower()
        if hints == "n":
            difficulty = input("Choose the difficulty (e for easy, m for medium, h for hard) ").lower()
            if difficulty == "h":
                if hi != "q":
                    y = 1
                    tries = 3
                    x = random.randint(1, 10)
                    guess = int(input("Take a guess! You have 3 tries! "))
                    while guess != x:
                        while tries != 1:
                          y += 1
                          tries -= 1
                          guess = int(input(f"Try again! You have a total of {tries} tries left! "))
                          if guess == x:
                              print(f"You are right, the number is {guess}! It took you a total of {y} tries to guess!")
                              hi = "e"
                              break
                        else:
                           print(f"You lost! The number was {x}!")
                           hi = "e"
                           break
                else:
                    print("Ok! Have a good day! ")
            if difficulty == "m":
                if hi != "q":
                    y = 1
                    tries = 7
                    x = random.randint(1, 10)
                    guess = int(input("Take a guess! You have 7 tries! "))
                    while guess != x:
                        while tries != 1:
                          y += 1
                          tries -= 1
                          guess = int(input(f"Try again! You have a total of {tries} tries left! "))
                          if guess == x:
                              print(f"You are right, the number is {guess}! It took you a total of {y} tries to guess!")
                              hi = "e"
                              break
                        else:
                           print(f"You lost! The number was {x}!")
                           hi = "e"
                           break
                else:
                    print("Ok! Have a good day! ")
            if difficulty == "e":
                if hi != "q":
                    y = 1
                    x = random.randint(1, 10)
                    guess = int(input("Take a guess! You have an unlimited amount of tries! "))
                    while guess != x:
                      y += 1
                      guess = int(input("Try again! You have an unlimited amount of tries left! "))
                    else:
                      print(f"You are right, the number is {guess}! It took you a total of {y} tries to guess!")
                      hi = "e"
                else:
                    print("Ok! Have a good day! ")
        if hints == "y":
            difficulty = input("Choose the difficulty (e for easy, m for medium, h for hard) ").lower()
            if difficulty == "h":
                if hi != "q":
                    y = 1
                    tries = 3
                    x = random.randint(1, 10)
                    guess = int(input("Take a guess! You have 3 tries! "))
                    while guess != x:
                        while tries != 1:
                            y += 1
                            tries -= 1
                            if guess < x:
                              guess = int(input(f"Try again! It should be greater! You have a total of {tries} tries left! "))
                            if guess > x:
                              guess = int(input(f"Try again! It should be lower! You have a total of {tries} tries left! "))
                            if guess == x:
                              print(f"You are right, the number is {guess}! It took you a total of {y} tries to guess!")
                              hi = "e"
                              break
                        else:
                            print(f"You lost! The number was {x}!")
                            hi = "e"
                            break
                else:
                    print("Ok! Have a good day! ")
            if difficulty == "m":
                if hi != "q":
                    y = 1
                    tries = 7
                    x = random.randint(1, 10)
                    guess = int(input("Take a guess! You have 7 tries! "))
                    while guess != x:
                        while tries != 1:
                            y += 1
                            tries -= 1
                            if guess < x:
                              guess = int(input(f"Try again! It should be greater! You have a total of {tries} tries left! "))
                            if guess > x:
                              guess = int(input(f"Try again! It should be lower! You have a total of {tries} tries left! "))
                            if guess == x:
                              print(f"You are right, the number is {guess}! It took you a total of {y} tries to guess!")
                              hi = "e"
                              break
                        else:
                            print(f"You lost! The number was {x}!")
                            hi = "e"
                            break
                else:
                    print("Ok! Have a good day! ")
            if difficulty == "e":
                if hi != "q":
                    y = 1
                    x = random.randint(1, 10)
                    guess = int(input("Take a guess! You have an unlimited amount of tries! "))
                    while guess != x:
                      y += 1
                      if guess < x:
                        guess = int(input("Try again! It should be greater! You have an unlimited amount of tries left! "))
                      if guess > x:
                        guess = int(input("Try again! It should be lower! You have an unlimited amount of tries left! "))
                      if guess == x:
                        print(f"You are right, the number is {guess}! It took you a total of {y} tries to guess!")
                        hi = "e"
                        break
                else:
                    print("Ok! Have a good day! ")
    if hi == 'q':
        print("Ok! Have a good day!")
        break


