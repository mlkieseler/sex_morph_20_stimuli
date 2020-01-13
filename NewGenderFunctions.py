import matplotlib.pyplot as plt
import numpy as np
import csv
import os


#PATH = "/Users/LevineMa/Desktop/LAB/Results Expression Morph/"
PATH = ""
SAVE = ""

subjectGlob = ""
resultsList = []    #List of all the files that need to be looked at

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
#Global lists to store all the times "e" and "i" occur at each interval (0% to 100%)

analyses = {
#       0:{
 #           "e": 0,
  #          "i": 0
   #     },"""
        1:{
            "e": 0,
            "i": 0
        },
        2:{
            "e": 0,
            "i": 0
        },
        3:{
            "e": 0,
            "i": 0
        },
        4:{
            "e": 0,
            "i": 0
        },
        5:{
            "e": 0,
            "i": 0
        },
        6:{
            "e": 0,
            "i": 0
        },
        7:{
            "e": 0,
            "i": 0
        },
        8:{
            "e": 0,
            "i": 0
        },
        9:{
            "e": 0,
            "i": 0
        }
#       10:{
 #          "e": 0,
  #         "i": 0
   #    }
    }   #Dictionary that maps each interval (0% to 100%) to a dictionary of how many times "e" or "i" occurs at each interval. Initially at 0 for everything

itemAnalysis = {

}   #Dictionary that maps everything important for the item analysis

x = []      #Stores the values for the x axis of the graph (Intervals)
yE = []     #Stores the values for the y axis of the graph for the percentage of times the person or people pressed "E"
yI = []     #Stores the values for the y axis of the graph for the percentage of times the person or people pressed "I"     #These are the global variables to store x and y values for the graph

#Initializes the dictionary that has the data that is used for the item analysis (Puts everything into dictionary and sets it equal to 0). Used for individual item analysis
def itemAnalysisMapMaker(filename):                     #Initializes and then populates the item analysis dictionary
    file = open(PATH + filename, 'r')
    for line in file:                                   #Loops through all the lines in the file and splits them at every comma
        splitCsv = line.split(",")
        try:
            splitLine = splitCsv[3].split()             #Tries to split the already split lines at every space      #IMPORTANT: Change the number in this row to be the column where the name of the stimulus occurs
            for value in splitLine:
                if value[value.__len__() - 1] == "F":   #If the last letter in a word is "F" it adds that word to the item analysis map
                    itemAnalysis[splitLine[0]]={}
        except IndexError:
            splitLine = splitLine
        for value in itemAnalysis:          #Initializes the item analysis dictionary
            itemAnalysis.get(value)["(1)"] = {"e":0, "i":0}     #Order of dictionary is continuum -> step -> e or i -> 0
            itemAnalysis.get(value)["(2)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(3)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(4)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(5)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(6)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(7)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(8)"] = {"e":0, "i":0}
            itemAnalysis.get(value)["(9)"] = {"e":0, "i":0}

    itemAnalysisMapPopulator(filename)

#Populates the map for the item analysis with all the data that is necessary
def itemAnalysisMapPopulator(filename):
    file = open(PATH + filename, 'r')
    for line in file:
        importantInformation = []           #Stores all the information that is important for the dictionary (continuum, step, and response)
        splitCsv = line.split(",")
        try:
            try:
                importantInformation.append(splitCsv[3].split()[0])     #continuum      #IMPORTANT: change the first number you see in this row to be the column where the stimulus name occurs. Same for the line below
                importantInformation.append(splitCsv[3].split()[1])     #step
                importantInformation.append(splitCsv[14])               #e or i (response)  #IMPORTANT: Change the number in this row to be the column where the 'e' or 'i' response is recorded
                itemAnalysis.get(importantInformation[0]).get(importantInformation[1])[importantInformation[2]] += 1        #Uses the important information to populate the item analysis dictionary
                # Order of dictionary is continuum -> step -> e or i -> how many times e or i occurs
            except AttributeError:
                importantInformation = importantInformation
        except IndexError:
            importantInformation = importantInformation

