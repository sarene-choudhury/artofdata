---
layout: post
title: Descriptive Lab
subtitle: By Sarene
gh-repo: daattali/beautiful-jekyll
gh-badge: [star, fork, follow]
tags: [test]
comments: true
---

## 1. Which dataset did you work with?

I worked with a dataset with statistics about Marvel characters

## 2. Which aspect of this dataset are you interested in? What do you hope to learn from analyzing this dataset?

I’m interested to see how the stats of the good, bad, and neutral characters compare, as I hypothesize that the good will tend to have the ‘best’ statistics (on average more powerful, more intelligent, etc.)

## 3. (I also draw my conclusions for question 4 in my answers for these questions) Discuss your analysis of the dataset. Include details such as:

## a) The variables you looked at

Since there were only six variables besides the alignment (good, bad, and neutral), which I used as an axes of comparison for all of the other variables, I looked at all six provided by the dataset: intelligence, strength, speed, durability, power, and combat, and the total of those values added together.

## b) Distributions of variables (center and variability)

When I looked at the summary statistics of various variables with respect to the three alignments, I found that while many stats were similar, there was an interesting difference between all the other stats and the stats for Speed. 

The means for Durability: Good = 39.29, Bad = 46.28, Neutral = 75.55
The means for Speed: Good = 26.69, Bad = 27.68, Neutral = 46.73

When looking at the means for all of the variables, I found that all of them except that of speed had a similar ratio between the three alignments. As shown above, the speed of good and bad characters were, on average, basically the same (the means of Intelligence had a practically perfect difference of 10 between each alignment), while the mean speed of neutral characters kept to the trend of being of the greatest value. The reason I find this anomaly to be interesting is because it begs the question: why speed? what about this variable differentiates itself (or rather, doesn't) from the trend? It doesn't seem to be from a certain capping point of speed imposed on all characters, as the mean for neutral is about double that of good and bad. 

The range of the variables was also interesting, as while one would assume it would be between 0 and 100, it was in fact not. The max for all of the variables was 100, and while the minimum for the good and bad characters was either 0 or 1 (characters have to have at least 1% of intelligence to function I gathered), the minimum for neutral characters was at least 10, and actually was 38 for Intelligence. From this I figured that to be a neutral character and refrain from having an alignment to good or bad, the intelligence levels would be higher, on average, because that would mean staying out of a fight and knowing more about self-preservation.

## c) Relationships between variables

The only relationship between the variables that I observed in the data was how, without fail, the stats for good would be worse than that of bad, which would be worse than that of neutral.

## d) Visualizations of the dataset

I found that violin plots were very helpful versus, for example, using scatterplots, and so I made them for each variable, as well as the total, to get the overarching picture of the differences between good, bad, and neutral.

Figure 1: "/assets/img/avatar-icon.png"
Figure 2: "/assets/img/avatar-icon.png"
Figure 3: "/assets/img/avatar-icon.png"
Figure 4: "/assets/img/avatar-icon.png"
Figure 5: "/assets/img/avatar-icon.png"
Figure 6: "/assets/img/avatar-icon.png"
Figure 7: "/assets/img/avatar-icon.png"
Figure 8: "/assets/img/avatar-icon.png"


## e) Limitations of your analysis and the dataset

This dataset may contain a solid few hundred marvel characters, but still doesn't encompass every single one of the characters, but the biggest limitation is how few variables it looks at. I did find an other dataset with significantly more variables, but unfortunately it only provided true or false values instead of numbers, as this dataset does. Such a binary dataset would have limited my analysis more than my general lack of experience with analysing datasets, and so I found and used this dataset instead. Another limitation of this dataset, however, is how the absolute minimum is 0 and the absolute maximum is 100, and so it cannot capture the nuance of varying stat levels of the characters. For example, the phoenix is significantly more powerful War Machine considering it is a comparison between a cosmic force of creation and a soldier in a metal suit, yet the Power level of both is 100.


