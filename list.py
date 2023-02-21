names = ["Jonh", "Jane", "Joey", "Jack"]

# Read Value
print(names)
print(names[1])
print(names[2], names[3])

print(names[-1])
print(names[-2])

# Update Value
names[2] = "Jonhny"
print(names)
print(names[2])

# Add new value
names.append("Bobby")
names.insert(0, "Samit")
print(names)

# Remove First Item
names.pop(0)
print(names)

# Remove Last Item
names.pop(-1)
print(names)

# Count Index
print(len(names))

# loop list
for i, n in enumerate(names):
    print(i, n)
