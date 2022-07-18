# Import function
import random
# Variables definition
name = "Guillaume"
question = "Will I ever be rich ?"
answer = ""
random_number = random.randint(1,11)

# Start of the program
print("The random number is : " + str(random_number))

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number ==10:
  answer = "For sure."
elif random_number == 11:
  answer = "Yeah, I don't think so.."
else:
  answer = "Error"

# Program 1.0
# print(name + " asks: " + question)
# print("Magic 8-Ball's answer: " + answer)

# Whitespace 
print(" ")
print(" ")
print(" ")


# Program 2.0

if name == "" and not question == "":
  print("The question is: " + question)
  print("Magic 8-Ball's answer: " + answer)
elif name == "" and  question == "":
  print("Listen stranger, the Magic 8-ball cannot provide a fortune without a question")
elif not name == "" and question == "":
   print(name + " did not ask anything.")
   print("The Magic 8-ball cannot provide a fortune without a question")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
