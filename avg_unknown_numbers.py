#Average of Unknown Numbers
#Zoë Klapman
#9/17/20

#Get number of test scores going to be averaging
numberOfScores = int(input("Enter the number of test scores:\n"))
print(f"Let's average the {numberOfScores} test scores...")

#Get the individual test scores and find their sum.
testScores = []
sum = 0
for i in range(0,numberOfScores):
    score = float(input("Enter test score:\n"))
    sum += score
    testScores.append(score)

#Average the test scores.
print(f"Let's average the {numberOfScores} test scores...")
avg = sum / numberOfScores
print("The average score is: " + str(avg))