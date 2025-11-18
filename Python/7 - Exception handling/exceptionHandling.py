# Exception Handling
# Exception execute a block of code that may raise an exception
# Exception handling is a mechanism to handle runtime errors

try:
    a=a
except NameError as err:
    print("An error occurred", " | ", err)


# Exception a especific type of error
try:
    a=1/0
    a=c
except ZeroDivisionError as tx: # Only one error will be raised
    print('Erro divisão por 0 - ', tx)


# else
# After all, the else block will execute if no exception is raised
try:
    number = int(input("Enter a number: "))
    result = number + 10
except ValueError as err:
    print("Invalid input:", err)
else: # Not executed when we get an error!
    print("Result:", result)


# Finally -> Ocorre sempre, mesmo que tenha ou não erro
try:
    number = int(input("Enter a number: "))
    result = number + 10
except ValueError as err:
    print("Invalid input:", err)
else: # Not executed when we get an error!
    print("Result:", result)
finally:
    print('Fim')
