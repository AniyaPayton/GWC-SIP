#print ("Hello World!")

#def Hello_World():

    #print ("hello world!")

#Hello_World()

# --- Define your functions below! ---
def intro():
    print ("Hi! I'm the chatbot!")

answer_list = ["hey", "what it do baby","what's up", "hi"]

def process_input(answer):
    if answer in answer_list:
        say_greeting()
    else:
        say_default()

def say_greeting():
  print("Hey there!")

# Display a default message to the user.
def say_default():
  print("That's cool!")

def joke():
    while True:
        answer2 = input("Do you want to hear a joke?")
        if answer2 == "yes":
            answer3 = input ("what sound does a nut make when it sneezes?")
        if answer2 == "no":
            print ("To Bad. What sound does a nut make when it sneezes?")
            joke2(answer3)
            #break

def joke2(answer3):
    if answer3 == "cashew":
        print ("That's right")
    else:
        print ("Do you want to give up?")
        if answer == "yes":
            print ("a cashew")
        if answer == "no":
            print("To bad it's a cashew :D")

# --- Put your main program below! ---

def main():
    intro()
    answer_hi= input ("Say hi!")
    process_input(answer_hi)
    joke()



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":

   main()
