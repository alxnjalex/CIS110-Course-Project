print("Hello! Today I will tell you a story about a dog and his owner.")
print("Before I begin telling the story, I have a few questions for you to answer.")
print("After typing the answer, please press the enter key to continue.")
input("\nPress the enter key to continue...")

rStory = "yes"
while rStory.lower() == "yes":
    ownerName = input("\nWhat is your name:  ")
    while (len(ownerName) == 0):
        ownerName = input("Please enter your name:  ")

    ownerAge = input("\nWhat is your age:  ")
    while (len(ownerAge) == 0):
        ownerAge = input("Please enter your age:  ")

    dogName = input("\nWhat is your dog's name:  ")
    while (len(dogName) == 0):
        dogName = input("Please enter your dog's name:  ")

    dogAge = input("\nWhat is your dog's age:  ")
    while (len(dogAge) == 0):
        dogAge = input("Please enter your dog's age:  ")

    dogBreed = input("\nWhat is your dog's breed:  ")
    while (len(dogBreed) == 0):
        dogBreed = input("Please enter your dog's breed:  ")

    favoriteTreat = input("\nWhat is your dog's favorite treat:  ")
    while (len(favoriteTreat) == 0):
        favoriteTreat = input("Please enter your dog's favorite treat:  ")


    print("\nLet us begin the story.")

    print("\nThere once lived a beautiful", dogBreed, "named", dogName + ".")
    print(dogName, "lived with their owner", ownerName, "in a beautiful neighborhood.")
    print(dogName, "was", dogAge, "years old and even thought he was sometimes lazy, he loved to workout.")
    print("Today", dogName, "didn't seem lazy at all, but very energetic.")
    print(ownerName, "had to figure out how to get rid of the excess energy", dogName, "had.")
    print(ownerName, "is", ownerAge, "years old and thinks exercise for both is of great benefit.")
    print(ownerName, "decides it is time to have a workout with his", dogBreed, ".")
    print("\n")
    dogScenario = input("Should they workout today? Type yes or no:  ")
    while dogScenario.lower() != "yes" and dogScenario.lower() != "no":
        dogScenario = input("Please type yes or no:  ")
    
    if dogScenario.lower() == "yes":
        print(ownerName, "and", dogName, "decide to start with a jog around their neighborhood.")
        print("Fifteen minutes later", ownerName, "spots a big open field.")
        print(dogName, "saw what", ownerName, "was looking at and started barking with exitement.")
        print(ownerName, "decides it is time for", dogName, "to do some sprints and heads to the open field.")
        print(ownerName, "pulls out a tennis ball and throws it far across the field.")
        print(ownerName, "keeps playing fetch with his dog for about an hour before he decides his", dogBreed, "had enough exercise.")
        print("They both head back home and the dog looks exhausted.")

    else:
        print(ownerName, " suddenly thought maybe they should do something more fun and relaxing.")
        print(ownerName, "and", dogName, "decided to go get some icecream instead of working out. They start the 10 minute walk to get icecream.")
        print(dogName, "saw that", ownerName, "was looking at the ice cream stand and started barking with exitement as they got closer.")
        print(ownerName, " arrives at the ice cream stand with", dogName, "and decides to both get a vanilla cone.")
        print(ownerName, "knows his dog loves this flavor.")
        print(dogName, " eats the ice cream fast and then waits for", ownerName, "to finish.")
        print("They both head back home and the dog seems sleepy from the sugar crash.")


    print("\n")
    print("As soon as they both arrive home,", dogName, "drinks water and heads off to his bed to take a nap.")
    print("After a long two-hour nap,", dogName, "wakes up and barks at", ownerName, "and the tv, indicating he wants to watch tv.")
    print(ownerName, "finds a channel about his", dogBreed, "and gives", dogName, favoriteTreat, "for being such a good dog today.")
    print("The", favoriteTreat, "is the dog's favorite and his incredibly happy eating it and watching tv.")
    print("\n")
    print("Outside it looks like the sun is about to set.")
    print(ownerName, "wants to go for a walk around the neighborhood with his", dogBreed, ".")
    print("\n")
    otherScenario = input("Is the dog too tired from previous events of the day? Type Yes or No:  ")
    while otherScenario.lower() != "yes" and otherScenario.lower() != "no":
        otherScenario = input("Please type yes or no:  ")

    if otherScenario.lower() == "yes":
        print(ownerName, "decides to go on a walk on his own and leave his dog home.")
        print(dogName, "is very happy with his owners decision.")
        print(ownerName, "hopes he wont regret the choice to leave his dog home on such a beautiful night.")

    else:
         print(dogName, "refuses to budge after", ownerName, "tries to take him outside.")
         print("In the end", ownerName, "promises", dogName, "that he will give him", favoriteTreat, ".")
         print("This makes", dogName, "agree to go on a walk and they both head out for a walk as the sun sets.")
         print("When they both arrive back home", dogName, "receives a lot of", favoriteTreat, ".")
    print("\n")
    if dogScenario.lower() == "yes":
        print("Today was a wonderful day.")
        print(dogName, "spent his day happily with", ownerName, ".")
        print(dogName, "is a wonderful", dogBreed, ".")
        print("Today", dogName, "had an outstanding workout doing 60-minute fetch sprints and later a short walk around the neighborhood enjoying the sunset with", ownerName, ".")
        print("\n")
   

    else: 
         print("Today was a wonderful day.")
         print(dogName, "spent his day happily with", ownerName, ".")
         print(dogName, "is a wonderful", dogBreed, ".")
         print("Today", dogName, "had a fantastic day and still cant believe he got to eat ice cream with", ownerName, ".")
         print("\n")
     

    if otherScenario.lower() == "yes":
         print("Later,", dogName, "wishes he could of went on that sunset walk with his owner.")
         print("The end. Thank you for reading.")
    rStory = input("Would you like to repeat the story? Enter yes or no:  ")
    while rStory.lower() != "yes" and rStory.lower() != "no":
        rStory = input("Please type yes or no: ")

  

     

     





