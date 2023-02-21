numbers = {1: "One", 2: "Two", 3: "Three"}
provinces = {
    "bkk": "Bangkok",
    "cha": "Chiang Mai",
    "khn": "Khon Kaen",
    "chm": "Chumphon"
}

print(numbers)
print(numbers[1])

print(provinces["cha"])
print(provinces["khn"])

print("-----------------------")

# loop dictionary
for p in provinces.keys():
    print(p)

print("-----------------------")

for p in provinces.values():
    print(p)

print("-----------------------")

for k, v in provinces.items():
    print(k, v)
