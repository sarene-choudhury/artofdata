story = { 
 "title": "Invisible Planets", 
 "author": "Hao Jingfang", 
 "published": 2013 
} 
story["words"] = 6359
story["title"] = "Folding Beijing"
story["translator"] = "Ken Liu"
del story['published']

print(story)

classrooms = {
    "B48": 14
}

classrooms["B48"] = 15
del classrooms['B48']


def count(list):
    dictionary = { list[0]: 1}
    for x in range(1, len(list)):
        if x not in dictionary.keys():
            dictionary[list[x]] = 1
        else:
            dictionary[list[x]] += 1
    return dictionary