locations = ['Taungyi','Innlay','Seoul','Tokyo','DisneyLand']
print(locations)

print(sorted(locations))

print(f"original list \n {locations}\n")

locations.reverse()
print(f"reverse list \n {locations}\n")

locations.reverse()
print(f"second time reversing and order of list \n {locations}\n")

locations.sort()
print(f"after sorting list \n{locations}\n")

locations.sort(reverse=True)
print(f"sorting list in reverse-alphabetical \n{locations}\n")

print(f"number of places that I like to travel: {len(locations)}")

# print(locations[5])
print(locations[-6])