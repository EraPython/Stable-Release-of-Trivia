# Python file
# Save this with extension .py
# Made By Arnav Naik
# A beginner's guide to Python


print("Welcome To The Trivia!!")


# Scoring
total_q = 4
print("Total Questions: ", total_q)


def question_1():
    global score
    score = int(0)

# Question1
question1 = str(input("1. What's the best programming language? "))
ans1u = "python"
ans1 = "Python"
if question1 == ans1u or question1 == ans1:
    question_1()
    print("Correct!!")
    score = score + 1
    print("Your Updated Score Is: ", score)
else:
    print("Wrong!!, the correct answer is ",ans1u,"/",ans1)

# Question2
question2 = str(input("2. What's 2+2? "))
ans2 = "4"
if question2 == ans2:
    print("Correct!!")
    score = score + 1
    print("Your Updated Score Is: ", score)
else:
    print("Wrong, the correct answer is: ", ans2)


# Question3
question3 = str(input("3. What's 4-5? "))
ans3 = "-1"
if question3 == ans3:
    print("Correct!!")
    score = score + 1
    print("Your Updated Score Is: ", score)
else:
    print("Wrong, the correct answer is: ", ans3)    


    
# Question4
question4 = str(input("4. What's Java-Script? "))
ans4u = "programming language"
ans4 = "Programming Language"
if question4 == ans4u or question4 == ans4:
    print("Correct!!")
    score = score + 1
    print("Your Updated Score Is: ", score)
else:
    print("Wrong!!, the correct answer is",ans4,"/",ans4u)



print("Thank You For Playing! You Scored: ", score)
print("Credits: Arnav Naik")
print("Check Out My GitHub: https://github.com/code643/Trivia")
    
