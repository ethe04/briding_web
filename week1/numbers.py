even_numbers = list(range(2,11,2)) #start, stop, step
print(even_numbers)

num_list = [4,5,6,7,8]
num_list2 = list(range(4,9))
a_tuple = (1,)
print(type(a_tuple))
b_tuple = tuple([4,5,6])


squares = []
tubes = []
for value in range(1,11):
    square = value ** 2
    tubes.append(value ** 3)
    squares.append(square)
    
print(f"squate list\n {squares}")
print(f"cube list\n{tubes}")    


square_list = [value **2 for value in range(1,11)]
print(square_list)