#Makes the graphs using matplotlib
def groupItemAnalysisGraph():
    n_groups = 9                #How many values will be on the x axis
    male = []                   #Empty list to store how many times male is chosen
    female = []                 #Empty list to store how many times female is chosen
    for value in itemAnalysis:
        for number in itemAnalysis.get(value):
            male.append(itemAnalysis.get(value).get(number).get('e'))       #Puts how many times 'e' was chosen into the male list by using the item analysis dictionary
            female.append(itemAnalysis.get(value).get(number).get('i'))     #Puts how many times 'i' was chosen into the female list by using the item analysis dictionary

        fig, ax = plt.subplots()                        #https://pythonspot.com/matplotlib-bar-chart/
        index = np.arange(n_groups)                     #Makes a list of how many things on the x axis we will use (0-8)
        bar_width = 0.35

        rects1 = plt.bar(index, male, bar_width, color='b', label='Male')                   #Initializes bar graph for male values
        rects2 = plt.bar(index + bar_width, female, bar_width, color='r', label='Female')   #Initializes bar graph for female values

        plt.xlabel('Continuum')
        plt.ylabel('Number Out Of 400')     #IMPORTANT: Change this title to say 'Number Out Of (10 times the second number in row 245 and 246)'
        plt.title(value + " Group Analysis")
        plt.xticks(index + (bar_width/2), ('10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'))      #Says what x values we will have and how far apart they should be
        plt.legend()

        plt.tight_layout()      #Makes plot fit in the graph space
        plt.savefig(SAVE + value + " Group Analysis")
        plt.show()
        male.clear()
        female.clear()

#Goes through the file that you want to get information from and puts all the information into lists that can be used later
def parser(filename):
    file = open(PATH + filename, 'r')
    for line in file:
        splitLine = line.split(",")     #Split all the lines in the csv file at commas
        for line in splitLine:          #Loop through all the lines
            for word in line.split():   #Loop through all the words in the line
                if word[0] == "(":      #If the first character is a "(" use the try-except to see if the next value is an integer
                    try:
                        value = int(word[1])    #Check if second letter is an integer
                        if value == 1:          #If second letter is an integer check what the integer is. Depending what the integer is append the "e" or "i" to the list matching the integer
                            one.append(splitLine[14])       #IMPORTANT: Change the number in this line and all other lines that are number.append(splitLine[#]) to whatever line it says where the person selected 'e' or 'i'
                        if value == 2:
                            two.append(splitLine[14])
                        if value == 3:
                            three.append(splitLine[14])
                        if value == 4:
                            four.append(splitLine[14])
                        if value == 5:
                            five.append(splitLine[14])
                        if value == 6:
                            six.append(splitLine[14])
                        if value == 7:
                            seven.append(splitLine[14])
                        if value == 8:
                            eight.append(splitLine[14])
                        if value == 9:
                            nine.append(splitLine[14])
                    except ValueError:          #If the second letter in the word isn't an integer an error will be thrown and if that error is thrown do nothing
                        value = 0

