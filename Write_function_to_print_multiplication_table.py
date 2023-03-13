# Write a function to print multiplication table of a given numbers.


def print_table(num): 
    for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 

# input a number
n = int(input("Please Enter a number to print its multiplication table:"))

# call the function tanle by passing actual parameter 'n' 

print_table(n)

