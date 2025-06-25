score = 0

print("Welcome to the Quiz Game!")
print("Answer the following questions in the form of 'a','b','c' or 'd':\n")

print("1.What is the Capital of India?")
print("a) Gujarat\nb) TamilNadu\nc) Maharashtra\nd) New Delhi")
answer1 = input("Your Answer: ").lower()
if answer1 == "d":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! The correct answer is d)New Delhi\n")

print("2.What is 238 + 67 ?")
print("a) 355\nb) 305\nc) 280\nd) 440")
answer2 = input("Your Answer: ").lower()
if answer2 == "b":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! The correct answer is b) 305\n")

print("3. Who wrote 'Harry Potter'?")
print("a) William Shakespeare\nb) J.K. Rowling\nc) Charles Dickens\nd) Mark Twain")
answer3 = input("Your answer: ").lower()
if answer3 == "b":
    print("✅ Correct!\n")
    score += 1
else:
    print("❌ Wrong! The correct answer is b) J.K. Rowling\n")

print(f"🎉 Quiz Completed! Your score is: {score}/3")

if score == 3:
    print("Excellent! You got all answers right!")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Not bad, try again!")
else:
    print("Better luck next time!")