#Populates analyses dictionary for the different steps with how many times e and i occur
def analysis(list1, list2, list3, list4, list5, list6, list7, list8, list9):
    #Puts how many times "e" and "i" occur at each interval in the analyses dictionary
    for value in list1:
        if value == "e":
            analyses.get(1)["e"] += 1
        if value == "i":
            analyses.get(1)["i"] += 1
    for value in list2:
        if value == "e":
            analyses.get(2)["e"] += 1
        if value == "i":
            analyses.get(2)["i"] += 1
    for value in list3:
        if value == "e":
            analyses.get(3)["e"] += 1
        if value == "i":
            analyses.get(3)["i"] += 1
    for value in list4:
        if value == "e":
            analyses.get(4)["e"] += 1
        if value == "i":
            analyses.get(4)["i"] += 1
    for value in list5:
        if value == "e":
            analyses.get(5)["e"] += 1
        if value == "i":
            analyses.get(5)["i"] += 1
    for value in list6:
        if value == "e":
            analyses.get(6)["e"] += 1
        if value == "i":
            analyses.get(6)["i"] += 1
    for value in list7:
        if value == "e":
            analyses.get(7)["e"] += 1
        if value == "i":
            analyses.get(7)["i"] += 1
    for value in list8:
        if value == "e":
            analyses.get(8)["e"] += 1
        if value == "i":
            analyses.get(8)["i"] += 1
    for value in list9:
        if value == "e":
            analyses.get(9)["e"] += 1
        if value == "i":
            analyses.get(9)["i"] += 1

#Gets the percent of times e and i are chosen and updates the analyses dictionary with that data for the group analysis
def getPercentage(list):
    for value in list:
        list.get(value)["e"]= 100 * list.get(value)["e"] / 800      #IMPORTANT: Change the second number in this row to be 10 * the second number occuring in rows 246 and 247
        list.get(value)["i"]= 100 * list.get(value)["i"] / 800
    for value in list:
        x.append(value)
        yE.append(list.get(value)["e"])
        yI.append(list.get(value)["i"])

# Gets the percent of times e and i are chosen and updates the analyses dictionary with that data for the individual analysis
def getPercentageIndividual(list):
    for value in list:
        list.get(value)["e"]= 100 * list.get(value)["e"] / 40       #IMPORTANT: Change the last number to be number of repetitions per stimulus times the number of stimuli in both this line and the line below
        list.get(value)["i"]= 100 * list.get(value)["i"] / 40
    for value in list:
        x.append(value)
        yE.append(list.get(value)["e"])
        yI.append(list.get(value)["i"])

#Resets all global variables. Used to switch from the group analysis to individual analyses
def reset():
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine
    global analyses
    global x
    global yE
    global yI
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    analyses = {
        1: {
            "e": 0,
            "i": 0
        },
        2: {
            "e": 0,
            "i": 0
        },
        3: {
            "e": 0,
            "i": 0
        },
        4: {
            "e": 0,
            "i": 0
        },
        5: {
            "e": 0,
            "i": 0
        },
        6: {
            "e": 0,
            "i": 0
        },
        7: {
            "e": 0,
            "i": 0
        },
        8: {
            "e": 0,
            "i": 0
        },
        9: {
            "e": 0,
            "i": 0
        }
    }
    x = []
    yE = []
    yI = []

#Writes CSV for group analysis
def outputGroupAnalysis(filename):
    file = open(SAVE + filename + ".csv", 'w')
    file.write("Group Analysis\n\n")
    file.write(analyses.__str__() + "\n\n\n")
    reset()

#Writes CSV for single subject analysis
def outputSingleAnalysis(filename, inputFile):
    file = open(SAVE + filename + ".csv", 'w')
    file.write("Individual Analysis\n\n")
    parser(inputFile)
    analysis(one, two, three, four, five, six, seven, eight, nine)
    getPercentageIndividual(analyses)
    file.write(analyses.__str__())
    reset()
    file.close()

# Makes a graph with the title passed into the program and the data stored in x, yE, and yI
def makeGraph(title):
    plt.plot(x, yE, color="blue")
    plt.title(title)
    plt.xlabel("Interval")
    plt.ylabel("Percent Chose Male")
    plt.savefig(SAVE + title)
    plt.show()

#Runs all the code needed for the single analysis
def singleAnalysis(resultsNumber, graphName):
    parser(resultsNumber)       #Goes through the file that you want to get information from and puts all the information into lists that can be used later
    analysis(one, two, three, four, five, six, seven, eight, nine)  #Populates analyses dictionary for the different steps with how many times e and i occur
    getPercentageIndividual(analyses)   # Gets the percent of times e and i are chosen and updates the analyses dictionary with that data for the individual analysis
    makeGraph(graphName)    # Makes a graph with the title passed into the program and the data stored in x, yE, and yI
    reset()
    outputSingleAnalysis(graphName, resultsNumber)     #Makes a CSV for the single analysis

