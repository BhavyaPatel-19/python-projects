def get_words():
    print("i will ask you for some words. \n")
    name      = input("Enter a person's name: ")
    adjective = input("Enter an adjective(describing word): ")
    noun      = input("Enter a noun(a thing): ")
    verb      = input("Enter a verb ending in -ing: ")
    place     = input("Enter a place: ")
    number    = input("enter a number: ")
    return name, adjective, noun, verb, place, number

def tell_story(name, adjective, noun, verb, place, number):
    print("\n--- HERE'S YOUR MADLIBS STORY! ---\n")
    print(f"One day, {name} woke up feeling very {adjective}.")
    print(f"They decided to take their {noun} to {place}.")
    print(f"On the way, they spent {number} hours {verb}.")
    print(f"Everyone in {place} was amazed by {name}.")
    print("\n The End!🎉")

def ask_play_again():
    answer=input("\nDo you want to play again? (Yes/No): ")
    return "yes" in answer.lower()

def main():
    print("=== Welcome to Madlibs! ===")
    while True:
        name, adjective, noun, verb, place, number = get_words()
        tell_story(name, adjective, noun, verb, place, number) 
        if ask_play_again():
            print("\nLet's Play Again!\n")
        else:
            print("Thanks for playing ! See you next time!🤜🏼")
            break 
main()

        
