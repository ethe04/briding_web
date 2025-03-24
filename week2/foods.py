my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print(f"My favorite foods are: {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")
my_foods[0]='cheese pizza'
print(f"\nfriends food list' {my_foods}")
print('\nfriends food list',friend_foods)