#Sarene Choudhury Digimon Lab

import csv

#opens the dataset
with open("datasets/digimon.csv", "r") as f:
    #creates a dictionary for the dataset 
    data = list(csv.DictReader(f))

    #Creates an empty list 
    list_of_speed = []

    #loops through every digimon
    for digimon in data:
        #Initializes variables for the digimon type, digimon speed, digimon memory, and digimon attack
        Speed = digimon["Spd"]
        Type = digimon["Type"]

        #Appends the values of the speeds for each digimon from Speed into the list created earlier
        list_of_speed.append(int(Speed))

    #Takes the average of the list of speeds of digimon and prints it
    Average_speed = sum(list_of_speed)/len(list_of_speed)
    print(Average_speed)

    #takes a key and counts the number of a certain value within the key
    def count_digimon(key, value):
        trait_counter = 0
        for digimon in data:
            if digimon[key] == value:
                trait_counter += 1
        return trait_counter
    print(count_digimon('Type','Vaccine'))           
    


    def digimon_teams():
        for digimon1 in data:
            for digimon2 in data:
                for digimon3 in data:
                    if (int(digimon1["Memory"]) + int(digimon2["Memory"]) + int(digimon3["Memory"]) < 15 and 
                    int(digimon1["Atk"]) + int(digimon2["Atk"]) + int(digimon3["Atk"]) > 300 and
                    digimon1 != digimon2 != digimon3):
                        return(digimon1, digimon2, digimon3) 
    print(digimon_teams())                 
