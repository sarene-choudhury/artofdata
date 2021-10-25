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
