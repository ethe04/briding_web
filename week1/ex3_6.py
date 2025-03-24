friends = ['Kaung','Moe','May']
print("Wow! we've got a bigger dinner table.")

friends.insert(0,'Ko Ko')
friends.insert(2,'Sabdi')
friends.append('Yuya')
print(f"{friends[0]}, please join the dinner tonight.")
print(f"{friends[1]}, please join the dinner tonight.")
print(f"{friends[2]}, please join the dinner tonight.")
print(f"{friends[3]}, please join the dinner tonight.")
print(f"{friends[4]}, please join the dinner tonight.")
print(f"{friends[5]}, please join the dinner tonight.")

print("Unluckily, there is only two people we can invite for dinner")
print(f" {friends.pop()}, We are sorry to inform that we can't invite you to dinner.")
print(f" {friends.pop()}, We are sorry to inform that we can't invite you to dinner.")
print(f" {friends.pop()}, We are sorry to inform that we can't invite you to dinner.")
print(f" {friends.pop()}, We are sorry to inform that we can't invite you to dinner.")

print(f"{friends[0]}, you are invited to dinner.")
print(f"{friends[1]}, you are invited to dinner.")

del friends[0]
del friends[0]
print(f"after deleting two guests from list {friends}")
