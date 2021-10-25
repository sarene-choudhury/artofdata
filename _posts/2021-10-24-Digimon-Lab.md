---
layout: post
title: Digimon Lab
subtitle: By Sarene
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

##Starting the Assigment

When first approaching this lab, I used my code for the penguins data assignment as a guide. This was how I imported and opened the dataset as a list, and then initialized variables for the two columns in the dataset I wanted to make lists outs of.

~~~
import csv

with open("datasets/digimon.csv", "r") as f:
    data = list(csv.DictReader(f))

    for digimon in data:
        Speed = digimon["Spd"]
        Type = digimon["Type"]
~~~

##Question 1

The first question was the simplest, and from the start I knew I just had to find the sum of all the speeds and then divide that by the number of digimon there were. As such, I knew I had to make a list, and I actually ended up unnecessarily making a table with the digimons and their speed, since that's what I did for the penguins dataset. Zack helped me realize that it was unnecessary, and once I got rid of the table my code was concise and perfectly functional. 

~~~
    list_of_speed = []

    list_of_speed.append(int(Speed))

    Average_speed = sum(list_of_speed)/len(list_of_speed)
    print(Average_speed)
~~~

##Question 2
