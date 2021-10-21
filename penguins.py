#Sarene

import csv
with open("datasets/penguins.csv", "r") as f:
    data = csv.DictReader(f)
    table = {}
    for penguin in data:
        #Initializes variables for the columns species, island, bill_length, and body_mass in penguins.csv 
        species = penguin["species"]
        island = penguin["island"]
        bill_length = penguin["bill_length_mm"]
        body_mass = penguin["body_mass_g"]


        #Creates a table
        if species not in table:
            table[species] = {}
            table[species]["bill_length"] = []
            table[species]["body_mass"] = []
        if island not in table[species]:
            table[species][island] = 0
        table[species][island] += 1   
        table[species]["body_mass"].append(body_mass)
        table[species]["bill_length"].append(bill_length)

    print(table)

#Which species of penguins has the longest bills (on average)?
Adelie_bill_length = sum(table["Adelie"][bill_length])/len(table["Adelie"]["bill_length"])
Gentoo_bill_length = sum(table["Gentoo"]["bill_length"])/len(table["Gentoo"]["bill_length"])
Chinstrap_bill_length = sum(table["Chinstrap"]["bill_length"])/len(table["Chinstrap"]["bill_length"])

if Adelie_bill_length > Gentoo_bill_length and Adelie_bill_length > Chinstrap_bill_length:
    print("Adelie has the longest bills (on average)")
if Gentoo_bill_length > Adelie_bill_length and Gentoo_bill_length > Chinstrap_bill_length:
    print("Gentoo has the longest bills (on average)")
if Chinstrap_bill_length > Adelie_bill_length and Chinstrap_bill_length > Gentoo_bill_length:
    print("Chinstrap has the longest bills (on average)")

#Which species of penguins is the most massive (on average)?
Adelie_body_mass = sum(table["Adelie"]["body_mass"])/len(table["Adelie"]["body_mass"])
Gentoo_body_mass = sum(table["Gentoo"]["body_mass"])/len(table["Gentoo"]["body_mass"])
Chinstrap_body_mass = sum(table["Chinstrap"]["body_mass"])/len(table["Chinstrap"]["body_mass"])

if Adelie_body_mass > Gentoo_body_mass and Adelie_body_mass > Chinstrap_body_mass:
    print("Adelie has the greatest body mass (on average)")
if Gentoo_body_mass > Adelie_body_mass and Gentoo_body_mass > Chinstrap_body_mass:
    print("Gentoo has the greatest body mass (on average)")
    print("Chinstrap has the greatest body mass (on average)")

#How many Chinstrap penguins are on Dream Island?
Chinstrap_on_Dream_Island = table["Chinstrap"]["Dream"]    
print("there are" , Chinstrap_on_Dream_Island , "Chinstrap penguins on Dream Island")        

    