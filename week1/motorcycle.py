motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)


motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('ducati')

print(motorcycles)
motorcycles.insert(0, 'hyundai')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(f" remaining motorcycles after popping {motorcycles}")
print(popped_motorcycles)

print(motorcycles.pop(0))
print(motorcycles)