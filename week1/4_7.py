"""4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
print the numbers in your list"""


mutliple_list=list(range(3,31,3))

for number in mutliple_list:
    print(number)
    

cubes =[]
for value in range(1,11):
    cubes.append(value ** 3)    
    
    
cubes = [value ** 3 for value in range(1,11)]  

print(f"first ten tubes \n {cubes}") 

 