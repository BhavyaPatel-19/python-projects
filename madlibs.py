

while True: 
    print ("=== Welcome to MadLibs! ===")
    print("i will ask you for some words. then i will create a funny story! \n")
    name = input ("enter a person's name: ")
    adjective = input("enter an adjective (describing word): ")
    noun = input ("enter a noun (a thing):")
    verb = input("enter a verb ending with -ing: ")
    place = input ("enter a place: ")
    number = input ("enter a number: ")
    print("\n---  your madlibs story ---\n")
    print(f"One day, {name} woke up feeling very {adjective}.")
    print (f"they decide to take their {noun} to {place}.")
    print (f"On the way, they spend {number} hours {verb}")
    print(f"Everyone in {place} was amazed by {name}!")
    print(f"\n THE END 🎉!")
    play_again = input("\n do you want to play agian? (yes/no):")
    play_again = play_again.lower()
    if "yes" in play_again:
        print ("\n Lets go again!!")
    else:
        print("\nthank you for playing, see you next time!!🙏🙏")
        break 

