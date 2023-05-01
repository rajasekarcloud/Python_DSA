# Get the number input from the user.
# Append the number to the list.
# Exit the code if "done" is pressed
# Once pressed "done" calculate the average of the numbers
list = [];
def problem():
    while True:
        num = input("Enter a number: ");
        if num == 'done':
            break;
        else:
            list.append(int(num));
    ans = sum(list)/len(list);
    print("Average is: ", ans, list);
problem();
