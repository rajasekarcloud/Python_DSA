import random;
import os;
import time;

def add_fn(count):
    for i in range(count):
        first_num = random.randint(50,99);
        sec_num = random.randint(50,99);
        print("What is ",first_num, " + ",sec_num,"?");
        time.sleep(10);
        print("Time UP. Enter Any Key To Continue");
        input("");
        print("Answer is ",first_num+sec_num);

def sub_fn(count):
    for i in range(count):
        first_num = random.randint(50, 99);
        sec_num = random.randint(10, 50);
        print("What is ",first_num, " - ",sec_num,"?");
        time.sleep(10);
        print("Time UP. Enter Any Key To Continue");
        input("");
        print("Answer is ", first_num - sec_num);

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