#Same code as groupItemAnalysisGraph but with a different name
def individualItemAnalysisGraph(filename):
    subject = ""
    n_groups = 9
    male = []
    female = []
    file = open(PATH + filename)
    for line in file:
        splitLine = line.split(",")
        try:
            if splitLine[5] == "en-US":     #IMPORTANT: Change to whatever number column has en-US in it (or some other similar factor on all documents) and if you change it for a cell that doesn't have en-US in it change the word at the end to whatever the new word in the column is
                subject = splitLine[9]      #IMPORTANT: Change to whatever number column has the name in it
        except IndexError:
            subject = subject
    for value in itemAnalysis:
        for number in itemAnalysis.get(value):
            male.append(itemAnalysis.get(value).get(number).get('e'))
            female.append(itemAnalysis.get(value).get(number).get('i'))

        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35

        rects1 = plt.bar(index, male, bar_width, color='b', label='Male')
        rects2 = plt.bar(index + bar_width, female, bar_width, color='r', label='Female')


        plt.xlabel('Continuum')
        plt.ylabel('Number Out Of Twenty')      #IMPORTANT: Change the words in the single quotes to say 'Number out of (number of repetitions per stimulus)'
        plt.title(value + " Analysis Subject " + subject)
        plt.xticks(index + (bar_width/2), ('10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%'))
        plt.legend()

        plt.tight_layout()
        plt.savefig(SAVE + value + " Analysis Subject " + subject)
        plt.show()
        male.clear()
        female.clear()
    reset()

def individualItemAnalysisLineGraph(filename):
    subject = ""
    male = []
    female = []
    file = open(PATH + filename)

    for line in file:
        splitLine = line.split(",")
        try:
            if splitLine[5] == "en-US":     #IMPORTANT: See individualItemAnalysisGraph for details on what to do for this line and the line under it
                subject = splitLine[9]
        except IndexError:
            subject = subject
    makeCSVIndividualItemAnalysis(subject)
    for value in itemAnalysis:
        for number in itemAnalysis.get(value):
            male.append(itemAnalysis.get(value).get(number).get('e'))
            female.append(itemAnalysis.get(value).get(number).get('i'))
        getPercentageIndividualItemAnalysis(male)
        fig, ax = plt.subplots()
        index = np.arange(1, 10)



        plt.plot(index, yE, color="blue")
        plt.xlabel('Continuum')
        plt.ylabel('Percent Chose Male')
        plt.title(value + " Analysis Subject " + subject)
        plt.savefig(SAVE + value + " Line Graph Analysis Subject " + subject)
        plt.show()
        male.clear()
        female.clear()
        yE.clear()
    reset()

def getPercentageIndividualItemAnalysis(list):
    for value in list:
        yE.append(100 * value / 20)     #IMPORTANT: Change the number in this line to how many repetitions per stimulus there are

#Makes a CSV file with all the data for each subject's infividual item analysis
def makeCSVIndividualItemAnalysis(subject):
    csvFile = open(SAVE + "csvFile for " + subject + ".csv", 'w')
    csvFile.write("Subject,Stimula,Continuum,e,i,\n")
    print(subject + ": " + itemAnalysis.__str__())
    for stimuli in itemAnalysis:
        for continuua in itemAnalysis.get(stimuli):
            csvFile.write(subject + "," + stimuli + "," + continuua.strip("()") + ",")
            for results in itemAnalysis.get(stimuli).get(continuua):
                csvFile.write(str(itemAnalysis.get(stimuli).get(continuua)[results]/20) + ",")      #IMPORTANT: Change the number in this line to how many repetitions per stimulus there are
            csvFile.write("\n")

