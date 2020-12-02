# ===========================================
# Interview Question --- December 2nd, 2020
# ===========================================
# Objective:
#     - Create a function to pass in a 'task', sort the 'task' respected objectives (values), and print the output.
# ===========================================
# Note:
#     - Create and write to output file was not originally required to answer this question 
# ===========================================

# Solution to Interview Question
def sortTask(task, myTask):
    myArr = []
    tempArr = []
    myArr = myTask.get(task)

    for x in myArr:
        tempArr.append(x)
        tempArr.sort()
    # print (tempArr)   *** Printing from Output File ***
    return tempArr

# Task and objectives to be sorted
myTask = {
    "A" : [],
    "B" : ["A", "B"],
    "C" : ["C", "A", "B"],
    "D" : ["A"],
    "E" : ["B", "D", "A"],
}

# Produces and sets sorted task objectives to an output array
outputList = []
outputList.append(sortTask('A', myTask))
outputList.append(sortTask('B', myTask))
outputList.append(sortTask('C', myTask))
outputList.append(sortTask('D', myTask))
outputList.append(sortTask('E', myTask))

# Produces output file for write and iterates through outputList
with open("output.txt", "w") as outputFile: 
    for x in outputList:
        if outputList[0:]:
            outputFile.write("%s\n" % x)
        else:
            outputFile.write("%s" % x)
outputFile.close()

# Opens and reads output file with expected values 
readFile = open("output.txt", "r") 
expectedOutput = readFile.read()
expectedOutput = expectedOutput[:-1]
print(expectedOutput)
readFile.close()

