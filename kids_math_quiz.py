import random;
import os;
import time;
# For text to speech https://pypi.org/project/pyttsx3/
import pyttsx3;
engine = pyttsx3.init();
def add_fn(count):
    correct_ans = 0;
    for i in range(count):
        first_num = random.randint(50,99);
        sec_num = random.randint(50,99);
        print("\nWhat is ",first_num, " + ",sec_num,"?");
        time.sleep(10);
        ans = int(input("Enter The Answer: "));
        if ans == (first_num+sec_num):
            print("\nYou Are Correct");
            correct_ans = correct_ans + 1;
        else:
            print("\nYou Are Wrong. Its ",first_num+sec_num);
    engine.say("Please find your scores.")
    print("Total Questions: ", count);
    print("Correct Answered: ",correct_ans);
    print("Average Score: ",(100*correct_ans)/count);
    engine.runAndWait()
    engine.stop()

def sub_fn(count):
    correct_ans = 0;
    for i in range(count):
        first_num = random.randint(50, 99);
        sec_num = random.randint(1, 49);
        print("\nWhat is ", first_num, " - ", sec_num, "?");
        time.sleep(10);
        ans = int(input("Enter The Answer: "));
        if ans == (first_num + sec_num):
            print("\nYou Are Correct");
            correct_ans = correct_ans + 1;
        else:
            print("\nYou Are Wrong. Its ", first_num - sec_num);
    engine.say("Please find your scores.")
    print("Total Questions: ", count);
    print("Correct Answered: ", correct_ans);
    print("Average Score: ", (100 * correct_ans) / count);
    engine.runAndWait()
    engine.stop()

print("1. Addition");
print("2. Subtraction");
print("3. Exit");

option = int(input("Select An Option: "));
count = int(input("Enter how many questions to be generated: "));
if option == 1:
    print("Welcome to Addition Math");
    add_fn(count);
elif option == 2:
    print("Welcome to Subtraction Math");
    sub_fn(count);
else:
    exit();
