my_foods = ['pizza','falafel','carrot cake']
friend_pizzas = my_foods[:]

my_foods.append("chesse pizza")
friend_pizzas.append("macroni pizza")

print("My favorite pizzas are: ")
for pizza in my_foods:
    print(pizza)
    
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)    
    
    
    