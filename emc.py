s = {1,2,2,3,"python"}
for element in s:
    print(element)  

tup = (1,2,3,4)
print(tup[0])

set_converted = list(s)
print(set_converted[1])

#Arithmetic operations

a = 2
b = 4
print(a+b)
print(a-b)      
print(a*b)
print(a/b) 
print(a!=0)

#logical operations

print(a>0 and b>0)
print(a>0 or b<0)
print(not(a>0))
number = int(input("Enter a number: "))
if number==0:
    print("This is neither even nor odd")
elif number<0:
    print("Negative")
elif number%2==0:
    print("Even")
else:
    print("Odd")




my_list = ['css', 'html', 'python', 'javascript', 'ts', 'node']
my_name = "emmanuel"
print(my_name.upper())

upper_case_programming_languages = []
for language in my_list:
    upper_case_programming_languages.append(language.upper())
print(upper_case_programming_languages)

print(my_name[::-1])
print(', '.join(my_list))
print(my_name.split('n'))
print(my_name.replace('E', 'e'))
print(f"My name is {my_name.upper()} and I am learning {my_list[2]}")

print(f"My name is \"{my_name.upper()}\" and I am learning {my_list[2]}")

print('''My name is Bharath \n I want to learn python''')

my_list = ["css", "html", "python", "python","javascript", "ts", "node"]
my_name = "Bharath"
print(my_name.swapcase())

#5th day
print("Hello World")

x=1
y=0
try:

    print(x/y)

except Exception as e:
    print(f"An error occurred: {e}")

#i used total as a global variable and i am trying to update it inside the function but it is giving me an error because i have not declared it as global inside the function. to fix this i need to declare total as global inside the function like this: