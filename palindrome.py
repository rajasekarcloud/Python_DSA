# Palindrome
# Program to check if the string is a palindrome or not
word="malayalam";
#print(word[0]); # Print first character
#print(word[-1]); # Print last character
#print(word[1:-1]); # Print strings between first and last
def palindrome(word):
   # print(word);
    if len(word) == 1:
        return True;
    else:
        return word[0] == word[-1] and palindrome(word[1:-1]);
print(palindrome(word));
