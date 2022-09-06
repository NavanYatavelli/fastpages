import getpass, sys # imports library/ code
from site import ENABLE_USER_SITE # imports from a site

def question_and_answer(prompt): # defines question_and_answer # definition
    print("Question: " + prompt) # asks question
    msg = input() # get input
    print("Answer: " + msg) # prints answer
    
questions = 8 # declaring variables
correct = 0
wrong = 0

def question_with_response(dictionary): # definition of optimized function
    question = list(dictionary.keys())[0] # get the question from dict
    answer = dictionary[question] # get the answer from dict
    print("Question: " + question) 
    rsp = input()
    global correct, wrong # use global variables
    if rsp == answer:
        print("Correct respose")
        correct += 1
    else:
        print("Incorrect response!")
        wrong += 1

print('Hey there!, ' + getpass.getuser() + " running " + sys.executable) # program logic beggins
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a quiz?") # first question begins

# This is a list of dictionaries
list_quiz =[
    {"Who was the quarterback for the Patriots 7 years ago?":"Tom Brady"},
    {"Who is the current quarterback for the Patriots?":"Mac Jones"},
    {"What position does Aaron Rodgers play?":"Quarterback"},
    {"Who is the owner of the Patriots football team?":"Robert Kraft"},
    {"What is the name of the most popular football video game?":"Madden"},
    {"What command is used to include other functions that are developed?":"import"},
    {"What command in this example is used to evaluate a response?":"if"},
    {"Each 'if' command contains an '_________' to determine a true or false condition?":"expression"}
    ]

# Ask each question    
for dictionary in list_quiz:
    question_with_response(dictionary)

# percent calculation    
percent = (correct/questions) * 100 # finding a perctage

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions) + ". You got " + str(wrong) + " questions wrong. Your percentage on this quiz is " + str(percent) + "%.") # printing out the score and percentage
