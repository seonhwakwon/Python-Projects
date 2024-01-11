from PIL import Image


def start(nice=0, mean=0, name=""):
    #get user's name
    image()
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)
    
#add image
def image():
    img =Image.open("nice_or_mean.jpg")
    img.show()
#    

def describe_game(name):
    if name != "":
        print(f"\n Thank you for playing again, {name}")
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name?\n>>>").capitalize()
                if name != "":
                    print(f"\nWelcome, {name}")
                    print("\nIn this game, you will be greeted \nby several different people, \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \n will be sealed by your action.")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\n Stranger approaches you for a \nconverstation. Will you be nice \nor mean (N/M) \n>>>: ").lower()
        if pick =="n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        elif pick =="m":
            print("\nThe stranger glares at you \nmenacingly and storms off")
            mean = (mean +1)
            stop = False
         #add this code
        else:
             print("\nEnter the N/M (N) for nice, (M)for mean")
    score(nice, mean, name)

def show_score(nice, mean, name):
    print(f"\n{name}, your current total:\n({nice}, Nice) and ({mean}, Mean)")

def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice, mean, name):
    print(f"\nNice job {name}, you win! \nEveryone loves yopu and you've \nmade lots of friends along the way!")
    again(nice, mean, name)

def lose(nice, mean, name):
    print(f"\nAhhhh too bad, game over!\n{name}, you live in a dirty beat-up \nvan by the river, wretched and alone.")
    again(nice,mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop= False
            reset(nice,mean,name)
        elif choice =='n':
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) fpr 'NO': \n>>>")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)


if __name__ == "__main__":
    start()

    
