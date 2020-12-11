# Creating a new text file.

f = open("writee.txt", "w")                     # 'f' is file handle. 'w' is write mode.
f.write("It's a beautiful day out there. ")     # With the help of 'f.write' we can write the file.

f.close()                                       # Command to close file.

# Append Function in File writing

f = open("writee.txt", 'a')                     # here 'a' is used for appending the file.
f.write("\nIt's so hot in here.")               # \n is new line character

f.close()

# Tip : In append the previous data in file is still there.


# How to find the number of character returned by append command.

f = open("writee.txt", 'a')
a = f.write("\nIt's so hot in here.")           # Here a return number of charaters present in file.
print(a)

