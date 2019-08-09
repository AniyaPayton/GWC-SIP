
start = '''
Brody was out late last night partying. His alarm goes off? Should he sleep in for 15 minutes?
'''

print(start)

# Gets up
print(" Type 'get up' to start getting ready for school or 'sleep in' to stay in bed.") # Update to match your story.
user_input = input()
if user_input == "get up":
    print ("Brody is finished getting ready for school with plenty of time to spare. Should he walk or take the bus to school? Type  'bus' or 'walk'")
    user_input = input()
if user_input == "bus":
    print ("Brody get to school on time, and walks to his chemistry class.His teacher goes over instructions but Brody isn't paying attention should he read the instructions or wing it? Type 'read' or 'wing it'")
    user_input = input()
if user_input == "walk":
    print ("On his walk to school Brody gets sprayed by a skunk!! He goes to school anyway, and walks to chemistry class. His teacher goes over instructions but Brody isn't paying attention should he read the instructions or wing it? Type 'read' or 'wing it'")
    user_input = input()
if user_input == "read":
    print ("Brody reads the instruction and expirement goes well")
    user_input = input()
if user_input == "wing it":
    print ("Brody disposes the chemicals in the sink, which is clearly stated in the instruction that if the chemicals are not disposed of properly the town water supply will be ruined!")
    user_input = input()
    # Continue code to finish story.

# sleeps in
elif user_input == "sleep in":
    if user_input == "sleep in":
        print ("Brody overslept and is now running late. Should he run or take the bus to school? Type 'take the bus' or 'run'")
        user_input = input()
    if user_input == "take the bus":
        print ("The bus has a 20 minute delay, so Brody arrives to his chemistry class late. His teacher has already gone over the lab instructions. Should Brody ask for help or improvise? Type 'help' or 'improvise'")
        user_input = input()
    if user_input == "run":
        print ("Brody grabs his backpack and starts running to school but doesnt make it on time. His teacher has already gone over the lab instructions. Should Brody ask for help or improvise? Type 'help' or 'improvise")
        user_input = input()
    if user_input == "help":
        print ("Brody's teacher gets mad at him and doesnt help him at all so Brody disposes his lab's chemical improperly.")
        user_input = input()
    if user_input == "improvise":
        print ("Brody disposes the chemicals in the sink, which is clearly stated in the instruction that if the chemicals are not disposed of properly the town water supply will be ruined!")
        user_input = input()
