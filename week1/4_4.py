"""One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.""" 

million_list = list(range(1,1000001))

for number in million_list:
    print(number,end=" ")

