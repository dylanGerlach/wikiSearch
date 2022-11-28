import wikipedia
import json
import editdistance
# 
def similarity(a, b):
    return 1.0 - editdistance.eval(a, b)/(1.0 * max(len(a), len(b)))
def printPage():
    for i in range(len(info)):
        print(info[i]["heading"] , "\n", info[i]["paragraph"], "\n")
def questionPrompt():
    currentInput = input(f"Your topic is {title}, what question do you have about it? \n")
    for i in range(len(info)):
        if info[i]["relevant"] == True:
            info[i]["weight"] =  similarity(currentInput, info[i]["paragraph"]) + similarity(currentInput, info[i]["heading"])
        else :
            info[i]["weight"] = 0
    
    newInfo = sorted(info, key= lambda x:x["weight"], reverse=True)
    print("Relevant topics to your search: \n" )
    for i in range(3):
        print(newInfo[i]["heading"], "\n", newInfo[i]["paragraph"], "\n")
link = input("Enter keyword or URL: ")
# The wikipedia API does not surrort URLs naturally, so this removes the URL part of the link
if "https://" in link and "wiki/" in link:
    link = link[link.find("wiki/") + 5 : len(link)]
title = wikipedia.page(link).title
print(f"topic: {title}")
info = []
# The wikipedia API sections does not include the summary, so it is added independently at the start
summary = { 
    "heading": "summary",
    "paragraph": wikipedia.page(link).summary,
    "weight": 0,  
    "relevant": True      
}
info.append(summary)
# algorithm to find the most relevant paragraphs

# Fills list with paragraphs
print("loading data...")
for i in range(len(wikipedia.page(link).sections)):
    current = { 
        "heading": wikipedia.page(link).sections[i],
        "paragraph": wikipedia.page(link).section(wikipedia.page(link).sections[i]),
        "weight": 0,
        "relevant": True        
    }
    if current["paragraph"] == "":
        current["paragraph"] = "Currently no information is available in this section, or this is a heading for the following subsections"
        current["relevant"] = False
    info.append(current)

print("data loaded")

inp = 0
while inp != -1:
    temp = input(" \n Enter (-1) to exit program \n Enter (0) to view all paragraphs \n (1) to ask question and recieve the most relevant data \n")
    inp = int(temp)
    if inp == -1:
        break
    if inp == 0:
        printPage()
    if inp == 1:
        questionPrompt()

    
  
















