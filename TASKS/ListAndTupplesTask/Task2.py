# Wap to check if the given number is palindrome or not

test=[]

#it is incorrect a string doesnot have copy attribute
# test = input("enter anything :")

#adds the entered elements in the list
test.append(input("enter what you want to check :"))

#creates a copy of the  list
copy_test = test.copy()

#reverses the list
copy_test.reverse()

# If the reversed and the original is same it is palindrome
if (copy_test == test) :
    print("the number is palindrome")
else :
    print("the number is not palindrome ")

