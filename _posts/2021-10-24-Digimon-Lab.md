---
layout: post
title: Digimon Lab
subtitle: By Sarene
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

## Starting the Assigment

When first approaching this lab, I used my code for the penguins data assignment as a guide. This was how I imported and opened the dataset as a list, and then initialized variables for the two columns in the dataset I wanted to make lists outs of.

~~~
import csv

with open("datasets/digimon.csv", "r") as f:
    data = list(csv.DictReader(f))

    for digimon in data:
        Speed = digimon["Spd"]
        Type = digimon["Type"]
~~~

## Question 1

The first question was the simplest, and from the start I knew I just had to find the sum of all the speeds and then divide that by the number of digimon there were. As such, I knew I had to make a list, and I actually ended up unnecessarily making a table with the digimons and their speed, since that's what I did for the penguins dataset. Zack helped me realize that it was unnecessary, and once I got rid of the table my code was concise and perfectly functional. 

~~~
    list_of_speed = []

    list_of_speed.append(int(Speed))

    Average_speed = sum(list_of_speed)/len(list_of_speed)
    print(Average_speed)
~~~

## Question 2

The second question was the one I struggled with the most, but not because I didn't know how to write the code for it. In fact, after writing my own code, I ended up getting help from Avi and Zack and completely redoing my code twice because it wasn't functioning. I knew that I needed to count the number of a certain value within a key, aka a column in the dataset, and so my first approach was to go directly into the dataset and iterate through by pulling out numbers. My code for this failed to work and I kept getting a KeyError. So, I tried a different method and created a dictionary, iterating through values from there instead of the dataset. However, I once again got a KeyError, so at this point I changed other parts of my code and reread all of it to no avail. Finally, I tried a third method that was most similar to my original method, only to get the same KeyError. It was only after consulting with Mr. Lee that I realized I had just needed to delete one word and that would fix the error, and all three of my methods would have been functional. 

~~~
def count_digimon(key, value):
        trait_counter = 0
        for digimon in data:
            if digimon[key] == value:
                trait_counter += 1
        return trait_counter
    print(count_digimon('Type','Vaccine'))       
~~~

## Question 3

For this last question, I knew I needed to think it through with proper pseudocode beforehand. The other two had been fairly simple to ideate, but to get the most concise version of the code to answer this question, working through the process in a detailed manner was necessary. The first criteria I knew I had to fulfill was comparing three digimon in a very manual way, using a counter to go through the lines and different combinations of three digimon whose Memory was each under 14. I also knew that these three hypothetical digimon needed to have a total attack greater than 300, and so I also wanted to do this in a very manual and inefficient way. This was not an effective method, but I had the right idea. After doing some research on stack overflow and testing my code with the help of Mr. Lee, I realized I could nest for loops and then use one, overarching if statement to iterate through all the different combinations of digimon teams of three until I found one that satisfied the requirements.

~~~
def digimon_teams():
        for digimon1 in data:
            for digimon2 in data:
                for digimon3 in data:
                    if (int(digimon1["Memory"]) + int(digimon2["Memory"]) + int(digimon3["Memory"]) < 15 and 
                    int(digimon1["Atk"]) + int(digimon2["Atk"]) + int(digimon3["Atk"]) > 300 and
                    digimon1 != digimon2 != digimon3):
                        return(digimon1, digimon2, digimon3) 
    print(digimon_teams())       
~~~

## Final Thoughts

This lab was definitely a challenge for me, and I think that my greatest downfall was that I tried to approach everything in a very manual way. That meant that my code was inefficient, and I also wasn't very good at finding errors. I think that when approaching the next project, I'll try and use pseudocode in a more serious way, and hopefully as a result, reach the most efficient code quicker. Overall, this was a fun learning experience and I learned a lot about how I want to code in the future.
         
