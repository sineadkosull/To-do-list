#Sinead and Abby
#1-10-24
#movie list

#initialize

#functions
def movieList():
    movielist = []
    print("Welcome to the movie watch list!")
    while True:
        choice = input("What would you like to do? \n1 - add movie\n2 - view full list\n3 - mark movie as watched \n4 - remove movie from list \n5 - clear full list \n6 - sort alphabetically\n7 - display # of movies\n8 - exit\n")
        if choice == "1":
            ListItem = input("What movie do you want to add to the list? ")
            movielist.insert(1,ListItem)
        elif choice == "2":
            print(movielist[0:])
        elif choice == "3":
            CompleteListItemChoice = input("What movie on the list did you watch? ")
            if CompleteListItemChoice in movielist:
                CompleteListItemIndex = movielist.index(CompleteListItemChoice)
                movielist[CompleteListItemIndex] = (CompleteListItemChoice + " [X]")
            else:
                print("Sorry, that item is not on the list!")
        elif choice == "4":
            RemoveListItem = input("What item would you like to remove? ")
            if CompleteListItemChoice in movielist:
                movielist.remove(RemoveListItem)
            else:
                print("Sorry, that item is not on the list!")
        elif choice == "5":
            movielist.clear()
        elif choice == "6":
            movielist.sort()
        elif choice == "7":
            print(len(movielist))
        elif choice == "8":
            break
        else:
            print("Sorry, thats not an option. Only type in a single number. Try again!")

#main
movieList()