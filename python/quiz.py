import getpass, sys
from site import ENABLE_USER_SITE

def question_and_answer(prompt):
    print("Question: " + prompt)
    msg = input()
    print("Answer: " + msg)
    
def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 5
correct = 0
wrong = 0

print('Hey there!, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a test?")

rsp = question_with_response("Who was the quarterback for the Patriots 7 years ago?")
if rsp == "Tom Brady":
    print(rsp + " Good Job!")
    correct += 1
elif rsp == "Mac Jones":
    print(rsp + " is the current quarterback, the question asked for 7 years ago.")
    wrong += 1 
else:
    print("Your answer of " + rsp + " is incorrect! Here is another question.")
    wrong += 1


rsp = question_with_response("Who is the current quarterback for the Patriots?")
if rsp == "Mac Jones":
    print(rsp + " is the current quarterback for the New England Patriots!")
    correct += 1
else:
    print(rsp + " is incorrect!")
    wrong += 1

rsp = question_with_response("What position does Aaron Rodgers play?")
if rsp == "Quarterback":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
    wrong += 1

rsp = question_with_response("Who is the owner of the Patriots football team?")
if rsp == "Robert Kraft":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
    wrong += 1

rsp = question_with_response("What is the name of the most popular football video game?")
if rsp == "Madden":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")
    wrong += 1
    
percent = (correct/questions) * 100

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions) + ". You got " + str(wrong) + " questions wrong. Your percentage on this quiz is " + str(percent) + "%.") 