#1) Read and display contents of file
file=open("C:\\Users\\Monisha Menon\\Desktop\\Core\\Python\\Python_Assignments\\Assignment_5\\exercise1.txt",'r')
print(file.read())

#2) Copy contents of one file to another
with open("C:\\Users\\Monisha Menon\\Desktop\\Core\\Python\\Python_Assignments\\Assignment_5\\source.txt", 'r') as source:
    content = source.read()  
with open("C:\\Users\\Monisha Menon\\Desktop\\Core\\Python\\Python_Assignments\\Assignment_5\\destination.txt", 'w') as destination:
    destination.write(content) 
    
#3) Read and count the words
with open("C:\\Users\\Monisha Menon\\Desktop\\Core\\Python\\Python_Assignments\\Assignment_5\\count.txt", 'r') as count:
    content = count.read()
words = content.split()
word_count = len(words)
print("Total number of words in the file is:",word_count)

#4) Converting string to integer
a = input("Enter a string to convert to an integer: ")
try:
    result = int(a)
    print("The converted integer is:", result)
except ValueError:
    print("Error: The input is not a valid integer.")

#5) Raise exception when integer list is negative
b = input("Enter a list of integers separated by spaces: ")
try:
    integer_list = [int(x) for x in b.split()]
    for number in integer_list:
        if number < 0:
            raise ValueError("Negative integer found")   
    print("All integers are non-negative.")  
except ValueError as e:
    print("Error",e)

#6) Compute average
try:
    c = input("Enter a list of integers separated by spaces: ")
    integer_list = [int(x) for x in c.split()]
    total = sum(integer_list)
    count = len(integer_list)    
    if count == 0:
        raise ZeroDivisionError("Cannot compute an average.")    
    average = total / count
    print("Average is: ",average)
except ValueError:
    print("Error: Enter only integers separated by spaces")
except ZeroDivisionError as e:
    print("Error",e)
finally:
    print("Program has finished running.")
    
#7) Input a filename and write a string to that file
try:
    filename = input("Enter the filename: ")
    file = open(filename, "w")
    file.write("This is a sample text.\n")
    file.close()
    print("File written successfully! Welcome!")
except Exception as e:
    print("Error",e)


