import csv
with open("Datasets/favorite_colors.csv", "r") as f:
    data = csv.DictReader(f)
    table = {}
    for student in data:
        grade = student["grade"]
        color = student["favorite_color"]
        if grade not in table:
            table[grade] = {}
        if color not in table[grade]:
            table[grade][color] = 0
        table[grade][color] += 1
    print(table)

total = 0
for grade in table:
    total += table[grade]["yellow"]
print(total)

total = sum(table[grade]["yellow"] for grade in table) 

print(total)

# print(table)

#table = {
#    "9": {
#        "blue": 5,
#        "red": 6,
#        "yellow": 7
#    }
#},
#"10": {...}


