score = int(input("What is your exam score (0-100):"))
if score >=90 and score <=100:
    print("You got an A! Congrats!")
elif score >= 80 and score <90:
    print("You got a B! Well done!")
elif score >=70 and score <80:
    print("You got a C.")
else:
    print("You did not pass the exam.")