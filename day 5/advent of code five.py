import math

with open('D:\Programming Stuff\Python\Advent of Code 2024\day 5\sampinp.txt', 'r') as file:
    samp_inp = file.read()

#Organizing sample input
org = samp_inp.split()
rules = []
updates = []
valid = []
invalid = []

for item in org:
    if "|" in item:
        rules.append(item)
    else:
        updates.append(item)

#splitting input into rules and updates
rulers = []
print(updates)

for item in rules:
    rulers.append(item.split("|"))

#an extremely obtuse way of checking if each update follows the rules

for item in updates:
    j = 0
    grubbo = item.split(",")
    for plibby in grubbo:
        for tumbo in rulers:
            if plibby == tumbo[1]:
                if tumbo[0] in grubbo:
                    if grubbo.index(plibby) < grubbo.index(tumbo[0]):
                        j +=1
                        break
                    else:
                        continue
                        
                else:
                    continue
            else:
                continue
    if j > 0:
        print(f"{grubbo} is invalid")
        invalid.append(grubbo)
        j = 0
    else:
        valid.append(grubbo)
        print(f"{grubbo} is valid")


#finding the middle of each list and then summing     
middles = []
for item in valid:
    middle = math.ceil(len(item)/2) - 1
    middles.append(item[middle])

fin_middles = list(map(int,middles))
print(f"Sum of valid midpoints: {sum(fin_middles)}")

#I am so sorry for what you are about to see, but I am correcting each incorrect entry
reformation = []
for item in invalid:
    itemr = item
    for number in item:
        for rule in rulers:
            if number == rule[1]:
                if rule[0] in item:
                    if item.index(number) < item.index(rule[0]):
                        a,b = item.index(number), item.index(rule[0])
                        item[b],item[a] = item[a],item[b]
                            
                    else:
                        continue
                else:
                    continue
            else:
                continue
    reformation.append(item)
     


#made it into a function, which I should have done sooner
def fixer(list):
    new = []
    for item in list:
        for number in item:
            for rule in rulers:
                if number == rule[1]:
                    if rule[0] in item:
                        if item.index(number) < item.index(rule[0]):
                            a,b = item.index(number), item.index(rule[0])
                            item[b],item[a] = item[a],item[b]
                            item = mini_fix(item)  
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
        new.append(item)
    return new

 #this is to make using the function recursively actually work   
def mini_fix(item):
    for number in item:
                for rule in rulers:
                    if number == rule[1]:
                        if rule[0] in item:
                            if item.index(number) < item.index(rule[0]):
                                a,b = item.index(number), item.index(rule[0])
                                item[b],item[a] = item[a],item[b]
                                mini_fix(item)
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue
    return item
    


reformed_middles = []
for item in reformation:
    middle = math.ceil(len(item)/2) - 1
    reformed_middles.append(item[middle])

fin_ref_middles = list(map(int,reformed_middles))
print(f"Sum of reformed midpoints: {sum(fin_ref_middles)}")
