import matplotlib.pyplot as plt
import numpy as np
import os
import NewGenderFunctions as gf

gf.PATH = input(
    "Would you like to use the default path? y/n ")  # Checks if user wants to use default path /Users/LevineMa/Desktop/LAB/Results Sex Morph/
if gf.PATH == "y":  # Uses default path if user wants to use default path
    gf.PATH = "/Users/marie/Documents/Projects/morph_project/sex_moprh/sex_morph_20_trials/data/results/63_83__113_53_inlab/sex_morph/"
elif gf.PATH == "n":  # If user doesn't want to use default path allows them to input their own path
    gf.PATH = input(
        "What is the path to your files? i.e: /Users/LevineMa/Desktop/LAB/Results Sex Morph/")  # Takes user input for the path to the files that need to be analyzed

gf.SAVE = input(
    "Would you like the files to be saved to the default folder? y/n ")  # Checks if user wants to save the graphs to the default folder
if gf.SAVE == "y":  # Uses default path if user wants to save to the default folder
    gf.SAVE = "/Users/marie/Documents/Projects/morph_project/sex_moprh/sex_morph_20_trials/data/results/63_83__113_53_inlab/sex_morph/graphs/"
elif gf.SAVE == "n":  # If user doesn't want to save to the default folder allows them to input thei own path to a folder to save in
    gf.SAVE = input(
        "What is the path to the folder you would like to save your graphs? i.e: /Users/LevineMa/Desktop/LAB/Graphs For Sex Morph/")  # Takes user input for a path to the folder they want the graphs to be saved to


for file in os.listdir(gf.PATH):
    if file[file.__len__() - 4] == ".":
        gf.resultsList.append(file)  # Gets all the files that need to be looked at for the results list


for file in gf.resultsList:
    gf.parser(file)

gf.analysis(gf.one, gf.two, gf.three, gf.four, gf.five, gf.six, gf.seven, gf.eight, gf.nine)
gf.getPercentage(gf.analyses)
gf.makeGraph("Group Analysis")
gf.outputGroupAnalysis("Group Analysis")
gf.reset()  # Code that is running for group analysis, doing the item analysis

gf.itemAnalysisMapMaker(gf.resultsList[0])
for file in gf.resultsList:
    if file != gf.resultsList[0]:
        gf.itemAnalysisMapPopulator(file)


for file in gf.resultsList:
    gf.itemAnalysisMapMaker(file)
    gf.individualItemAnalysisGraph(file)  # Code that is running for the individual item analysis

for file in gf.resultsList:
    gf.itemAnalysisMapMaker(file)
    gf.individualItemAnalysisLineGraph(file)

for file in gf.resultsList:
    read = open(gf.PATH + file, 'r')
    # Gets the subject's ID number to name the graph
    for line in read:
        splitLine = line.split(",")
        try:
            if splitLine[5] == "en-US":
                subjectGlob = splitLine[9]
        except IndexError:
            subjectGlob = subjectGlob
    gf.singleAnalysis(file, subjectGlob + " Analysis")  # Code that is running for the single analysis

gf.itemAnalysisMapMaker(gf.resultsList[0])
for file in gf.resultsList:
    if file != gf.resultsList[0]:
        gf.itemAnalysisMapPopulator(file)
gf.groupItemAnalysisGraph()